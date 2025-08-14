#!/usr/bin/env python3
"""
Example echo bot without using hooks
"""

import logging
import sys

from deltachat_rpc_client import DeltaChat, EventType, Rpc, SpecialContactId
from dotenv import load_dotenv
import os
import qrcode


def main():
    # logging.getLogger().setLevel(logging.DEBUG)

    with Rpc() as rpc:
        deltachat = DeltaChat(rpc)
        system_info = deltachat.get_system_info()
        logging.info("Running deltachat core %s", system_info["deltachat_core_version"])

        accounts = deltachat.get_all_accounts()
        account = accounts[0] if accounts else deltachat.add_account()

        account.set_config("bot", "1")
        if not account.is_configured():
            logging.info("Account is not configured, configuring from .env file")

            load_dotenv()

            account.set_config("addr", os.getenv("ADDR"))
            account.set_config("mail_pw", os.getenv("MAIL_PW"))
            if os.getenv("MAIL_SERVER"):
                account.set_config("mail_server", os.getenv("MAIL_SERVER"))
            if os.getenv("MAIL_PORT"):
                account.set_config("mail_port", os.getenv("MAIL_PORT"))
            if os.getenv("MAIL_SECURITY"):
                account.set_config("mail_security", os.getenv("MAIL_SECURITY"))
            if os.getenv("SEND_SERVER"):
                account.set_config("send_server", os.getenv("SEND_SERVER"))
            if os.getenv("SEND_PORT"):
                account.set_config("send_port", os.getenv("SEND_PORT"))
            if os.getenv("SEND_SECURITY"):
                account.set_config("send_security", os.getenv("SEND_SECURITY"))
            account.configure()
            logging.info("Configured")
        else:
            logging.info("Account is already configured")
            deltachat.start_io()

        def process_messages():
            for message in account.get_next_messages():
                snapshot = message.get_snapshot()
                if snapshot.from_id != SpecialContactId.SELF and not snapshot.is_bot and not snapshot.is_info:
                    snapshot.chat.send_text(snapshot.text)
                snapshot.message.mark_seen()

        def echo_qr():
            qr_code = account.get_qr_code()
            logging.info("Bot QR Code:\n%s", qr_code)
            try:
                qr = qrcode.QRCode()
                qr.add_data(qr_code)
                qr.make(fit=True)
                print("Bot QR Code:")
                qr.print_tty()
            except ImportError:
                logging.warning("Install 'qrcode' library to display QR code as image.")
                logging.info("Bot QR Code:\n%s", qr_code)

        echo_qr()

        # Process old messages.
        process_messages()

        while True:
            event = account.wait_for_event()
            if event["kind"] == EventType.INFO:
                #logging.info("%s", event["msg"])
                pass
            elif event["kind"] == EventType.INCOMING_MSG:
                logging.info("Got an incoming message")
                process_messages()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
