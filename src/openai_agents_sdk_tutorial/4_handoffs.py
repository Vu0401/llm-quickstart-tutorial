import asyncio
from agents import Agent, Runner, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

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

calculation_agent = Agent(
    name="Caculation Specialist",
    handoff_description="Specialist agent for multiply calculation",
    instructions=(
        "You're a helpful assistant, remember to always "
        "use the provided tools whenever possible. Do not "
        "rely on your own knowledge too much and instead "
        "use your tools to help you answer queries."
    ),
    model=model,
    tools = [multiply]
)

main_agent = Agent(
    name="Assistant",
    instructions="""
    You are helpful agent. 
    """,
    model=model,
    handoffs=[calculation_agent]
)

# --- Main Function ---

async def main():
    query = "what is the answer for 7.814 multiplied by 103.892?"
    result = await Runner.run(main_agent, query)
    response = result.final_output.strip()
    print("\nFINAL RESPONSE:", response)
    
if __name__ == "__main__":
    asyncio.run(main())