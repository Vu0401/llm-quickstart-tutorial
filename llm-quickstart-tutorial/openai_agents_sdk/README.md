# OpenAI Agents SDK

The **OpenAI Agents SDK** is a production-ready toolkit for building multi-agent AI systems — fast, modular, and powerful.

| Component     | Meaning                                                                 |
|--------------|-------------------------------------------------------------------------|
| 🧠 LLM        | The brain of the agent, powered by prompts                              |
| 🔧 Tools      | Python functions the agent can call automatically                       |
| 🛡️ Guardrails | Input/output checks to keep responses clean, safe, and structured       |
| 🗂️ Context    | Inject memory, chat history, or external data into each interaction     |


The SDK takes care of the hard stuff:
parsing, reasoning, tool-calling, and orchestration. You just plug in logic.

---

## What’s Inside?

| File                     | Core Concept          | What it shows                                                    |
| ------------------------ | --------------------- | ---------------------------------------------------------------- |
| `1_basic_agent.py`       | 🧠 Agent (LLM prompt) | Create a minimal agent: system prompt → user input → reply       |
| `2_structured_output.py` | 📦 Output formatting  | Guide the agent to return structured JSON or specific formats    |
| `3_tool_calls.py`        | 🔧 Tools              | Let the agent call Python functions automatically                |
| `4_handoffs.py`          | 🔁 Multi-agent logic  | Hand off tasks between agents or workflows                       |
| `5_input_guardrails.py`  | 🛡️ Input guardrails  | Sanitize, validate, or rephrase user input before processing     |
| `6_output_guardrails.py` | 🛡️ Output guardrails | Post-process or check the agent's response before returning      |
| `7_context.py`           | 🗂️ Context & memory  | Feed in dynamic context: past chats, external info, user history |


---

## 🚀 Run a Script

From the root of the repo:

```bash
uv run python src/openai_agents_sdk/1_basic_agent.py
```

> ⚠️ Make sure dependencies are installed from the main repo first.

## 🤔 Want to go deeper?

Curious how it all works under the hood?
> 🔍 Dive deeper with the [full official docs here](https://openai.github.io/openai-agents-python/).
