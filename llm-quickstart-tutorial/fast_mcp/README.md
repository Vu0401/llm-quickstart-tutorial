# FastMCP

FastMCP is the fast, Pythonic framework for building Model Context Protocol (MCP) servers and clients — the new standard for connecting LLMs to external tools, data, and logic.

It transforms how language models interact with the world, enabling structured, secure, and extensible execution of tools, access to resources, and prompt-driven workflows. With clean Python code and minimal boilerplate, FastMCP empowers developers to turn simple functions into powerful AI capabilities.

## 🚀 Core Concepts

A high-level toolkit to build intelligent, interactive LLM backends — modular, scalable, and built for real-world usage.

| Component    | Function                                                    | Think of it as...           |
| ------------ | ----------------------------------------------------------- | --------------------------- |
| 🧠 **Tools** | Execute code via LLMs                                       | POST endpoints for actions  |
| 📡 **Resources** | Expose structured data to LLMs                         | GET endpoints for facts     |
| 📝 **Prompts** | Define reusable LLM interaction templates                 | Prompt libraries            |
| 🧭 **Context** | Access runtime state (logging, HTTP, LLM calls)          | Request/session context     |
| 🔁 **Clients** | Connect to MCP servers programmatically                   | SDK for MCP integration     |

FastMCP is built around composable building blocks that help LLMs perform tasks, retrieve data, and interact intelligently.

---

### 🧠 Tools

**Execute Python functions through LLMs**

```python
@mcp.tool()
def calculate_average(scores: list[float]) -> float:
   """Calculate average from scores"""
   return sum(scores) / len(scores)
```

- Auto-generates schemas from type hints
- Perfect for: calculations, API calls, data processing

---

### 📡 Resources

**Expose structured data sources**

```python
@mcp.resource("student://{student_id}")
def get_student(student_id: str) -> str:
    """Get student information by ID"""
    return students_db.get(student_id)
```

- Supports dynamic URIs with templates
- Perfect for: user profiles, configs, documentation

---

### 📝 Prompts

**Reusable interaction templates**

```python
@mcp.prompt()
def analyze_performance(student_id: str, scores: list[float]) -> str:
    """Generate analysis prompt for student performance"""
    return f"Analyze student {student_id} with scores {scores}..."
```

- Standardize common LLM interactions
- Perfect for: summaries, rewrites, structured queries

---

### 🧭 Context

**Access runtime session state**

```python
@mcp.tool()
def advanced_analysis(ctx: Context, data: dict) -> str:
    ctx.log_info("Starting analysis...")           # Logging
    user_data = ctx.read_resource("user://123")    # Access resources
    return analysis_result
```

- Enables: logging, HTTP requests, internal tool calls
- Perfect for: multi-step workflows, complex reasoning chains

---

### 🔁 Clients

**Connect to MCP servers programmatically**

```python
async with MCPServerStdio(params={"command": "python", "args": ["server.py"]}) as server:
    agent = Agent(mcp_servers=[server])
    result = await Runner.run(agent, "Calculate average of [1, 2, 3]")
```

- Multiple transports: stdin, HTTP, in-memory
- Perfect for: testing, integration, tool chaining

---

## What’s Inside?

| File/Module             | Core Concept         | What It Demonstrates                                          |
| ----------------------- | -------------------- | ------------------------------------------------------------- |
| `student_management_server.py` | 🧠 Tools, Resources, ... | Core MCP tools (score calculation, analysis) and student data |
| `main.py`               | 🔁 Client Usage      | How an LLM agent interacts with MCP via Gemini + MCP Server   |

---

## 🧪 How It Works

1. Run the student_management MCP server locally using:

```bash
uv run python src/fast_mcp_tutorial/student_management_server.py
```

2. Launch main.py to connect the agent and test LLM-driven tool calls.

```bash
python main.py
```

3. Watch the magic: Gemini automatically calls MCP tools like `calculate_average_score`.

---

## 🤔 Want to go deeper?

Curious how it all works under the hood?
> 🔍 Dive deeper with the [full official docs here](https://github.com/jlowin/fastmcp).
