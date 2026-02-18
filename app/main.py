# app/main.py

from app.agent_router import EntertainmentAgent

def run():

    agent = EntertainmentAgent()

    while True:
        query = input("\nAsk something (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        result = agent.handle_query(query)

        print("\nIntent Detected:", result["intent"])
        print("\nResponse:\n", result["response"])


if __name__ == "__main__":
    run()
