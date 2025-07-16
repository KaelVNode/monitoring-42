# 🛡️ Monad Wallet Balance Monitor

Monitor saldo wallet Monad (native MON & token ERC-20) dan kirim notifikasi otomatis ke Telegram setiap kali ada penambahan saldo.

---

## ✨ Fitur

- Memantau saldo native MON dan token ERC-20.
- Kirim notifikasi Telegram saat saldo bertambah.
- Monitoring otomatis tiap 60 detik.
- Menggunakan `.env` untuk keamanan variabel sensitif.

---

## ⚙️ Persyaratan

- Python 3.8+
- Bot Telegram
- API RPC dari [Alchemy](https://www.alchemy.com/)
- Wallet dan token address di jaringan Monad

---

## 📦 Instalasi

1. **Clone repository dan masuk folder:**

```bash
git clone https://github.com/KaelVNode/monitoring-42.git
cd monitoring-42
```

2. **Install dependensi**

```bash
pip install -r requirements.txt
```
