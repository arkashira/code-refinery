from core.agent import CodeAgent

def main():
    agent = CodeAgent(model_id="test-model")
    tasks = ["task1", "task2", "task3"]
    agent.run_loop(tasks)

if __name__ == "__main__":
    main()