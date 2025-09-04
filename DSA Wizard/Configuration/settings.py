import os
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL1, FAMILY1, MODEL2, FAMILY2

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_KEY2 = os.getenv('OPENAI_API_KEY2')

def get_model_client():
    open_router_model_client = OpenAIChatCompletionClient(
        base_url ="https://openrouter.ai/api/v1",
        model = MODEL1,
        api_key = OPENAI_API_KEY,
        model_info = {
            "family": FAMILY1,
            "vision": True,
            "function_calling": True,
            "json_output": False,
            "structured_output": True,
            },
        )

    return open_router_model_client


def get_model_client_2():
    open_router_model_client2 = OpenAIChatCompletionClient(
        base_url = "https://openrouter.ai/api/v1",
        model = MODEL2,
        api_key = OPENAI_API_KEY2,
        model_info ={
            "family": FAMILY2,
            "vision": True,
            "function_calling": True,
            "json_output": False,
            "structured_output":True
            },
        )

    return open_router_model_client2