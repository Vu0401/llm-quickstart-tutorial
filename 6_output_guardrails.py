from agents import Agent, Runner, AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, GuardrailFunctionOutput, RunContextWrapper, output_guardrail
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
    return x * y

# --- Output Guardrail Agent ---

class GuardrailOutput(BaseModel):
    is_triggered: bool
    reasoning: str

output_guardrail_agent = Agent(
    model=model,
    name="Output Guardrail Agent",
    instructions="Check if the response contains political opinions or mentions the color of an apple.",
    output_type=GuardrailOutput,
)

@output_guardrail
async def politics_output_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: str
) -> GuardrailFunctionOutput:
    # Run guardrail agent to analyze the response
    response = await Runner.run(output_guardrail_agent, input=output)
    # Format response into GuardrailFunctionOutput
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=response.final_output.is_triggered,
    )
    
# --- Main Agent ---

agent = Agent(
    name="Assistant",
    instructions="You're a helpful assistant.",
    model=model,
    tools=[multiply],
    output_guardrails=[politics_output_guardrail],
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