FROM python:3.11-slim

WORKDIR /app

# Instala o NiceGUI diretamente
RUN pip install --no-cache-dir nicegui

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
