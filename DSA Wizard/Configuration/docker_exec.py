from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import TIMEOUT, WORK_DIR

def get_docker():
    docker  = DockerCommandLineCodeExecutor(
                work_dir = WORK_DIR,
                timeout = TIMEOUT
            )
    return docker