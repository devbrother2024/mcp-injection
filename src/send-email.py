from fastmcp import FastMCP

mcp = FastMCP("Send Email")

@mcp.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """이메일을 보냅니다.

    """
    print(f"이메일을 보내는 중입니다: {to}, {subject}, {body}")
    return "이메일이 성공적으로 보내졌습니다."

if __name__ == "__main__":
    mcp.run(transport="stdio")
