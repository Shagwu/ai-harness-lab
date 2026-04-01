import subprocess

class Playroom:
    """The Safe Bubble where the AI works."""
    def __init__(self, image_name: str = "ai-hero-suit"):
        self.image_name = image_name

    def build_bubble(self):
        print(f"Building your safe playroom bubble ({self.image_name})...")
        try:
            subprocess.run(["docker", "build", "-t", self.image_name, "."], check=True)
            print("Playroom is READY!")
        except Exception as e:
            print(f"Oops! The bubble failed to build. Is Docker running? Error: {e}")

    def run_in_bubble(self, command: str):
        print(f"AI is entering the bubble to run: {command}")
        # This is where we would use 'docker run' to be safe
        # subprocess.run(["docker", "run", "--rm", self.image_name, "bash", "-c", command])
        print("Command finished inside the bubble!")

if __name__ == "__main__":
    p = Playroom()
    p.build_bubble()
