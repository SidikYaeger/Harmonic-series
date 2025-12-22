# 🧮 Harmonic Series Calculator (Iteratif vs Rekursif)

Aplikasi web berbasis **Streamlit** untuk menghitung dan membandingkan **deret harmonik** menggunakan dua pendekatan algoritmik:
- **Iteratif**
- **Rekursif**

Aplikasi ini juga menampilkan **waktu eksekusi** dari masing-masing metode serta **visualisasi grafik** perbandingannya.

🔗 **Live Demo**:  
https://harmonicseries.streamlit.app/

---

## 📌 Deskripsi Singkat

Deret harmonik merupakan deret matematika dengan bentuk:

1/1 + 1/2 +...+1/n

Pada aplikasi ini, perhitungan dilakukan menggunakan:
- **Metode Iteratif** (menggunakan perulangan)
- **Metode Rekursif** (menggunakan pemanggilan fungsi berulang)

Tujuan utama aplikasi adalah:
- Memahami perbedaan pendekatan algoritma
- Membandingkan performa (waktu eksekusi)
- Memberikan visualisasi hasil secara interaktif

---

## ✨ Fitur Utama

- Input nilai `n` secara interaktif
- Menampilkan proses penjumlahan deret
- Perhitungan menggunakan metode:
  - Iteratif
  - Rekursif (dengan batas aman rekursi)
- Perbandingan waktu eksekusi (ms)
- Visualisasi grafik (Matplotlib)
- Antarmuka sederhana

---

## 🛠️ Teknologi yang Digunakan

- **Python 3**
- **Streamlit**
- **Matplotlib**
- **Time & Contextlib**
- **StringIO**

---

## 📂 Struktur Program

```text
.
├── streamlit_app.py   # File utama aplikasi Streamlit
├── requirements.txt   # Dependensi Python
└── README.md          # Dokumentasi proyek
