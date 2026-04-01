from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Tool:
    name: str
    description: str
    parameters: Dict[str, Any]

def get_default_tools() -> List[Tool]:
    """Returns the basic robots for our AI Suit."""
    return [
        Tool(
            name="read_file",
            description="Allows the AI to see what is inside a file.",
            parameters={"path": "string"}
        ),
        Tool(
            name="run_command",
            description="Allows the AI to run a command inside the safe bubble.",
            parameters={"command": "string"}
        ),
        Tool(
            name="write_file",
            description="Allows the AI to write new information to a file.",
            parameters={"path": "string", "content": "string"}
        ),
        Tool(
            name="gemini_research",
            description="Uses Gemini CLI to research a topic and provide a detailed summary.",
            parameters={"topic": "string"}
        )
    ]

if __name__ == "__main__":
    tools = get_default_tools()
    for tool in tools:
        print(f"Robot ready: {tool.name} - {tool.description}")
