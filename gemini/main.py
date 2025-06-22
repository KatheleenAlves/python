import os
import google.generativeai as genai
from dotenv import load_dotenv #lê as chaves de acesso

load_dotenv() #mêtodo que lê o arquivo .env

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY") #recebe a chave e guarda nessa constante
genai.configure(api_key=CHAVE_API_GOOGLE)

#Definindo modelo do gemini
MODELO_ESCOLHIDO = "gemini-1.5-flash" 

#Guardar o prompt do sistema
prompt_sistema = "Liste apenas o nomes dos produtos e ofereça uma breve descrição de cada um." 

#Criando um dicionário para confgiurar o modelo
configuracao_modelo = {
    "temperature": 2.0, #criatividade da resposta
    "top_p": 0.9, #equilibrio entre diversidade e relevância
    "top_k": 64, #quantas palavras o modelo pode escolher
    "max_output_tokens": 8192, 
    "response_mime_type": "text/plain" #
}

#Interando como o gemini
llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema
)

#Variável para receber a pergunta
pergunta = "Liste três produtos de moda sustentável para ir ao shopping"

#Recebendo a resposta do gemini
resposta = llm.generate_content(pergunta)

print(f"A resposta gerada para pergunta é: {resposta.text}")