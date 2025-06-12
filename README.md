# ⚡ LLM Quickstart Tutorial

A plug-and-play collection of quickstart tutorials for popular LLM tools and agent frameworks.  
**No fluff. Just code. Get in, get it running, and start building cool stuff.**

---

## 😎 Choose Your Weapon

A quick overview of all available modules — click the folder to explore examples, or visit the upstream repo to learn more about the original project.

| Module             | Quickstart Folder                                                    | Upstream Repo                                                |
|--------------------|-----------------------------------------------------------------------|--------------------------------------------------------------|
| **OpenAI Agents SDK**<br/>Spin up and wire agents using OpenAI's new experimental framework | [`src/openai_agents_sdk/`](src/openai_agents_sdk/)           | [OpenAI SDK](https://github.com/openai/openai-python/tree/main/openai/agents) |
| **Mem0** 🚧<br/>Memory-first agents that learn and adapt over time                         | [`src/mem0/`](src/mem0/)                                     | [Mem0](https://github.com/mem0-ai/mem0)                     |
| **Fast MCP**<br/>Minimal controller for managing multi-agent workflows                     | [`src/fast_mcp/`](src/fast_mcp/)                             | [Fast MCP](https://github.com/minerllabs/fast-mcp) (if public) |
| **Neo4j**<br/>Integrate agents with graph databases using Neo4j                            | [`src/neo4j/`](src/neo4j/)                                   | [Neo4j](https://github.com/neo4j/neo4j-python-driver)       |

---

## ⚙️ Setup in 3 Commands

> Uses [`uv`](https://github.com/astral-sh/uv) — blazing-fast Python package manager  
> *(Don’t worry — one-liner install below)*

```bash
# 1. Install uv (if needed)
curl -Ls https://astral.sh/uv/install.sh | sh

# 2. Clone the repo
git clone https://github.com/yourusername/llm-quickstart-tutorial.git
cd llm-quickstart-tutorial

# 3. Fire up your virtual environment and install stuff
uv venv
uv pip install -e .
```

🧪 All dependencies are in pyproject.toml — no requirements.txt, no clutter.

### 🚀 Run Your First Agent

```bash
# Example: Run a basic OpenAI agent
uv run python src/openai_agents_sdkl/1_basic_agent.py
```

Each folder has a few ready-to-run scripts.
Check README.md inside the folder or just open the .py files — they come with inline guides.

---

### ❤️ Contribute or Drop a Star
Found this useful? Give it a ⭐
Have a cool integration or demo? PRs are very welcome.