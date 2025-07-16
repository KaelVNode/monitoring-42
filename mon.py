#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import asyncio
import time
from decimal import Decimal
from telegram import Bot
from telegram.constants import ParseMode
from dotenv import load_dotenv

# === Load .env file ===
load_dotenv()

# === KONFIGURASI ===
RPC_URL = os.getenv("RPC_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS").lower()
TOKEN_42_ADDRESS = os.getenv("TOKEN_42_ADDRESS").lower()
NATIVE_SYMBOL = os.getenv("NATIVE_SYMBOL", "MON")
EXPLORER_URL = f"https://testnet.monadexplorer.com/address/{WALLET_ADDRESS}?tab=Token"

bot = Bot(token=TELEGRAM_BOT_TOKEN)
last_balance_42 = Decimal('0.0')
last_balance_mon = Decimal('0.0')


def get_erc20_balance(token_address, wallet_address):
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [
            {
                "to": token_address,
                "data": f"0x70a08231000000000000000000000000{wallet_address[2:]}"
            },
            "latest"
        ]
    }
    try:
        resp = requests.post(RPC_URL, json=data)
        resp.raise_for_status()
        result = resp.json().get('result')
        if result:
            return Decimal(int(result, 16)) / Decimal('1e18')
    except Exception as e:
        print("❌ Gagal ambil balance token 42:", e)
    return Decimal('0.0')


def get_native_balance(wallet_address):
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    try:
        resp = requests.post(RPC_URL, json=data)
        resp.raise_for_status()
        result = resp.json().get('result')
        if result:
            return Decimal(int(result, 16)) / Decimal('1e18')
    except Exception as e:
        print("❌ Gagal ambil balance MON:", e)
    return Decimal('0.0')


async def monitor():
    global last_balance_42, last_balance_mon
    print("🔄 Inisialisasi saldo awal...")

    last_balance_42 = get_erc20_balance(TOKEN_42_ADDRESS, WALLET_ADDRESS)
    last_balance_mon = get_native_balance(WALLET_ADDRESS)

    print(f"🟡 Saldo awal 42: {last_balance_42:,.4f}")
    print(f"🟢 Saldo awal {NATIVE_SYMBOL}: {last_balance_mon:,.4f}")

    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=(
            f"📡 <b>Monitoring dimulai</b>\n\n"
            f"- <b>Wallet:</b> <code>{WALLET_ADDRESS[:6]}...{WALLET_ADDRESS[-4:]}</code>\n"
            f"- <b>Saldo awal 42:</b> <code>{last_balance_42:,.4f}</code>\n"
            f"- <b>Saldo awal {NATIVE_SYMBOL}:</b> <code>{last_balance_mon:,.4f}</code>\n\n"
            f"- <a href=\"{EXPLORER_URL}\">Lihat di Explorer</a>\n"
            f"- <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>"
        ),
        parse_mode=ParseMode.HTML
    )

    print("✅ Monitoring aktif... (interval 60 detik)")

    while True:
        try:
            balance_42 = get_erc20_balance(TOKEN_42_ADDRESS, WALLET_ADDRESS)
            balance_mon = get_native_balance(WALLET_ADDRESS)

            notify = False
            msg = ""

            if balance_42 > last_balance_42:
                diff_42 = balance_42 - last_balance_42
                notify = True
                msg += f"- <b>Balance 42:</b> <code>{balance_42:,.4f}</code> (+{diff_42:,.4f})\n"
                last_balance_42 = balance_42

            if balance_mon > last_balance_mon:
                diff_mon = balance_mon - last_balance_mon
                notify = True
                msg += f"- <b>Balance {NATIVE_SYMBOL}:</b> <code>{balance_mon:,.4f}</code> (+{diff_mon:,.4f})\n"
                last_balance_mon = balance_mon

            if notify:
                short_wallet = WALLET_ADDRESS[:6] + "..." + WALLET_ADDRESS[-4:]
                text = (
                    f"<b>💰 Penambahan Saldo Terdeteksi!</b>\n\n"
                    f"- <b>Wallet:</b> <code>{short_wallet}</code>\n"
                    f"{msg}\n"
                    f"- <a href=\"{EXPLORER_URL}\">Lihat di Explorer</a>\n"
                    f"- <code>{time.strftime('%Y-%m-%d %H:%M:%S')}</code>"
                )
                await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text, parse_mode=ParseMode.HTML)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ Notifikasi dikirim.")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] ⏳ Tidak ada perubahan saldo.")

        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] ❌ Error: {e}")

        await asyncio.sleep(60)


if __name__ == '__main__':
    asyncio.run(monitor())
