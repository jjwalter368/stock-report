FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir yfinance
COPY ./src ./src


CMD ["python3", "src/main.py" ]
