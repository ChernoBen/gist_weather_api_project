FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install httpx

COPY test.sh .

RUN chmod +x test.sh

ENV PYTHONPATH="${PYTHONPATH}:/app/src"

ENV WEATHER_KEY=$WEATHER_KEY

ENV GITHUB_KEY=$GITHUB_KEY

ENV GIST_ID=$GIST_ID

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
