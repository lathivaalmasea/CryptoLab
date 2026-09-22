import streamlit as st
from algorithms.caesar import caesar_encrypt, caesar_decrypt, caesar_steps
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt, vigenere_steps
from algorithms.xor_cipher import xor_encrypt, xor_decrypt, xor_steps
from algorithms.lfsr import lfsr_keystream, lfsr_xor_bytes, lfsr_steps
from algorithms.super_cipher import super_encrypt, super_decrypt

st.set_page_config(
    page_title="CryptoLab",
    page_icon="🔐",
    layout="wide"
)

st.markdown("""
<style>
    .main { background-color: #f7f9fc; }
    .block-container { padding-top: 2rem; }
    .title { font-size: 2.4rem; font-weight: 800; color: #163b70; }
    .subtitle { color: #5b677a; margin-bottom: 1.5rem; }
    .card {
        padding: 1.2rem;
        border-radius: 16px;
        background: white;
        border: 1px solid #e4e9f2;
        margin-bottom: 1rem;
    }
    .result {
        padding: 1rem;
        border-radius: 12px;
        background: #eef5ff;
        border-left: 5px solid #2878e8;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

MENU = [
    "Beranda",
    "1. Caesar Cipher",
    "2. Vigenère Cipher",
    "3. XOR Cipher",
    "4. LFSR Stream Cipher",
    "5. Super Encryption",
]

choice = st.sidebar.selectbox("Menu", MENU)

st.sidebar.markdown("---")
st.sidebar.caption("CryptoLab — Proyek Mata Kuliah Kriptografi")

if choice == "Beranda":
    st.markdown('<div class="title">CryptoLab</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Aplikasi pembelajaran enkripsi dan dekripsi '
        'berbasis algoritma kriptografi klasik dan modern.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    cards = [
        ("1", "Caesar", "Klasik"),
        ("2", "Vigenère", "Klasik"),
        ("3", "XOR", "Modern"),
        ("4", "LFSR", "Modern"),
        ("5", "Super", "4 Algoritma"),
    ]
    for col, (num, name, typ) in zip([c1,c2,c3,c4,c5], cards):
        with col:
            st.markdown(
                f'<div class="card"><h3>{num}. {name}</h3><p>{typ}</p></div>',
                unsafe_allow_html=True
            )

    st.info(
        "Versi awal ini sudah menyediakan kerangka 5 menu. "
        "Setiap menu dirancang agar proses enkripsi/dekripsi dapat ditampilkan, "
        "bukan hanya hasil akhirnya."
    )

elif choice == "1. Caesar Cipher":
    st.header("1. Caesar Cipher")
    st.caption("Kriptografi klasik — substitusi dengan pergeseran k posisi.")

    process = st.radio("Pilih proses", ["Enkripsi", "Dekripsi"], horizontal=True)
    text = st.text_area("Masukkan teks", "BELAJAR KRIPTOGRAFI")
    key = st.number_input("Kunci (k)", min_value=0, max_value=25, value=3, step=1)

    if st.button("Proses", type="primary"):
        result = caesar_encrypt(text, key) if process == "Enkripsi" else caesar_decrypt(text, key)
        st.markdown(f'<div class="result">Hasil: {result}</div>', unsafe_allow_html=True)

        st.subheader("Langkah-langkah proses")
        st.dataframe(caesar_steps(text, key, process), use_container_width=True)

        st.latex(
            r"C = (P+k)\bmod 26"
            if process == "Enkripsi"
            else r"P = (C-k)\bmod 26"
        )

elif choice == "2. Vigenère Cipher":
    st.header("2. Vigenère Cipher")
    st.caption("Kriptografi klasik — menggunakan kunci yang berulang secara periodik.")

    process = st.radio("Pilih proses", ["Enkripsi", "Dekripsi"], horizontal=True)
    text = st.text_area("Masukkan teks", "THIS PLAINTEXT")
    key = st.text_input("Kunci", "SONY")

    if st.button("Proses", type="primary"):
        if not key.strip():
            st.error("Kunci tidak boleh kosong.")
        else:
            result = vigenere_encrypt(text, key) if process == "Enkripsi" else vigenere_decrypt(text, key)
            st.markdown(f'<div class="result">Hasil: {result}</div>', unsafe_allow_html=True)
            st.subheader("Langkah-langkah proses")
            st.dataframe(vigenere_steps(text, key, process), use_container_width=True)
            st.latex(
                r"C_i=(P_i+K_i)\bmod 26"
                if process == "Enkripsi"
                else r"P_i=(C_i-K_i)\bmod 26"
            )

elif choice == "3. XOR Cipher":
    st.header("3. XOR Cipher")
    st.caption("Kriptografi modern berbasis operasi XOR pada data biner.")

    process = st.radio("Pilih proses", ["Enkripsi", "Dekripsi"], horizontal=True)
    text = st.text_input("Masukkan teks", "A")
    key = st.number_input("Kunci (0–255)", min_value=0, max_value=255, value=5, step=1)

    if st.button("Proses", type="primary"):
        result = xor_encrypt(text, key) if process == "Enkripsi" else xor_decrypt(text, key)
        st.markdown(f'<div class="result">Hasil: {result}</div>', unsafe_allow_html=True)

        st.subheader("Representasi biner dan proses XOR")
        st.dataframe(xor_steps(text, key, process), use_container_width=True)
        st.latex(r"C=P\oplus K" if process == "Enkripsi" else r"P=C\oplus K")

elif choice == "4. LFSR Stream Cipher":
    st.header("4. LFSR Stream Cipher")
    st.caption("Stream cipher dengan LFSR sebagai pembangkit keystream.")

    process = st.radio("Pilih proses", ["Enkripsi", "Dekripsi"], horizontal=True)
    text = st.text_input("Masukkan teks", "HELLO")
    seed = st.text_input("Seed awal (4-bit)", "1111")

    if st.button("Proses", type="primary"):
        try:
            if len(seed) != 4 or any(ch not in "01" for ch in seed):
                raise ValueError("Seed harus tepat 4 bit, contoh: 1111.")

            result = lfsr_xor_bytes(text.encode("utf-8"), seed).decode("utf-8", errors="replace")
            keystream = lfsr_keystream(len(text.encode("utf-8")), seed)

            st.markdown(f'<div class="result">Hasil: {result}</div>', unsafe_allow_html=True)
            st.write("Keystream (bit):", keystream)
            st.subheader("Proses LFSR")
            st.dataframe(lfsr_steps(seed, len(text.encode("utf-8"))), use_container_width=True)
            st.info(
                "Implementasi awal menggunakan LFSR 4-bit dengan feedback "
                "berdasarkan XOR bit pertama dan bit terakhir, mengikuti contoh pada materi."
            )
        except Exception as e:
            st.error(str(e))

elif choice == "5. Super Encryption":
    st.header("5. Super Encryption")
    st.caption("Gabungan empat algoritma: Caesar → Vigenère → XOR → LFSR.")

    process = st.radio("Pilih proses", ["Enkripsi", "Dekripsi"], horizontal=True)
    text = st.text_area("Masukkan teks", "RAHASIA")

    c1, c2, c3 = st.columns(3)
    with c1:
        caesar_key = st.number_input("Kunci Caesar", 0, 25, 3)
    with c2:
        vigenere_key = st.text_input("Kunci Vigenère", "DATA")
    with c3:
        xor_key = st.number_input("Kunci XOR", 0, 255, 5)

    seed = st.text_input("Seed LFSR (4-bit)", "1111")

    if st.button("Proses Super Encryption", type="primary"):
        try:
            if not vigenere_key.strip():
                raise ValueError("Kunci Vigenère tidak boleh kosong.")
            if len(seed) != 4 or any(ch not in "01" for ch in seed):
                raise ValueError("Seed LFSR harus tepat 4 bit.")

            if process == "Enkripsi":
                final, stages = super_encrypt(text, caesar_key, vigenere_key, xor_key, seed)
            else:
                final, stages = super_decrypt(text, caesar_key, vigenere_key, xor_key, seed)

            st.subheader("Tahapan proses")
            for i, (name, value) in enumerate(stages, start=1):
                st.write(f"**{i}. {name}**")
                st.code(value)

            st.markdown(f'<div class="result">Hasil akhir: {final}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(str(e))
