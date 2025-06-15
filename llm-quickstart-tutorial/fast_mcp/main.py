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
            instructions="You are a helpful assistant and always use mcp tools to achieve the task", 
            model_settings=model_settings,
            mcp_servers = [server]
            )

        result = await Runner.run(agent, "Calculate average of [1, 2, 3]", run_config=config)

        print(result.final_output)
        
if __name__ == "__main__":
    asyncio.run(main())