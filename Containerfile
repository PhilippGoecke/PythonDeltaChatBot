FROM python:3.11-slim

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN useradd -ms /bin/bash deltachat \
  && mkdir -p /home/deltachat/bot \
  && chown deltachat:deltachat -R /home/deltachat
WORKDIR /home/deltachat/bot

COPY .botenv .env
COPY deltachatbot.py .

USER deltachat:deltachat

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir --user deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

RUN pwd && ls -lisah

CMD ["python", "deltachatbot.py"]
