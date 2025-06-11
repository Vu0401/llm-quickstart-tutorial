# 🚀 LLM Quickstart Tutorial

A curated collection of quickstart tutorials and hands-on examples for popular LLM repositories and agent frameworks. This project helps you dive in quickly without wading through long documentation.

---

## 📁 Directory Structure

```bash
src/
├── openai_agents_sdkl/   # Quickstart for OpenAI Agents SDK (local-based)
├── mem0/                 # Quickstart for the mem0 agent framework
├── fast_mcp/             # Quickstart for the fast_mcp controller
```

---

## Tutorials Overview
| Name               | Folder                | Description                                             |
| ------------------ | --------------------- | ------------------------------------------------------- |
| OpenAI Agents SDKL | `openai_agents_sdkl/` | Run and customize agents with OpenAI's experimental SDK |
| Mem0               | `mem0/`               | Agent framework with memory modules and local flow      |
| Fast MCP           | `fast_mcp/`           | Lightweight agent controller for fast deployment        |

---

## 🛠️ Getting Started

### 1. Install dependencies with uv

```bash
# Install uv if you haven't already
curl -Ls https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/yourusername/llm-quickstart-tutorial.git
cd llm-quickstart-tutorial

# Create a virtual environment and install dependencies
uv venv
uv pip install -e .
```

All dependencies are managed via pyproject.toml. No requirements.txt needed.

### 2. Run a Quickstart Example

```bash
# Example: Run a basic OpenAI agent
uv run python src/openai_agents_sdkl/1_basic_agent.py
```
Each module may contain multiple example scripts. Check the subfolder README.md or script headers for details.