import asyncio
from config.docker_exec import get_docker
from team.dsa_team import get_dsa_team
from config.docker_handler import start_docker_container
from config.docker_handler import stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult 

async def main():
    dsa_team, docker = get_dsa_team()

    try:
        await start_docker_container(docker)

        task = input("Enter your URL:")

        async for message in dsa_team.run_stream(task= task):
            if isinstance(message, TextMessage):
                print("==" * 50)
                print(message.source, ":", message.content)
            elif isinstance(message, TaskResult):
                print("Stop Reason: ", message.stop_reason)
    except Exception as e:
        print(f"Error: ", {e})
    finally:
        await stop_docker_container(docker)

if __name__ == "__main__":
    asyncio.run(main())
