"""Connector Factory."""

import ems_protocol.connectors.core
from ems_protocol.connectors.chatgpt import OpenAIConnector
from ems_protocol.connectors.gemini import GeminiConnector
from ems_protocol.connectors.anthropic import AnthropicConnector
from ems_protocol.connectors.xai import XAIConnector


def get_connector(platform: str) -> core.Connector:
    if platform.upper() == "OPENAI":
        return OpenAIConnector()
    elif platform.upper() == "XAI":
        return XAIConnector()
    elif platform.upper() == "GEMINI":
        return GeminiConnector()
    elif platform.upper() == "ANTHROPIC":
        return AnthropicConnector()
    else:
        raise ValueError(f"Unsupported platform: {platform}")
