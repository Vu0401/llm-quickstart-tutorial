import os
import asyncio
from dotenv import load_dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings
from agents.run import RunConfig 
from agents.mcp.server import MCPServerStdio

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

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

model_settings = ModelSettings(temperature=0.1, top_p=0.9)

# --- Main ---

async def main():
    async with MCPServerStdio(
        params={
            "command": "uv",
            "args": ["run", "python", "src/fast_mcp_tutorial/student_management_server.py"],
        }
    ) as server:

        agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant and always use MCP tools and prompts when possible.",
            model_settings=model_settings,
            mcp_servers=[server]
        )

        queries = [
            "Get student info for ID 001",
            "Calculate average score of [6.5, 7.0, 8.0]",
            "Analyze student 002 with scores [4.0, 5.5, 6.0]",
            "Use prompt to analyze student 001 with scores [9.0, 7.5, 8.5]"
        ]

        for query in queries:
            print("=" * 50)
            print(f"🔍 Prompt: {query}")
            result = await Runner.run(agent, query, run_config=config)
            print("🧠 Output:")
            print(result.final_output)
            print("=" * 50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
