import os
from dotenv import load_dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings
from agents.run import RunConfig

# --- Config ---


gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

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

model_settings = ModelSettings(temperature=0, top_p=0.9)

# --- Main ---

agent = Agent(name="Assistant", instructions="You are a helpful assistant", model_settings=model_settings)

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)

print(result.final_output)