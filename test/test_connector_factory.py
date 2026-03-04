from ems_protocol.connectors import OpenAIConnector, get_connector, XAIConnector, GeminiConnector, AnthropicConnector


def test_openai():
    connector = get_connector("openai")
    assert isinstance(connector, OpenAIConnector)

def test_xai():
    connector = get_connector("xai")
    assert isinstance(connector, XAIConnector)

def test_gemini():
    connector = get_connector("gemini")
    assert isinstance(connector, GeminiConnector)

def test_anthropic():
    connector = get_connector("anthropic")
    assert isinstance(connector, AnthropicConnector)