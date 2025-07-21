from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """_summary_
    Add two numbers
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """_summary_
    Multiply two numbers
    """
    return a * b

# The transport = "stdio" (standard input output) to recieve and respond to tool function calls in the terminal itself
if __name__ == "__main__":
    mcp.run(transport="stdio")