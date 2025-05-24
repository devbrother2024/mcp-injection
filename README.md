# MCP 모의 해킹 실습

## Prerequisites

- Python 3.13+
- Anthropic Claude Desktop app (or Cursor)
- UV (Python package manager), install with `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Steps

### 해당 Repository를 클론합니다.

```bash
git clone https://github.com/devbrother2024/mcp-injection.git
cd mcp-injection
```

### uv sync

```bash
uv sync
```

### mcp.json 파일 설정

```json
{
    "mcpServers": {
        "calculator": {
            "command": "{{PATH_TO_UV}}", // `which uv` 명령어로 해당 경로를 출력한 후 입력하세요.
            "args": [
                "--directory",
                "{{PATH_TO_SRC}}/src", // cd 명령어로 해당 repo 루트 경로로 들어가고, `pwd` 명령어로 현재 경로를 출력한 후 해당 경로를 입력하세요.
                "run",
                "direct-poisoning.py"
            ]
        }
    }
}
```
