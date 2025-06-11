from agents import Agent, Runner, AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, GuardrailFunctionOutput, RunContextWrapper, input_guardrail
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import asyncio

# --- Config ---

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# --- Tools ---

@function_tool
def multiply(x: float, y: float) -> float:
    """Multiplies `x` and `y` to provide a precise
    answer."""
    print("Tool Call !")
    return x*y

# --- Agents ---
class GuardrailOutput(BaseModel):
    is_triggered: bool
    reasoning: str

politics_agent = Agent(
    model=model,
    name="Politics check",
    instructions="Check if the user is asking you about political opinions or color of an apple.",
    output_type=GuardrailOutput,
)

@input_guardrail
async def politics_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str,
) -> GuardrailFunctionOutput:
    # run agent to check if guardrail is triggered
    response = await Runner.run(starting_agent=politics_agent, input=input)
    # format response into GuardrailFunctionOutput
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=response.final_output.is_triggered,
    )
    
agent = Agent(
    name="Assistant",
    instructions=(
        "You're a helpful assistant."
    ),
    model=model,
    tools=[multiply],
    input_guardrails=[politics_guardrail], 
)

async def main():
    # query = "what 2 * 4"
    query = "what is the color of an apple?"
    # query = "what do you think about the labour party in the UK?"
    
    try:
        result = await Runner.run(agent, query)
        final_output = result.final_output
        print(final_output)
    except:
        print("I can not provide an answer to this question.", "\n")
        
if __name__ == "__main__":
    asyncio.run(main())