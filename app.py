import streamlit as st

st.set_page_config(
    page_title="CryptoLab",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CRYPTOLAB - UI SKELETON
# ============================================================
# This file contains the shared UI only.
# Algorithm implementation will be added by each member.
# ============================================================

st.markdown("""
<style>
    /* ---------- Global ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    html,
    body,
    .stApp,
    [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp,
    .stApp *,
    .stApp input,
    .stApp textarea,
    .stApp button,
    .stApp label,
    .stApp p,
    .stApp span,
    .stApp div {
        font-family: 'Poppins', sans-serif !important;
    }
                
    .stApp {
        background: #f3f8ff;
    }

    [data-testid="stHeader"] {
        background: rgba(255,255,255,0.0);
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }
            
    div[data-testid="stVerticalBlock"] {
        gap: 0.5rem;
    }
            
    /* =========================================================
    FORM SPACING
    ========================================================= */

    div[data-testid="stTextInput"] {
        margin-bottom: 6px;
    }

    div[data-testid="stRadio"] {
        margin-bottom: 4px;
    }

    div.stButton {
        margin-top: 6px;
    }


    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e2d55 0%, #173f73 100%);
    }

    section[data-testid="stSidebar"] * {
        font-family: 'Poppins', sans-serif;
    }

    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] .stCaption {
        color: white;
    }
            
    .side-brand {
        padding: 10px 6px 18px 6px;
    }

    .side-brand-title {
        font-size: 22px;
        font-weight: 800;
        line-height: 1.2;
        margin: 0;
    }

    .side-brand-subtitle {
        font-size: 9px;
        font-weight: 500;
        letter-spacing: 1.2px;
        opacity: .7;
        margin-top: 4px;
    }

    .side-line {
        height: 1px;
        background: rgba(255,255,255,.18);
        margin: 16px 0;
    }

    /* ---------- Hero ---------- */
    .hero {
        background: linear-gradient(135deg, #ffffff 0%, #edf6ff 100%);
        border: 1px solid #d9e8f7;
        border-radius: 20px;
        padding: 30px 32px;
        box-shadow: 0 8px 28px rgba(28, 77, 125, .07);
        margin-bottom: 24px;
    }

    .hero-kicker {
        color: #2878d4;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }

    .hero-title {
        color: #12366a;
        font-size: 38px;
        line-height: 1.15;
        font-weight: 800;
        margin: 0 0 10px 0;
    }

    .hero-title span {
        color: #1677e8;
    }

    .hero-text {
        color: #5a6b80;
        font-size: 14px;
        line-height: 1.6;
        max-width: 720px;
        margin: 0;
    }

    .quote-box {
        margin-top: 16px;
        padding: 10px 14px;
        background: #fff1f5;
        border-left: 4px solid #ef5272;
        border-radius: 10px;
        color: #8b4050;
        font-size: 12px;
        height: 1.5;
    }

    /* ---------- Cards ---------- */
    .algo-card {
        min-height: 142px;
        border-radius: 17px;
        padding: 18px;
        border: 1px solid #dfeaf5;
        box-shadow: 0 6px 18px rgba(25, 69, 110, .06);
        background: white;
    }

    .algo-number {
        font-size: 12px;
        font-weight: 800;
        color: #60748b;
    }

    .algo-name {
        font-size: 17px;
        font-weight: 800;
        color: #173b6c;
        margin-top: 12px;
    }

    .algo-type {
        font-size: 11px;
        color: #708198;
        margin-top: 4px;
    }

    .card-caesar { background: linear-gradient(145deg,#fff0f3,#fffafa); }
    .card-vigenere { background: linear-gradient(145deg,#fff8e7,#fffdf6); }
    .card-xor { background: linear-gradient(145deg,#eafaf5,#f8fffc); }
    .card-lfsr { background: linear-gradient(145deg,#f1edff,#fcfaff); }
    .card-super { background: linear-gradient(145deg,#edf4ff,#fafdff); }

    /* ---------- Section ---------- */
    .section-title {
        color: #163a6b;
        font-size: 20px;
        font-weight: 800;
        margin: 8px 0 10px;
    }

    .info-card {
        background: white;
        border: 1px solid #dfeaf5;
        border-radius: 16px;
        padding: 18px;
        min-height: 105px;
        box-shadow: 0 5px 18px rgba(25, 69, 110, .05);
    }

    .info-title {
        color: #214b80;
        font-weight: 800;
        font-size: 14px;
    }

    .info-text {
        color: #6b7d92;
        font-size: 12px;
        margin-top: 6px;
        line-height: 1.45;
    }

    /* ---------- Algorithm page ---------- */
    .page-header {
        background: white;
        border: 1px solid #dfeaf5;
        border-radius: 18px;
        padding: 18px 22px;
        box-shadow: 0 5px 18px rgba(25,69,110,.05);
        margin-bottom: 16px;
    }

    .page-title {
        color: #153a6d;
        font-size: 27px;
        font-weight: 850;
        margin: 0;
    }

    .page-subtitle {
        color: #718197;
        font-size: 12px;
        margin-top: 4px;
    }

    .formula {
        background: #fff1f5;
        border: 1px solid #f3d6df;
        border-radius: 12px;
        padding: 12px 15px;
        color: #8b3e4d;
        font-family: 'Poppins', sans-serif !important;
        font-size: 12px;
        line-height: 1.6;
        margin-bottom: 16px;
    }

    /* =========================================================
    STREAMLIT CONTAINERS
    ========================================================= */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff;
        border: 1px solid #dfe6ef;
        border-radius: 16px;
        padding: 4px;
        box-shadow: 0 5px 18px rgba(25, 69, 110, 0.05);
        margin-bottom: 16px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]
    > div {
        border: none !important;
    }

    .panel-title {
        color: #184477;
        font-size: 16px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .result-box {
        background: #edf9f3;
        border: 1px solid #cdeedf;
        border-radius: 14px;
        padding: 16px;
        color: #236a4a;
        font-family: 'Poppins', sans-serif !important;
        min-height: 65px;
    }

    .placeholder {
        background: #f8fbff;
        border: 1px dashed #aac4df;
        border-radius: 12px;
        padding: 18px;
        color: #708198;
        text-align: center;
        font-size: 13px;
    }

    .note {
        background: #fff9df;
        border: 1px solid #f4e4a5;
        border-radius: 12px;
        padding: 12px 14px;
        color: #77621c;
        font-size: 12px;
    }

    /* Streamlit controls */
    div.stButton > button {
        border-radius: 10px;
        font-weight: 750;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)


def sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="side-brand">
            <div class="side-brand-title">🔐 CryptoLab</div>
            <div class="side-brand-subtitle">KRIPTOGRAFI EXPLORER</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Menu")

        menu = st.radio(
            "Navigasi",
            [
                "Beranda",
                "1. Caesar Cipher",
                "2. Vigenère Cipher",
                "3. XOR Cipher",
                "4. LFSR Stream Cipher",
                "5. Super Encryption",
                "Tentang Aplikasi",
                "Kelompok",
            ],
            label_visibility="collapsed",
        )

        st.markdown('<div class="side-line"></div>', unsafe_allow_html=True)
        st.caption("CryptoLab — Proyek Mata Kuliah Kriptografi")

    return menu


def algorithm_header(title, subtitle, formula):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-title">{title}</div>
        <div class="page-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="formula"><b>Rumus:</b><br>{formula}</div>',
                unsafe_allow_html=True)


def process_skeleton(title, input_label="Masukkan Teks", key_label="Kunci"):
    left, right = st.columns([1.05, 1.35], gap="large")

    # ========================================================
    # KOLOM KIRI
    # ========================================================
    with left:

        # ---------- INPUT ----------
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Input</div>',
                unsafe_allow_html=True
            )

            mode = st.radio(
                "Pilih Proses",
                ["Enkripsi", "Dekripsi"],
                horizontal=True,
                key=f"{title}_mode"
            )

            text = st.text_input(
                input_label,
                key=f"{title}_text"
            )

            key = st.text_input(
                key_label,
                key=f"{title}_key"
            )

            st.button(
                "🔒 Proses",
                type="primary",
                use_container_width=True,
                key=f"{title}_button"
            )

        # ---------- HASIL ----------
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Hasil</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="placeholder">'
                'Hasil algoritma akan ditampilkan oleh anggota '
                'yang mengerjakan modul ini.'
                '</div>',
                unsafe_allow_html=True
            )

    # ========================================================
    # KOLOM KANAN
    # ========================================================
    with right:

        # ---------- LANGKAH PROSES ----------
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Langkah-langkah Proses</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="placeholder">'
                'Tabel/detail proses algoritma akan diisi oleh '
                'anggota yang bertanggung jawab.'
                '</div>',
                unsafe_allow_html=True
            )

        # ---------- CATATAN ----------
        st.markdown(
            '<div class="note">'
            '💡 Area ini disediakan untuk penjelasan proses, '
            'rumus, representasi karakter/biner, atau tahapan algoritma.'
            '</div>',
            unsafe_allow_html=True
        )

    return mode, text, key


# ============================================================
# PAGES
# ============================================================

menu = sidebar()

if menu == "Beranda":
    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">KRIPTOGRAFI EXPLORER</div>
        <div class="hero-title">Selamat Datang di <span>CryptoLab</span></div>
        <div class="hero-text">
            Aplikasi Enkripsi dan Dekripsi dengan 4 Algoritma Kriptografi
            dan Super Encryption.
        </div>
        <div class="quote-box">
            "Keamanan informasi dimulai dari pemahaman, bukan sekadar teknologi."
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Algoritma</div>', unsafe_allow_html=True)

    cards = [
        ("1", "Caesar Cipher", "Klasik", "card-caesar"),
        ("2", "Vigenère Cipher", "Klasik", "card-vigenere"),
        ("3", "XOR Cipher", "Modern", "card-xor"),
        ("4", "LFSR Stream Cipher", "Modern", "card-lfsr"),
        ("5", "Super Encryption", "Gabungan 4 Algoritma", "card-super"),
    ]

    cols = st.columns(5)
    for col, (num, name, typ, cls) in zip(cols, cards):
        with col:
            st.markdown(f"""
            <div class="algo-card {cls}">
                <div class="algo-number">{num}</div>
                <div class="algo-name">{name}</div>
                <div class="algo-type">{typ}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(3)
    info = [
        ("🖱️ Mudah Digunakan", "Antarmuka sederhana dan interaktif."),
        ("⚙️ Proses Algoritma", "Menampilkan langkah-langkah enkripsi dan dekripsi."),
        ("📖 Belajar Kriptografi", "Disiapkan untuk mendukung pembelajaran materi kuliah."),
    ]

    for col, (title, desc) in zip(cols, info):
        with col:
            st.markdown(f"""
            <div class="info-card">
                <div class="info-title">{title}</div>
                <div class="info-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

elif menu == "1. Caesar Cipher":
    algorithm_header(
        "1. Caesar Cipher (Klasik)",
        "Kerangka modul Caesar Cipher. Implementasi akan dikerjakan Anggota 1.",
        "Enkripsi : C = (P + k) mod 26<br>Dekripsi : P = (C - k) mod 26"
    )
    process_skeleton("caesar", key_label="Kunci (k)")

elif menu == "2. Vigenère Cipher":
    algorithm_header(
        "2. Vigenère Cipher (Klasik)",
        "Kerangka modul Vigenère Cipher. Implementasi akan dikerjakan Anggota 2.",
        "Enkripsi : Cᵢ = (Pᵢ + Kᵢ) mod 26<br>Dekripsi : Pᵢ = (Cᵢ - Kᵢ) mod 26"
    )
    process_skeleton("vigenere", key_label="Kunci")

elif menu == "3. XOR Cipher":
    algorithm_header(
        "3. XOR Cipher (Modern)",
        "Kerangka modul XOR Cipher. Implementasi akan dikerjakan Anggota 3.",
        "Enkripsi : C = P ⊕ K<br>Dekripsi : P = C ⊕ K"
    )
    process_skeleton("xor", key_label="Kunci XOR")

elif menu == "4. LFSR Stream Cipher":
    algorithm_header(
        "4. LFSR Stream Cipher (Modern)",
        "Kerangka modul LFSR Stream Cipher. Implementasi akan dikerjakan Anggota 3.",
        "Keystream dibangkitkan oleh LFSR kemudian digunakan pada operasi XOR."
    )
    process_skeleton("lfsr", key_label="Seed Awal (biner)")

elif menu == "5. Super Encryption":
    algorithm_header(
        "5. Super Encryption (Gabungan 4 Algoritma)",
        "Kerangka integrasi empat algoritma. Implementasi akan dikerjakan Anggota 4.",
        "Caesar → Vigenère → XOR → LFSR"
    )

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Input & Parameter Kunci</div>',
                unsafe_allow_html=True)

    left, right = st.columns([1.3, 1])

    with left:
        st.radio("Pilih Proses", ["Enkripsi", "Dekripsi"], horizontal=True)
        st.text_input("Masukkan Teks", key="super_text")

    with right:
        st.text_input("Kunci Caesar (k)", key="super_caesar")
        st.text_input("Kunci Vigenère", key="super_vigenere")
        st.text_input("Kunci XOR", key="super_xor")
        st.text_input("Seed LFSR (biner)", key="super_lfsr")

    st.button("🔒 Proses Super Encryption", type="primary",
              use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    left, right = st.columns([1.25, 1])

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-title">Tahapan Proses</div>',
                    unsafe_allow_html=True)
        st.markdown("""
        <div class="placeholder">
            <b>1.</b> Caesar Cipher<br><br>
            <b>2.</b> Vigenère Cipher<br><br>
            <b>3.</b> XOR Cipher<br><br>
            <b>4.</b> LFSR Stream Cipher
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-title">Hasil Akhir</div>',
                    unsafe_allow_html=True)
        st.markdown(
            '<div class="placeholder">Hasil Super Encryption akan diisi Anggota 4.</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Tentang Aplikasi":
    st.header("Tentang Aplikasi")
    st.info("Halaman informasi aplikasi — dapat dikembangkan setelah struktur kelompok disepakati.")

elif menu == "Kelompok":
    st.header("Kelompok")
    st.info("Daftar anggota dan pembagian tugas akan ditambahkan bersama anggota kelompok.")
