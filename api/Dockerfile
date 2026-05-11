FROM python:3.12-slim
RUN pip install --no-cache-dir uvicorn fastapi motor mysql-connector-python
COPY . .
EXPOSE 8000