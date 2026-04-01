from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    id: int
    goal: str
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[str] = None

@dataclass
class Backlog:
    """The Big To-Do List managed by the Boss AI."""
    main_goal: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, goal: str):
        task_id = len(self.tasks) + 1
        self.tasks.append(Task(id=task_id, goal=goal))
        print(f"Added to list: Step #{task_id} - {goal}")

if __name__ == "__main__":
    # Example of the Boss AI planning a robot game
    my_backlog = Backlog(main_goal="Build a Robot Game")
    my_backlog.add_task("Draw the robot")
    my_backlog.add_task("Make the robot jump")
    my_backlog.add_task("Add space music")
