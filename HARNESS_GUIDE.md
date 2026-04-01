# 🦸‍♂️ AI Harness Lab: The Superhero Suit for AI Agents

Welcome to the **AI Harness Lab**. This project is a study in **Harness Engineering**—the art of building the "nervous system" that connects smart AI brains to the real world safely and effectively.

## 🚀 What is AI Harness Lab?

Think of a standard AI as a genius who is stuck in a room with no doors. They are incredibly smart, but they can't actually *do* anything on your computer.

The **AI Harness** is like a **high-tech superhero suit**. When the AI "puts on the suit," it suddenly gains:
1.  **Hands:** Tools to read, write, and run code.
2.  **A Bubble:** A safe space (Docker) to work so it doesn't break your computer.
3.  **A Memory:** A notebook (Secretary) so it never forgets its plan.
4.  **A Brain Structure:** A way to break huge goals into small, easy steps.

---

## 🏗️ How it Works (The 4 Pillars)

| Component | Role | What it does |
| :--- | :--- | :--- |
| **The Boss (Orchestrator)** | The Brain | Takes your big goal (e.g., "Build a game") and breaks it into a **Backlog** of tiny tasks. |
| **The Secretary (Context)** | The Memory | Saves every step to `memory.json`. If you turn off the computer, the AI remembers where it left off. |
| **The Toolbox (Tools)** | The Hands | Contains "Robot Blueprints" for tasks like `read_file`, `write_file`, and `gemini_research`. |
| **The Playroom (Docker)** | The Safety | Creates an isolated "bubble" where the AI runs its commands. No mess ever leaks out to your Mac. |

---

## 🤖 Specialized Workers: The Gemini Researcher

Our harness includes a **Specialized Gemini Worker**. 
-   **Deep Research:** Unlike standard agents, this worker is specifically wired to use the **Gemini CLI**.
-   **Isolation:** It runs entirely inside the Docker bubble, meaning it can fetch information and summarize it without cluttering your host environment.

---

## 🛠️ The "Tech Lead" Lifecycle

The AI Harness Lab enforces a professional engineering workflow:
1.  **Decompose:** Break the mission into small pieces.
2.  **Route:** Pick the best tool or specialized worker for the job.
3.  **Execute:** Run the work inside the safe Docker bubble.
4.  **Review:** Check if the work was successful before moving to the next task.

---

## 🌟 Why this matters

Harness Engineering is the bridge between "Chatting with AI" and "Working with AI." By isolating the execution and organizing the tasks, we transform an LLM into a reliable autonomous engineer.

---

*Built with ❤️ in the AI Harness Lab.*
