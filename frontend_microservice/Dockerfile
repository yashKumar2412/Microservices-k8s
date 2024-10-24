
# Frontend Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY templates ./templates
COPY static ./static
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY frontend_app.py .

CMD ["python", "frontend_app.py"]
