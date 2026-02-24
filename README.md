# LangChain Study - Zhipu AI (GLM) Integration

Este repositório é um projeto de estudo baseado no [LangChain Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart), adaptado para utilizar os modelos **GLM** da Zhipu AI através da plataforma Z.ai.

## Configuração da Licença e Modelos

Este projeto utiliza o plano **Z.ai Coding Lite**, que fornece acesso a modelos otimizados para codificação e raciocínio.

### Modelos Suportados
Os testes foram validados com os seguintes modelos:
- `glm-4.7` (Recomendado)
- `glm-4.6`
- `glm-4.5`
- `glm-4.5-Air`

### Como Configurar

Para rodar este projeto localmente, siga estes passos:

1. **Clonar o repositório**:
   ```bash
   git clone <url-do-seu-repo>
   cd langchain-study
   ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as Variáveis de Ambiente**:
   Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API da Z.ai:
   ```text
   ZAI_API_KEY=sua_chave_aqui
   ```
   *Nota: O arquivo `.env` está no `.gitignore` e não deve ser enviado para o GitHub.*

4. **Executar os Testes**:
   - `test_zhipu.py`: Verifica a conectividade básica com o endpoint de Coding da Z.ai.
   - `test_langchain_glm.py`: Valida uma Chain completa do LangChain (Prompt + LLM + Output Parser) usando o modelo GLM.

## Estrutura Técnica
Para ser compatível com o plano **Coding Lite**, os scripts utilizam a interface `ChatOpenAI` configurada com o endpoint específico:
- **Base URL**: `https://api.z.ai/api/coding/paas/v4`
