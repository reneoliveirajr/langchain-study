import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

base_url = "https://api.z.ai/api/coding/paas/v4"
model_name = "glm-4.7"
key = os.getenv("ZAI_API_KEY")

llm = ChatOpenAI(
    model=model_name,
    openai_api_key=key,
    openai_api_base=base_url,
    temperature=0.7,
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# Imprimir o resultado de forma legível
for m in result['messages']:
    m.pretty_print()