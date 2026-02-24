import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carregar variáveis do arquivo .env
load_dotenv()

def test_langchain_glm():
    # Configurações para o Plano Z.ai Coding Lite
    base_url = "https://api.z.ai/api/coding/paas/v4"
    model_name = "glm-4.7"
    key = os.getenv("ZAI_API_KEY")
    
    print(f"--- Testando LangChain + GLM ({model_name}) ---")
    
    # 1. Inicializar o Modelo
    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=key,
        openai_api_base=base_url,
        temperature=0.7,
    )
    
    # 2. Criar um Prompt Template
    prompt = ChatPromptTemplate.from_template("Dê uma explicação curta e criativa sobre o que é {topico}.")
    
    # 3. Criar uma Chain simples usando LCEL (LangChain Expression Language)
    chain = prompt | llm | StrOutputParser()
    
    # 4. Executar
    try:
        print("Executando chain...")
        result = chain.invoke({"topico": "LangChain"})
        print(f"\n✅ Resultado do LangChain:\n{result}")
    except Exception as e:
        print(f"❌ Erro ao executar LangChain: {e}")

if __name__ == "__main__":
    test_langchain_glm()
