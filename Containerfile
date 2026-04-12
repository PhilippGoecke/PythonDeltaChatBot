FROM python:3.14-slim-trixie

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN useradd --create-home --shell /bin/bash deltachat

RUN chown deltachat:deltachat -R /home/deltachat

VOLUME /home/deltachat/data

WORKDIR /home/deltachat/bot

COPY --chown=deltachat:deltachat .botenv .env
COPY --chown=deltachat:deltachat deltachatbot.py .

USER deltachat:deltachat

ENV PATH=/home/deltachat/.local/bin:$PATH

RUN pip install deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

CMD ["python", "deltachatbot.py"]
