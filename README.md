# 🛡️ Monad Wallet Balance Monitor

[![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue?logo=python)](https://www.python.org/)
[![Deployed on Monad Testnet](https://img.shields.io/badge/Deployed%20on-Monad%20Testnet-blue)](https://monad.xyz)
[![Status](https://img.shields.io/badge/shouldRespond-true-brightgreen)](#)

Monitor the balance of a Monad wallet (both native MON and ERC-20 tokens) and automatically send Telegram notifications whenever a new balance is detected.

## ✨ Features

- Monitor native MON and ERC-20 token balances.
- Send Telegram alerts when the balance increases.
- Automatic monitoring every 60 seconds.
- Uses `.env` file to keep sensitive data secure.

---

## ⚙️ Requirements

- Python 3.8+
- A Telegram bot
- RPC API from [Alchemy](https://www.alchemy.com/)
- Wallet and token address on the Monad network

---

## 📦 Installation

1. **Clone repository dan masuk folder:**

```bash
git clone https://github.com/KaelVNode/monitoring-42.git
cd monitoring-42
```

2. **Install dependensi**

```bash
pip install -r requirements.txt
```
3. Edit the .env file:

Ensure the .env file exists. Then fill in your credentials:
- `RPC_URL` dari Alchemy
- `TELEGRAM_BOT_TOKEN` dari @BotFather
- `TELEGRAM_CHAT_ID` dari @userinfobot
- `WALLET_ADDRESS` & `TOKEN_42_ADDRESS` di jaringan Monad

4. Start monitoring
```bash
   python3 mon.py
```
✅ Sample Terminal Output:

<img width="364" height="105" alt="image" src="https://github.com/user-attachments/assets/c16b73e2-52ef-45d9-8ea1-6a9b19508ec0" />


✅ Sample Telegram Notification

<img width="563" height="164" alt="image" src="https://github.com/user-attachments/assets/302beec8-4869-43f0-8e03-2b5a7a2c06b9" />

## ☁️ Recommended Deployment
Use tools like:

- screen

- tmux

- pm2

To keep the script running in the background.
Or configure it as a systemd service for autostart on boot.

---

## 🙏 Credits
Built with ❤️ by [KaelVNode](https://github.com/KaelVNode/)
Inspired by the need to monitor balances without relying on centralized dashboards.

---
## ⚠️ Disclaimer
This tool is provided "as is" with no warranties. Use at your own risk.
Always test on testnet before deploying to mainnet environments.

---

## MIT © 2025 [KaelVNode](https://github.com/KaelVNode)
---
