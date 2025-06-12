# ⚡ LLM Quickstart Tutorial

A plug-and-play collection of quickstart tutorials for popular LLM tools and agent frameworks.  
**No fluff. Just code. Get in, get it running, and start building cool stuff.**

---

## 😎 Choose Your Weapon

| Name               | Folder                                       | What's it about?                                         |
|--------------------|----------------------------------------------|----------------------------------------------------------|
| OpenAI Agents SDK  | [`src/openai_agents_sdk/`](src/openai_agents_sdk/) | OpenAI’s new SDK to spin up and wire agents easily       |
| Mem0               | [`src/mem0/`](src/mem0/)                         | A memory-first agent framework for local workflows       |
| Fast MCP           | [`src/fast_mcp/`](src/fast_mcp/)                 | Minimal controller to manage and scale LLM agents fast   |
| Neo4j              | [`src/neo4j/`](src/neo4j/)                       | Hook agents into graphs — Neo4j style                    |

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