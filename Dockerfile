# 간단한 Flask 앱 예시
FROM python:3.9-slim

WORKDIR /app
COPY app.py .

RUN pip install flask

CMD ["python", "app.py"]

