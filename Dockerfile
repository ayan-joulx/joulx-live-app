FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Python script ke zariye app run hogi jo dynamic PORT ko handle karegi
CMD ["python", "app.py"]