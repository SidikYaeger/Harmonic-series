import streamlit as st
import sys
from io import StringIO
from contextlib import redirect_stdout
import time
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Harmonic Series", layout="centered")

st.title("🧮 Kalkulator Deret Harmonik: Iteratif VS Rekursif")
st.write("Menghitung jumlah deret: 1/1 + 1/2 + ... + 1/n")


def rekursif(n):
    if n == 1:
        print("1/1", end="")
        return 1.0
    x = rekursif(n - 1)
    print(" + 1/" + str(n), end="")
    return x + (1.0 / n)

def iteratif(n):
    total = 0.0
    for i in range(1, n + 1):
        print("1/" + str(i), end="")
        if i < n:
            print(" + ", end="")
        total = total + (1.0 / i)
    return total

def total(n):
    total = 0.0
    for i in range(1, n + 1):
        total = total + (1.0 / i)
    return total

n = st.number_input("Masukkan nilai n:", min_value=1, step=1, value=5)

if st.button("Hitung Hasil", type="primary"):
    
    waktu_iteratif = 0
    waktu_rekursif = None

    st.subheader("1. Metode Iteratif")
    
    buffer_iter = StringIO()
    
    start_iter = time.perf_counter()
    with redirect_stdout(buffer_iter):
        res_iter = iteratif(n)
    end_iter = time.perf_counter()
    
    waktu_iteratif = 1000 * (end_iter - start_iter)
    teks_iter = buffer_iter.getvalue()

    st.caption("Proses Penjumlahan:")
    st.code(teks_iter, language="text")
    st.success(f"Hasil: {res_iter}")

    st.subheader("2. Metode Rekursif")

    if n > 992:
        st.warning("⚠️ Nilai n terlalu besar untuk metode Rekursif (batas aman Python untuk aplikasi ini <= 992).")
    else:
        buffer_rec = StringIO()

        start_rec = time.perf_counter()
        with redirect_stdout(buffer_rec):
            res_rec = rekursif(n)
        end_rec = time.perf_counter()

        waktu_rekursif = 1000 * (end_rec - start_rec)
        teks_rec = buffer_rec.getvalue()

        st.caption("Proses Penjumlahan:")
        st.code(teks_rec, language="text")
        st.success(f"Hasil: {res_rec}")

    st.divider()
    st.subheader("⏱️ Perbandingan Waktu Eksekusi")
    
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Waktu Iteratif", value=f"{waktu_iteratif:.4f} ms")
    
    with col2:
        if waktu_rekursif is not None:
            st.metric(label="Waktu Rekursif", value=f"{waktu_rekursif:.4f} ms", delta=f"{waktu_iteratif - waktu_rekursif:.4f} ms")
        else:
            st.metric(label="Waktu Rekursif", value="Tidak dijalankan")

    st.write("### Visualisasi Grafik")
    
    kategori = ['Iteratif', 'Rekursif']
    
    nilai_rekursif_safe = waktu_rekursif if waktu_rekursif is not None else 0
    waktu = [waktu_iteratif, nilai_rekursif_safe]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    
    bars = ax.bar(kategori, waktu, color=['#3498db', '#e74c3c'])
    
    ax.set_ylabel('Waktu (milisekon)')
    ax.set_title('Perbandingan Kecepatan Eksekusi')
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.4f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

    st.pyplot(fig)

    if waktu_rekursif is not None:
        if waktu_iteratif < waktu_rekursif:
            st.info("ℹ️ Kesimpulan: Metode **Iteratif** lebih cepat.")
        else:
            st.info("ℹ️ Kesimpulan: Metode **Rekursif** lebih cepat.")
    
    st.caption("*Catatan: Waktu mencakup proses pembuatan string (I/O) dan kalkulasi.*")

    #aaaaaaaaaaaaaaaaaaaaaaaaaaa
    footer="""<style>
    a:link , a:visited{
    color: blue;
    background-color: transparent;
    text-decoration: underline;
    }

    a:hover,  a:active {
    color: red;
    background-color: transparent;
    text-decoration: underline;
    }

    .footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    }
    </style>
    ceritanya ini footer eak
    
    ~Made by Ravananda & Zhafir~
    jangan lupa mampir ke https://github.com/SidikYaeger

    """
    st.markdown(footer,unsafe_allow_html=True)
