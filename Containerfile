FROM python:3.14-slim-trixie

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y

RUN useradd --create-home --shell /bin/bash deltachat

RUN chown deltachat:deltachat -R /home/deltachat

VOLUME /home/deltachat/data

WORKDIR /home/deltachat/bot

RUN cp -rv /home/deltachat/data/* /home/deltachat/bot/ || true \
  && chown deltachat:deltachat -R /home/deltachat

COPY --chown=deltachat:deltachat .botenv .env
COPY --chown=deltachat:deltachat deltachatbot.py .

USER deltachat:deltachat

ENV PATH=/home/deltachat/.local/bin:$PATH

RUN python --version \
  && pip install deltachat_rpc_client deltachat-rpc-server dotenv qrcode

CMD ["sh", "-c", "python deltachatbot.py & while [ ! -f accounts/accounts.toml ]; do sleep 1; done; sleep 42; cp -r /home/deltachat/bot/* /home/deltachat/data/ && echo 'Account saved!' && sleep infinity"]
