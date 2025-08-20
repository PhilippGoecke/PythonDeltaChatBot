#!/usr/bin/env python3
"""Advanced echo bot example.
it will echo back any message that has non-empty text and also supports the /help command.
"""

import logging
import sys
from threading import Thread

from deltachat_rpc_client import Bot, DeltaChat, EventType, Rpc, events
from dotenv import load_dotenv
import os

hooks = events.HookCollection()

@hooks.on(events.RawEvent)
def log_event(event):
    if event.kind == EventType.INFO:
        logging.info(event.msg)
    elif event.kind == EventType.WARNING:
        logging.warning(event.msg)

@hooks.on(events.RawEvent(EventType.ERROR))
def log_error(event):
    logging.error(event.msg)

@hooks.on(events.MemberListChanged)
def on_memberlist_changed(event):
    logging.info("member %s was %s", event.member, "added" if event.member_added else "removed")

@hooks.on(events.GroupImageChanged)
def on_group_image_changed(event):
    logging.info("group image %s", "deleted" if event.image_deleted else "changed")

@hooks.on(events.GroupNameChanged)
def on_group_name_changed(event):
    logging.info("group name changed, old name: %s", event.old_name)

@hooks.on(events.NewMessage(func=lambda e: not e.command))
def echo(event):
    snapshot = event.message_snapshot
    if snapshot.text or snapshot.file:
        snapshot.chat.send_message(text=snapshot.text, file=snapshot.file)

@hooks.on(events.NewMessage(command="/help"))
def help_command(event):
    snapshot = event.message_snapshot
    snapshot.chat.send_text("Send me any message and I will echo it back")

def main():
    with Rpc() as rpc:
        deltachat = DeltaChat(rpc)
        system_info = deltachat.get_system_info()
        logging.info("Running deltachat core %s", system_info.deltachat_core_version)

        accounts = deltachat.get_all_accounts()
        account = accounts[0] if accounts else deltachat.add_account()

        bot = Bot(account, hooks)
        if not bot.is_configured():
            logging.info("Account is not configured, configuring from .env file")

            load_dotenv()

            kwargs = {
                "email": os.getenv("ADDR"),
                "password": os.getenv("MAIL_PW"),
                "mail_server": os.getenv("MAIL_SERVER"),
                "mail_port": os.getenv("MAIL_PORT"),
                "mail_security": os.getenv("MAIL_SECURITY"),
                "send_server": os.getenv("SEND_SERVER"),
                "send_port": os.getenv("SEND_PORT"),
                "send_security": os.getenv("SEND_SECURITY"),
            }
            # Filter out keys where the value is None
            kwargs = {k: v for k, v in kwargs.items() if v is not None}

            configure_thread = Thread(run=bot.configure, kwargs=kwargs)
            configure_thread.start()
        bot.run_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
