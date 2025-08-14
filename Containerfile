FROM python:3.11-slim

RUN useradd -ms /bin/bash deltachat
WORKDIR /home/deltachat/bot

COPY .botenv .env
COPY deltachatbot.py .

USER deltachat:deltachat

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir --user deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

CMD ["python", "deltachatbot.py"]
