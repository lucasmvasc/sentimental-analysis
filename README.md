# Sentimental Analysis

Este repositório contém um programa que realiza a transcrição de áudio MP3 para texto usando a biblioteca da OpenAI: Whisper[^1] e, em seguida, realiza a análise de sentimentos usando o modelo pré treinado provido pela nlptown: bert-base-multilingual-uncased-sentiment[^2].
Tudo isso conectado por meio do NgRok, que provém a possibilidade de tornar essa URL pública.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas necessárias em um virtual env (instaláveis via `pip install -r requirements.txt`)
- Instalar o NgRok e criar uma conta: [Link aqui](https://ngrok.com/download)
- Anaconda Prompt (para criação de virtual envs): [Link aqui](https://www.anaconda.com/download)

## Configuração do projeto
Caso queira executá-lo em sua máquina

1. Execute o seguinte comando para ativar o Ngrok - túnel de comunicação:
```bash
ngrok http 5000
```

1. Configure o seu arquivo secrets.JSON na root com as variáveis API_KEY e API_URL:
```json
{
    "API_KEY": "SUA_CHAVE_AQUI"
}
```

3. Em um terminal separado, execute agora o código main.py
- Esse passo tem de ser feito dentro de um ambiente virtual com todas as bibliotecas necessárias instaladas

## Uso
Transcrição de Áudio para Texto

Execute o seguinte comando para transcrever um arquivo de áudio MP3 para texto e obter sua análise de sentimentos em formato de dicionário:
```bash
curl -X POST \
  -H "Api-Key: $API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@$AUDIO_FILE" \
  $API_URL
```
Esquema de variáveis:<br>
API_URL="SUA_URL_OBTIDA_NO_NGROK" <br>
API_KEY="SUA_CHAVE_AQUI" <br>
AUDIO_FILE="DIRETÓRIO/DO/SEU/AUDIO.mp3"
PS: A API_URL está no test.py

## Passo a passo da execução no código: 
1. O texto é transcrito via whisper e salvo em um arquivo JSON dividido com cada segmento da conversação.

2. O modelo pré-treinado é configurado em formato de pipeline, para assim poder receber uma lista de segmentos/partes da conversa.

3. Para cada uma das partes dessa conversa, é inferido seu respectivo sentimento entre valores inteiros de 1 até 5 (no qual foram convertidos para: Positivo, Ligeiramente Positivo, Neutro, Ligeiramente Negativo e Negativo).

4. É retornado um dicionário com cada um dos segmentos de conversa e seu respectivo sentimento.

## Referências
[^1]: [Modelo Whisper da OpenAI](https://openai.com/research/whisper)
[^2]: [Modelo bert-base-multilingual-uncased-sentiment da NplTown](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)

