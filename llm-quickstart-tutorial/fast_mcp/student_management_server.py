from fastmcp import FastMCP, Context

# Create MCP server
mcp = FastMCP("Student Management")

# Resource: Get student info by ID
@mcp.resource("student://{student_id}")
def get_student_info(student_id: str) -> str:
    """Retrieve student information based on ID"""
    students = {
        "001": "Peter, 15 years old, class A",
        "002": "Alex, 16 years old, class B"
    }
    return students.get(student_id, "Student not found")

# Tool: Calculate average score
@mcp.tool()
def calculate_average_score(scores: list[float]) -> float:
    """Calculate average score from a list of scores"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# Tool: Analyze student with `Context`
@mcp.tool()
def analyze_with_context(ctx: Context, student_id: str, scores: list[float]) -> str:
    """Analyze student using Context to access resources and logging"""
    
    # 1. Logging
    ctx.log_info(f"Analyzing student {student_id}")
    
    # 2. Access Resource
    student_info = ctx.read_resource(f"student://{student_id}")
    
    # 3. Calculate
    avg_score = sum(scores) / len(scores) if scores else 0
    
    # 4. More logging
    ctx.log_info(f"Average calculated: {avg_score}")
    
    # 5. Return result
    return f"""
Student Analysis:
- Info: {student_info}
- Average Score: {avg_score:.2f}
- Status: {'PASS' if avg_score >= 5.0 else 'FAIL'}
"""

# Prompt: Generate analysis template
@mcp.prompt()
def analyze_student(student_id: str, scores: list[float]) -> str:
    """Generate a prompt to analyze student info and scores"""
    return f"""
Please analyze the student with ID {student_id}:
- Use analyze_with_context tool with scores: {scores}
- Provide detailed feedback and suggestions
"""

if __name__ == "__main__":
    mcp.run()