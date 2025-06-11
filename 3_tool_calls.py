import asyncio
from typing import List
from pydantic import BaseModel, Field
from agents import Agent, Runner, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
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

# --- Models for structured outputs ---

class TravelPlan(BaseModel):
    destination: str
    duration_days: int
    budget: float
    activities: List[str] = Field(description="List of recommended activities")
    notes: str = Field(description="Additional notes or recommendations")

# --- Tools ---

@function_tool
def multiply(x: float, y: float) -> float:
    """Multiplies `x` and `y` to provide a precise
    answer."""
    print("tool call!")
    return x*y

# --- Agents ---

agent = Agent(
    name="Assistant",
    instructions=(
        "You're a helpful assistant, remember to always "
        "use the provided tools whenever possible. Do not "
        "rely on your own knowledge too much and instead "
        "use your tools to help you answer queries."
    ),
    # model=model,
    tools=[multiply]  # note that we expect a list of tools
)

# --- Main Function ---

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    # Example queries to test the system
    query = "what is the answer for 7.814 multiplied by 103.892?"
    
    print(f"QUERY: {query}")
        
    result = await Runner.run(agent, query, run_config=config)
    response = result.final_output.strip()
    
    print("\nFINAL RESPONSE:", response)
    
if __name__ == "__main__":
    asyncio.run(main())