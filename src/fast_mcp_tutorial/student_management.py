from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Student Management")

# Resource: Get student info by ID
@mcp.resource("student://{student_id}") # Same as GET in FastAPI
def get_student_info(student_id: str) -> str:
    """Retrieve student information based on ID"""
    # Simulate student data
    students = {
        "001": "Peter, 15 years old, class 10A",
        "002": "Alex, 16 years old, class 11B"
    }
    return students.get(student_id, "Student not found")

# Tool: Calculate average score
@mcp.tool() # # Same as POST in FastAPI
def calculate_average_score(scores: list[float]) -> float:
    """Calculate average score from a list of scores"""
    if not scores:
        return 0.0
    return str(sum(scores) / len(scores))

# Prompt: Generate analysis template
@mcp.prompt()
def analyze_student(student_id: str, scores: list[float]) -> str:
    """Generate a prompt to analyze student info and scores"""
    return f"""
    Please analyze the student with ID {student_id}:
    - Information: {get_student_info(student_id)}
    - Average score: {calculate_average_score(scores)}
    Suggestion: Evaluate if the student meets the requirement (average score >= 5.0).
    """

if __name__ == "__main__":
    mcp.run()