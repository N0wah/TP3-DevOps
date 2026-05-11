FROM python:3.12-slim

WORKDIR /app
RUN pip install --no-cache-dir uvicorn fastapi motor mysqli-connector-python pymango

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]