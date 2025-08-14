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

ENV PATH=/home/deltachat/.local/bin:$PATH

RUN pip install deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

CMD ["python", "deltachatbot.py"]
