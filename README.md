# CryptoLab

Aplikasi pembelajaran enkripsi dan dekripsi untuk Mata Kuliah Kriptografi.

## Kerangka algoritma

1. Caesar Cipher — Anggota 1
2. Vigenère Cipher — Anggota 2
3. XOR Cipher — Anggota 3
4. LFSR Stream Cipher — Anggota 3
5. Super Encryption — Anggota 4

## Struktur

```text
CryptoLab/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── algorithms/
    ├── __init__.py
    ├── caesar.py
    ├── vigenere.py
    ├── xor_cipher.py
    ├── lfsr.py
    └── super_cipher.py
```

## Cara menjalankan

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Aturan kerja kelompok

Setiap anggota mengerjakan file algoritma sesuai pembagian. Jangan menghapus struktur fungsi yang sudah disediakan tanpa koordinasi dengan anggota yang mengurus integrasi.
