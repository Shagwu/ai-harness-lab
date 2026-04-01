import json
import os
from typing import List, Dict, Any, Optional
from models import Backlog, Task, TaskStatus

class Secretary:
    """The Notebook that remembers what the AI did."""
    def __init__(self, storage_path: str = "memory.json"):
        self.storage_path = storage_path

    def save_work(self, backlog: Backlog):
        data = {
            "main_goal": backlog.main_goal,
            "tasks": [
                {"id": t.id, "goal": t.goal, "status": t.status.value, "result": t.result}
                for t in backlog.tasks
            ]
        }
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Secretary: I've saved everything in {self.storage_path}!")

    def load_work(self) -> Optional[Backlog]:
        if not os.path.exists(self.storage_path):
            return None
        with open(self.storage_path, "r") as f:
            data = json.load(f)
        
        backlog = Backlog(main_goal=data["main_goal"])
        for t_data in data["tasks"]:
            task = Task(
                id=t_data["id"],
                goal=t_data["goal"],
                status=TaskStatus(t_data["status"]),
                result=t_data["result"]
            )
            backlog.tasks.append(task)
        return backlog

    def write_to_vault(self, title: str, content: str):
        vault_path = "/Users/shagwu/Documents/MySecondBrain"
        file_path = os.path.join(vault_path, f"{title}.md")
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Secretary: I've archived a new note in your vault: {title}.md")

if __name__ == "__main__":
    sec = Secretary()
    # Test saving a plan
    test_list = Backlog(main_goal="Mission to Mars")
    test_list.add_task("Build rocket")
    sec.save_work(test_list)
