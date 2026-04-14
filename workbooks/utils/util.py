
import os
from enum import Enum

from openai import OpenAI

class LLM(Enum):
    ANTROPIC = "ANTHROPIC"
    OPENAI = "OPENAI"
    GEMINI = "GEMINI"
    OPENROUTER = "OPENROUTER"
    OLLAMA = "OLLAMA"


def get_llm(llm_name:str):
    match llm_name:
        case LLM.ANTROPIC:
            return OpenAI(api_key=os.getenv("ANTHROPIC_API_KEY"), base_url="https://api.anthropic.com/v1/")
        case LLM.OPENAI:
            return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        case LLM.GEMINI:
            return OpenAI(api_key=os.getenv("GOOGLE_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
        case LLM.OPENROUTER:
            return OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1")
        case LLM.OLLAMA:
            return OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
        case _:
            raise ValueError(f"Unsupported LLM: {llm_name}")
        
def message_updater(messages:list, role: str):
    system_message = messages[0]
    rest_messages = messages[1:]
    for i in range(0, len(rest_messages), 2):
        rest_messages[i]["role"] = role
    for i in range(1, len(rest_messages), 2):
        rest_messages[i]["role"] = "assistant" if role == "user" else "user"

    return [system_message] + rest_messages
