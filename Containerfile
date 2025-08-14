FROM python:3.11-slim

RUN useradd -ms /bin/bash deltabot
WORKDIR /home/deltabot

COPY .botenv .env
COPY deltachatbot.py .

USER deltabot:deltabot

RUN pip install deltachat_rpc_client deltachat-rpc-server dotenv qrcode 

CMD ["python", "deltachatbot.py"]
