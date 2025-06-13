# OpenAI Agents SDK Examples

Quick, no-fluff examples for OpenAI’s experimental Agents SDK. Each script focuses on one core feature — run and learn by doing.

> ⚠️ Make sure dependencies are installed from the main repo first.

---

## 🧩 What’s Inside?

| File                   | Purpose                                                       |
|------------------------|---------------------------------------------------------------|
| `1_basic_agent.py`     | Minimal agent: system prompt → user input → response          |
| `2_structured_output.py` | Make agents return structured output                        |
| `3_tool_calls.py`      | Let the agent call tools (functions)                          |
| `4_handoffs.py`        | Handoff from one agent or task to another                     |
| `5_input_guardrails.py`| Add input validation / cleanup                                |
| `6_output_guardrails.py`| Add output validation / transformation                       |
| `7_context.py`         | Inject context (e.g., memory, external info) into the agent   |

---

## 🚀 Run a Script

From the root of the repo:

```bash
uv run python src/openai_agents_sdk/1_basic_agent.py
```