import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carregar variáveis do arquivo .env
load_dotenv()

def test_zhipu():
    # Endpoints e Modelos para o Plano Z.ai Coding Lite
    # O endpoint DEVE ser o de coding para usar a assinatura do plano
    base_url = "https://api.z.ai/api/coding/paas/v4"
    models = ["glm-4.7", "glm-4.6", "glm-4.5", "glm-4.5-Air"]
    key = os.getenv("ZAI_API_KEY")
    
    if not key:
        print("❌ ERRO: ZAI_API_KEY não encontrada no arquivo .env")
        return
    
    print(f"--- Iniciando teste com Plano Z.ai Coding Lite ---")
    print(f"Endpoint: {base_url}\n")

    for model_name in models:
        try:
            print(f"--- Tentando modelo: {model_name} ---")
            # Usamos ChatOpenAI por ser mais flexível com base_url customizada
            llm = ChatOpenAI(
                model=model_name,
                openai_api_key=key,
                openai_api_base=base_url,
                temperature=0.7,
            )
            
            print(f"Enviando requisição via Z.ai Coding API...")
            response = llm.invoke("Responda apenas 'OK' se estiver funcionando via Z.ai.")
            
            print(f"✅ SUCESSO com {model_name}!")
            print(f"Resposta: {response.content}")
            return
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                print(f"❌ Erro 429 no modelo {model_name}. Pode ser limite de frequência do plano Lite.")
            else:
                print(f"❌ Erro com {model_name}: {error_msg}")
            
            if model_name != models[-1]:
                print("Tentando o próximo modelo...\n")
    
    print("\n--- Resultado Final ---")
    print("Não foi possível conectar aos modelos usando o endpoint de Coding.")
    print("Dica: Verifique se sua chave da Z.ai está ativa e se o endpoint está correto para o seu plano.")

if __name__ == "__main__":
    test_zhipu()
