FROM python:3.11-slim

RUN useradd -ms /bin/bash deltabot
WORKDIR /home/deltabot

COPY .botenv .env
COPY deltachatbot.py .

USER deltabot:deltabot

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

CMD ["python", "deltachatbot.py"]
