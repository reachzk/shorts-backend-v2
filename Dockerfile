FROM python:3.10-slim

# Instalar dependências do sistema necessárias para MoviePy e FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Copiar arquivos
WORKDIR /app
COPY . .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
