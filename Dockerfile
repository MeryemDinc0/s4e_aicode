FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ollama
COPY templates /app/
COPY app.py /app/
COPY your_model.py /app/
COPY . /app/
CMD ["python", "app.py"]
