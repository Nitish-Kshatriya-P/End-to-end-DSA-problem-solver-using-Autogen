from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_exec import get_docker

docker = get_docker()

def get_code_executor_agent():

    codexecutor_agent = CodeExecutorAgent(
                name = 'Code_Executor_Agent',
                code_executor = docker
            )
    return codexecutor_agent, docker