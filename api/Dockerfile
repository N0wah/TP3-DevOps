FROM python:3.12-slim
RUN pip install --no-cache-dir uvicorn fastapi motor mysqli-connector-python pymango
COPY . .
EXPOSE 8000