from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.z.ai/api/coding/paas/v4"
model_name = "glm-4.7"
key = os.getenv("ZAI_API_KEY")

llm = ChatOpenAI(
    model=model_name,
    openai_api_key=key,
    openai_api_base=base_url,
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em segurança ofensiva."),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"input": "Explique o que é SSRF em 3 linhas."})

print(response)
