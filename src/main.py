from models import Backlog, TaskStatus
from tools import get_default_tools
from secretary import Secretary
from playroom import Playroom

def main():
    print("--- 🦸 AI Superhero Suit: Booting Up ---")
    
    # 1. Initialize components
    sec = Secretary()
    play = Playroom()
    tools = get_default_tools()
    
    # 2. Try to load an existing plan, or start a new one
    backlog = sec.load_work()
    if not backlog:
        print("Boss AI: No active mission found. Starting a new one!")
        backlog = Backlog(main_goal="Explore the Lab")
        backlog.add_task("Check the Toolbox")
        backlog.add_task("Build the Playroom Bubble")
        sec.save_work(backlog)
    else:
        print(f"Boss AI: Resuming mission - {backlog.main_goal}")

    # 3. Show current status
    print(f"\nStatus Report for: {backlog.main_goal}")
    for task in backlog.tasks:
        print(f"[{task.status.value.upper()}] Step #{task.id}: {task.goal}")

    print("\nBoss AI: Harness is online. Ready for orders!")

if __name__ == "__main__":
    main()
