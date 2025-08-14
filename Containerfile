FROM python:3.11-slim

RUN useradd -ms /bin/bash deltachat
WORKDIR /home/deltachat/bot

COPY .botenv .env
COPY deltachatbot.py .

USER deltachat:deltachat

RUN python -m venv . \
  && source bin/activate \
  && pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

RUN pwd && ls -lisah

CMD ["python", "deltachatbot.py"]
