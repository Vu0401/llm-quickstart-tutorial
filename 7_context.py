import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, AsyncOpenAI, function_tool, OpenAIChatCompletionsModel, RunContextWrapper
from dotenv import load_dotenv
import os

# --- Load API Key ---
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# --- Set up Gemini ---
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# --- Local Context ---

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    """Retrieves the user's age from internal context."""
    return f"User {wrapper.context.name} is 25 years old"

# --- Agent Setup ---
agent = Agent[UserInfo](
    name="Assistant",
    model=model,
    instructions="You are a helpful AI assistant. Call tool if needed.",
    tools=[fetch_user_age],  # LLM can call this tool
)

async def main():
    user_info = UserInfo(name="Alex", uid=123)  

    result = await Runner.run(
        starting_agent=agent,
        input="What is Alex age?",
        context=user_info,  # Local Context is passed in
    )

    print(result.final_output)  
    # Gemini will call `fetch_user_age()` and respond: "User Alex is 25 years old."

if __name__ == "__main__":
    asyncio.run(main())
