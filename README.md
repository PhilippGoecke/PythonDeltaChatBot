# PythonDeltaChatBot 🤖
Python DeltaChat Bot

A simple echo bot for the [Delta Chat](https://delta.chat/) messenger 💬, built with Python 🐍. This project is based on the official [py.delta.chat JSON-RPC examples](https://py.delta.chat/jsonrpc/examples.html#echo-bot).

## ✅ Prerequisites

- A dedicated email account for your bot to use with Delta Chat.

## 🚀 Getting Started

### 1. Setup Environment 📁

First, create and activate a Python virtual environment.

```shell
python3 -m venv .
source bin/activate
```

### 2. Install Dependencies 📦

Install the required Python packages using pip.

```shell
pip install deltachat_rpc_client deltachat-rpc-server dotenv qrcode
```

### 3. Configuration ⚙️

This bot uses a `.env`/`.botenv` file for configuration. Create a file named `.env`/`.botenv` in the root directory and add your bot's email address and password.

```env
# .env/.botenv file
ADDR=bot@example.org
MAIL_PW=your-app-password
```

### 4. Run the Bot ▶️

Execute the main script to start the bot. A QR code will be displayed in the terminal for you to add the bot.

```shell
python3 deltachatbot.py
```

## 🐳 Running with Podman

Alternatively, you can run the bot in a container using the provided Podman script. Make sure your `.botenv` file is configured as described above.

```shell
bash podman-run-bot.bash
```
