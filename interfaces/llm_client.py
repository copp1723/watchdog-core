"""
Interface for LLM client operations.
"""

from typing import Protocol
import os

class LLMClient(Protocol):
    """
    Interface for interacting with an LLM.
    In production, this will call OpenAI via LlamaIndex.
    """

    def ask(self, prompt: str) -> str:
        if os.getenv("LLM_DISABLED") == "true":
            raise RuntimeError("LLM calls disabled due to budget cap")
        raise NotImplementedError("LLM call not implemented yet.")

