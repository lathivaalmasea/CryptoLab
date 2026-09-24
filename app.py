import streamlit as st
import os
from algorithms import caesar, lfsr

###. LOGO CRYPTOLAB
def get_logo_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "assets", "cryptolab_logo.png")

###. SIDEBAR CRYPTOLAB

def pilih_menu(menu):
    st.session_state["nav_menu"] = menu

def sidebar():
    with st.sidebar:

        # LOGO
        logo_path = get_logo_path()

        if os.path.exists(logo_path):
            st.image(logo_path, width=52)
        else:
            st.warning(
                "Logo tidak ditemukan. "
                "Pastikan file ada di assets/cryptolab_logo.png"
            )

        # BRAND
        st.markdown(
            """
            <div class="side-brand-title">CryptoLab</div>
            <div class="side-brand-subtitle">
                KRIPTOGRAFI EXPLORER
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Menu")

        # DAFTAR MENU
        menu_list = [
            "Beranda",
            "1. Caesar Cipher",
            "2. Vigenère Cipher",
            "3. XOR Cipher",
            "4. LFSR Stream Cipher",
            "5. Super Encryption",
            "Tentang Aplikasi",
            "Kelompok",
        ]

        # MENU DEFAULT
        if "nav_menu" not in st.session_state:
            st.session_state["nav_menu"] = "Beranda"

        # TOMBOL MENU
        for menu_item in menu_list:

            is_active = (
                st.session_state["nav_menu"] == menu_item
            )

            st.button(
                menu_item,
                key=f"nav_{menu_item}",
                type="primary" if is_active else "secondary",
                use_container_width=True,
                on_click=pilih_menu,
                args=(menu_item,)
            )

        st.markdown(
            '<div class="side-line"></div>',
            unsafe_allow_html=True
        )

    return st.session_state["nav_menu"]

###. UI SKELETON - CRYPTOLAB
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

/* COLOR PALETTE */

:root {
    --main-bg: #F2E3D3;
    --colombia-blue: #D2E8FF;
    --green: #26422A;
    --brown: #5D372A;
    --brown-hover: #704634;
    --white: #FFFFFF;
    --border: rgba(93, 55, 42, 0.18);
    --shadow: rgba(93, 55, 42, 0.08);
}

/* GLOBAL */

html,
body,
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

/* =========================================================
   FIX IKON PANAH SIDEBAR STREAMLIT
   ========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0');

/* Ikon pada tombol buka/tutup sidebar */
[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"],
[data-testid="stSidebarCollapsedControl"] [data-testid="stIconMaterial"],
[data-testid="stSidebarNavCollapseIcon"],
[data-testid="stIconMaterial"] {
    font-family: "Material Symbols Rounded" !important;
    font-weight: 400 !important;
    font-style: normal !important;
    font-size: 24px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    direction: ltr !important;
    font-feature-settings: "liga" !important;
    -webkit-font-feature-settings: "liga" !important;
}

/* Background Utama */
.stApp {
    background: var(--main-bg);
    color: var(--green);
}

/* Header Streamlit */
[data-testid="stHeader"] {
    background: transparent;
}

/* Area utama */
.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Jarak antar komponen */
div[data-testid="stVerticalBlock"] {
    gap: 1rem;
}


/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: var(--colombia-blue);
}

/* Semua teks sidebar */
section[data-testid="stSidebar"] * {
    font-family: 'Poppins', sans-serif !important;
    color: var(--green);
}

/* Brand */
.side-brand {
    padding: 8px 4px 18px 4px;
    text-align: left;
}

/* Logo */
.side-logo {
    width: 52px;
    height: 52px;
    object-fit: contain;
    margin-bottom: 8px;
}

/* Nama aplikasi */
.side-brand-title {
    color: var(--green);
    font-size: 23px;
    font-weight: 800;
    line-height: 1.2;
    margin: 0;
}

/* Subtitle */
.side-brand-subtitle {
    color: var(--green);
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 1.2px;
    opacity: .75;
    margin-top: 4px;
}

/* Judul Menu */
section[data-testid="stSidebar"] h3 {
    color: var(--green) !important;
    font-weight: 800;
}


/* =========================================================
   SIDEBAR MENU - TAMPILAN PUSH BUTTON
   ========================================================= */

/* Jarak antar tombol menu */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 10px !important;
}

/* Tampilan tombol menu yang tidak aktif */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    min-height: 44px !important;
    padding: 10px 14px !important;
    box-sizing: border-box !important;

    background: #F5FAFF !important;
    border: 1px solid rgba(38, 66, 42, 0.15) !important;
    border-radius: 10px !important;

    color: var(--green) !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

/* Hilangkan lingkaran radio agar terlihat seperti tombol */
section[data-testid="stSidebar"] div[role="radiogroup"] label [data-baseweb="radio"] {
    display: none !important;
}

/* Tombol saat diarahkan kursor */
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #E8F2E8 !important;
    border-color: var(--green) !important;
}

/* Tombol menu yang sedang aktif */
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: #E5F0E3 !important;
    border: 1.5px solid var(--green) !important;
    color: var(--green) !important;
    font-weight: 700 !important;
    box-shadow: inset 4px 0 0 var(--green) !important;
}

/* Pastikan teks menu tetap terlihat */
section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: var(--green) !important;
    margin: 0 !important;
    font-size: 14px !important;
}

/* Garis sidebar */
.side-line {
    height: 1px;
    background: rgba(93,55,42,.25);
    margin: 18px 0;
}

/* Caption */
section[data-testid="stSidebar"] .stCaption {
    color: var(--green) !important;
    opacity: .75;
}


/* HERO */
.hero {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-radius: 24px;
    padding: 32px 34px;
    box-shadow: 0 8px 25px rgba(93,55,42,.08);
    margin-bottom: 28px;
}

.hero-kicker {
    color: var(--green);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.hero-title {
    color: var(--green);
    font-size: 38px;
    line-height: 1.15;
    font-weight: 800;
    margin: 0 0 10px 0;
}

.hero-title span {
    color: var(--green);
}

.hero-text {
    color: var(--green);
    font-size: 14px;
    line-height: 1.6;
    max-width: 720px;
    margin: 0;
}

.quote-box {
    margin-top: 18px;
    padding: 11px 15px;
    background: var(--main-bg);
    border-left: 4px solid var(--green);
    border-radius: 10px;
    color: var(--green);
    font-size: 12px;
    line-height: 1.5;
}


/* SECTION TITLE */
.section-title {
    color: var(--green);
    font-size: 21px;
    font-weight: 800;
    margin: 8px 0 12px;
}


/* ALGORITHM CARDS */
.algo-card {
    min-height: 145px;
    border-radius: 18px;
    padding: 18px;
    border: 1px solid var(--green-soft);
    box-shadow: 0 6px 18px rgba(93,55,42,.06);
    background: var(--white);
}

.algo-number {
    font-size: 12px;
    font-weight: 800;
    color: var(--green);
}

.algo-name {
    font-size: 17px;
    font-weight: 800;
    color: var(--green);
    margin-top: 12px;
}


.algo-type {
    font-size: 11px;
    color: var(--green);
    opacity: .7;
    margin-top: 5px;
}


.card-caesar,
.card-vigenere,
.card-xor,
.card-lfsr,
.card-super {
    background: var(--white);
}


/* INFO CARDS */
.info-card {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-radius: 17px;
    padding: 18px;
    min-height: 105px;
    box-shadow: 0 5px 18px rgba(93,55,42,.05);
}

.info-title {
    color: var(--green);
    font-weight: 800;
    font-size: 14px;
}

.info-text {
    color: var(--green);
    opacity: .75;
    font-size: 12px;
    margin-top: 6px;
    line-height: 1.45;
}


/* ALGORITHM PAGE */
.page-header {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-radius: 18px;
    padding: 19px 22px;
    box-shadow: 0 5px 18px rgba(93,55,42,.05);
    margin-bottom: 16px;
}

.page-title {
    color: var(--green);
    font-size: 27px;
    font-weight: 800;
    margin: 0;
}

.page-subtitle {
    color: var(--green);
    opacity: .7;
    font-size: 12px;
    margin-top: 4px;
}


/* FORMULA */
.formula {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-left: 4px solid var(--green);
    border-radius: 12px;
    padding: 12px 15px;
    color: var(--green);
    font-family: 'Poppins', sans-serif !important;
    font-size: 12px;
    line-height: 1.6;
    margin-bottom: 16px;
}


/* STREAMLIT CONTAINER */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-radius: 16px;
    padding: 5px;
    box-shadow: 0 5px 18px rgba(93,55,42,.05);
    margin-bottom: 16px;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    border: none !important;
}

/* Judul panel */
.panel-title {
    color: var(--green);
    font-size: 16px;
    font-weight: 800;
    margin-bottom: 12px;
}


/* INPUT */

div[data-testid="stTextInput"] input {
    background: #fffdf6 !important;
    color: var(--green) !important;
    border: 1px solid rgba(38,66,42,.20) !important;
    border-radius: 10px !important;
}


div[data-testid="stTextInput"] input:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 1px var(--green) !important;
}


/* LABEL INPUT */

div[data-testid="stTextInput"] label {
    color: var(--green) !important;
}


/* RADIO */

div[data-testid="stRadio"] label {
    color: var(--green) !important;
}


/* BUTTON */

div.stButton {
    margin-top: 6px;
}


div.stButton > button {
    background: var(--green) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 42px;
}


div.stButton > button:hover {
    background: #1d3521 !important;
    color: var(--white) !important;
}


/* PLACEHOLDER */

.placeholder {
    background: #fffdf6;
    border: 1px dashed rgba(38,66,42,.30);
    border-radius: 12px;
    padding: 18px;
    color: var(--green);
    opacity: .75;
    text-align: center;
    font-size: 13px;
}


/* NOTE */

.note {
    background: var(--colombia-blue);
    border: 1px solid rgba(38,66,42,.15);
    border-radius: 12px;
    padding: 12px 14px;
    color: var(--green);
    font-size: 12px;
}


/* RESULT */

.result-box {
    background: #eef7ee;
    border: 1px solid rgba(38,66,42,.20);
    border-radius: 14px;
    padding: 16px;
    color: var(--green);
    font-family: 'Poppins', sans-serif !important;
    min-height: 65px;
}


/* DATAFRAME */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* FOOTER */

/* Area utama memenuhi tinggi layar */
.main .block-container {
    min-height: calc(100vh - 5rem);
    display: flex;
    flex-direction: column;
}

/* Kontainer utama Streamlit */
.main .block-container > div[data-testid="stVerticalBlock"] {
    flex: 1;
    display: flex;
    flex-direction: column;
}

/* Dorong elemen footer ke bagian bawah */
div[data-testid="stElementContainer"]:has(.app-footer) {
    margin-top: auto !important;
    width: 100%;
}

/* Tampilan footer */
.app-footer {
    background: var(--brown);
    color: var(--white);
    width: 100%;
    box-sizing: border-box;
    margin-top: 30px;
    padding: 24px 20px;
    text-align: center;
    font-size: 13px;
    font-weight: 600;
    border-radius: 0;
}


/* REMOVE DEFAULT STREAMLIT INFO COLORS */
div[data-testid="stAlert"] {
    border-radius: 14px;
}


/* FORM SPACING */

div[data-testid="stTextInput"] {
    margin-bottom: 6px;
}


div[data-testid="stRadio"] {
    margin-bottom: 4px;
}

/* SPACING BERANDA */

/* Jarak setelah judul Algoritma */
.section-title {
    color: var(--green);
    font-size: 21px;
    font-weight: 800;
    margin: 8px 0 18px;
}

/* Jarak antar kartu algoritma */
.algo-card {
    min-height: 145px;
    border-radius: 18px;
    padding: 18px;
    border: 1px solid var(--green-soft);
    box-shadow: 0 6px 18px rgba(38, 66, 42, 0.06);
    background: var(--white);
    box-sizing: border-box;
}

/* Jarak antara kartu algoritma dan kartu informasi */
.home-section-spacer {
    height: 30px;
}

/* Kartu informasi */
.info-card {
    background: var(--white);
    border: 1px solid var(--green-soft);
    border-radius: 17px;
    padding: 20px;
    min-height: 110px;
    box-shadow: 0 5px 18px rgba(38, 66, 42, 0.05);
    box-sizing: border-box;
}

/* SIDEBAR MENU BUTTON */

/* Tombol menu tidak aktif */
section[data-testid="stSidebar"] div.stButton > button {
    background: rgba(255, 255, 255, 0.75) !important;
    color: var(--green) !important;
    border: 1px solid rgba(38, 66, 42, 0.15) !important;
    border-radius: 10px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 10px 14px !important;
    min-height: 42px;
    margin-bottom: 5px;
}

/* Tombol menu aktif */
section[data-testid="stSidebar"]
div.stButton > button[data-testid="stBaseButton-primary"] {
    background: var(--green) !important;
    color: var(--white) !important;
    border: 1px solid var(--green) !important;
    font-weight: 700 !important;
}

/* Efek hover */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: rgba(38, 66, 42, 0.12) !important;
    color: var(--green) !important;
    border-color: var(--green) !important;
}

/* Hover tombol aktif */
section[data-testid="stSidebar"]
div.stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #1d3521 !important;
    color: var(--white) !important;
}

</style>
""", unsafe_allow_html=True)


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

    # KOLOM KIRI
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
                "Proses",
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
            'Area ini disediakan untuk penjelasan proses, '
            'rumus, representasi karakter/biner, atau tahapan algoritma.'
            '</div>',
            unsafe_allow_html=True
        )

    return mode, text, key

def caesar_page():
    left, right = st.columns([1.05, 1.35], gap="large")

    # ========================================================
    # KOLOM KIRI: INPUT DAN HASIL
    # ========================================================

    with left:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Input</div>',
                unsafe_allow_html=True
            )

            mode = st.radio(
                "Pilih Proses",
                ["Enkripsi", "Dekripsi"],
                horizontal=True,
                key="caesar_mode"
            )

            text = st.text_input(
                "Masukkan Teks",
                key="caesar_text"
            )

            key = st.text_input(
                "Kunci (k)",
                key="caesar_key"
            )

            proses = st.button(
                "Proses",
                type="primary",
                use_container_width=True,
                key="caesar_button"
            )

        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Hasil</div>',
                unsafe_allow_html=True
            )

            if proses:
                if not text:
                    st.warning("Masukkan teks terlebih dahulu.")

                elif not key.strip():
                    st.warning("Masukkan kunci terlebih dahulu.")

                else:
                    try:
                        kunci = int(key)

                        if mode == "Enkripsi":
                            hasil = caesar.encrypt(text, kunci)
                        else:
                            hasil = caesar.decrypt(text, kunci)

                        st.markdown(
                            '<div class="result-box">'
                            '<b>Hasil {}:</b><br>{}'
                            '</div>'.format(mode, hasil),
                            unsafe_allow_html=True
                        )

                    except ValueError:
                        st.error(
                            "Kunci harus berupa bilangan bulat."
                        )

            else:
                st.markdown(
                    '<div class="placeholder">'
                    'Hasil algoritma akan ditampilkan di sini.'
                    '</div>',
                    unsafe_allow_html=True
                )

    # ========================================================
    # KOLOM KANAN: LANGKAH-LANGKAH PROSES
    # ========================================================

    with right:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">'
                'Langkah-langkah Proses'
                '</div>',
                unsafe_allow_html=True
            )

            if proses and text and key.strip():
                try:
                    kunci = int(key)

                    langkah = caesar.get_steps(
                        text, kunci, mode
                    )

                    if langkah:
                        st.dataframe(
                            langkah,
                            use_container_width=True,
                            hide_index=True
                        )
                    else:
                        st.info("Tidak ada karakter untuk diproses.")

                except ValueError:
                    st.info(
                        "Masukkan kunci berupa bilangan bulat "
                        "untuk melihat langkah proses."
                    )

            else:
                st.markdown(
                    '<div class="placeholder">'
                    'Tabel perhitungan setiap karakter '
                    'akan ditampilkan di sini.'
                    '</div>',
                    unsafe_allow_html=True
                )

        st.markdown(
            '<div class="note">'
            '<b>Catatan:</b> Caesar Cipher menggeser setiap '
            'huruf berdasarkan nilai kunci. Spasi, angka, '
            'dan simbol tidak mengalami perubahan.'
            '</div>',
            unsafe_allow_html=True
        )

def footer():
    st.markdown("""
    <div class="app-footer">
        CryptoLab - Project Mata Kuliah Kriptografi
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# LFSR STREAM CIPHER PAGE
# ============================================================

def lfsr_page():
    left, right = st.columns([1.05, 1.35], gap="large")

    # ========================================================
    # KOLOM KIRI: INPUT DAN HASIL
    # ========================================================

    with left:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Input</div>',
                unsafe_allow_html=True
            )

            mode = st.radio(
                "Pilih Proses",
                ["Enkripsi", "Dekripsi"],
                horizontal=True,
                key="lfsr_mode"
            )

            if mode == "Enkripsi":
                input_label = "Masukkan Teks"
                placeholder = "Masukkan teks yang akan dienkripsi..."
            else:
                input_label = "Ciphertext (Hexadecimal)"
                placeholder = "Masukkan ciphertext hexadecimal..."

            text = st.text_area(
                input_label,
                placeholder=placeholder,
                key="lfsr_text"
            )

            seed = st.text_input(
                "Seed Awal (8 bit biner)",
                placeholder="Contoh: 10110010",
                key="lfsr_seed"
            )

            proses = st.button(
                "Proses",
                type="primary",
                use_container_width=True,
                key="lfsr_button"
            )

        # ====================================================
        # HASIL
        # ====================================================

        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">Hasil</div>',
                unsafe_allow_html=True
            )

            if proses:
                if not text.strip():
                    st.warning("Masukkan teks terlebih dahulu.")

                elif not seed.strip():
                    st.warning("Masukkan seed awal terlebih dahulu.")

                else:
                    try:
                        if mode == "Enkripsi":
                            hasil = lfsr.encrypt(text, seed)
                        else:
                            hasil = lfsr.decrypt(text, seed)

                        st.markdown(
                            f'<div class="result-box">'
                            f'<b>Hasil {mode}:</b>'
                            f'</div>',
                            unsafe_allow_html=True
                        )

                        st.code(hasil, language=None)

                    except ValueError as e:
                        st.error(str(e))

            else:
                st.markdown(
                    '<div class="placeholder">'
                    'Hasil enkripsi atau dekripsi akan ditampilkan di sini.'
                    '</div>',
                    unsafe_allow_html=True
                )

    # ========================================================
    # KOLOM KANAN: LANGKAH PROSES
    # ========================================================

    with right:
        with st.container(border=True):
            st.markdown(
                '<div class="panel-title">'
                'Langkah-langkah Proses'
                '</div>',
                unsafe_allow_html=True
            )

            if proses and text.strip() and seed.strip():
                try:
                    langkah = lfsr.get_steps(text, seed, mode)

                    if langkah:
                        st.dataframe(
                            langkah,
                            use_container_width=True,
                            hide_index=True
                        )
                    else:
                        st.info("Tidak ada data untuk diproses.")

                except ValueError as e:
                    st.info(str(e))

            else:
                st.markdown(
                    '<div class="placeholder">'
                    'Tabel perhitungan byte dan keystream '
                    'akan ditampilkan di sini.'
                    '</div>',
                    unsafe_allow_html=True
                )

        st.markdown(
            '<div class="note">'
            '<b>Catatan:</b> LFSR menghasilkan keystream dari '
            'register biner. Keystream kemudian digunakan untuk '
            'melakukan operasi XOR terhadap data input. '
            'Dekripsi menggunakan seed yang sama.'
            '</div>',
            unsafe_allow_html=True
        )

# ============================================================
# FOOTER FUNCTION
# ============================================================

def footer():
    st.markdown(
        """
        <div class="app-footer">
            CryptoLab - Project Mata Kuliah Kriptografi
        </div>
        """,
        unsafe_allow_html=True
    )

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

    # ========================================================
    # KARTU ALGORITMA
    # ========================================================

    cards = [
        ("1", "Caesar Cipher", "Klasik", "card-caesar"),
        ("2", "Vigenère Cipher", "Klasik", "card-vigenere"),
        ("3", "XOR Cipher", "Modern", "card-xor"),
        ("4", "LFSR Stream Cipher", "Modern", "card-lfsr"),
        ("5", "Super Encryption", "Gabungan 4 Algoritma", "card-super"),
    ]

    cols = st.columns(5, gap="medium")

    for col, (num, name, typ, cls) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="algo-card {cls}">
                    <div class="algo-number">{num}</div>
                    <div class="algo-name">{name}</div>
                    <div class="algo-type">{typ}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Jarak antara kartu algoritma dan kartu informasi
    st.markdown(
        '<div class="home-section-spacer"></div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # KARTU INFORMASI
    # ========================================================

    info = [
        (
            "Mudah Digunakan",
            "Antarmuka sederhana dan interaktif."
        ),
        (
            "Proses Algoritma",
            "Menampilkan langkah-langkah enkripsi dan dekripsi."
        ),
        (
            "Belajar Kriptografi",
            "Disiapkan untuk mendukung pembelajaran materi kuliah."
        ),
    ]

    cols = st.columns(3, gap="large")

    for col, (title, desc) in zip(cols, info):
        with col:
            st.markdown(
                f"""
                <div class="info-card">
                    <div class="info-title">{title}</div>
                    <div class="info-text">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


elif menu == "1. Caesar Cipher":
    algorithm_header(
        "1. Caesar Cipher (Klasik)",
        "Implementasi algoritma Caesar Cipher untuk "
        "proses enkripsi dan dekripsi.",
        "Enkripsi : C = (P + k) mod 26<br>"
        "Dekripsi : P = (C - k) mod 26"
    )

    caesar_page()

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
        "Implementasi algoritma LFSR Stream Cipher untuk "
        "proses enkripsi dan dekripsi.",
        "Keystream dibangkitkan oleh LFSR kemudian digunakan "
        "pada operasi XOR.<br>"
        "C = P XOR K<br>"
        "P = C XOR K"
    )

    lfsr_page()

elif menu == "5. Super Encryption":
    algorithm_header(
        "5. Super Encryption (Gabungan 4 Algoritma)",
        "Kerangka integrasi empat algoritma. Implementasi akan dikerjakan Anggota 4.",
        "Caesar → Vigenère → XOR → LFSR"
    )

    # ========================================================
    # INPUT & PARAMETER
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="panel-title">Input & Parameter Kunci</div>',
            unsafe_allow_html=True
        )

        left, right = st.columns([1.3, 1], gap="large")

        with left:

            st.radio(
                "Pilih Proses",
                ["Enkripsi", "Dekripsi"],
                horizontal=True,
                key="super_mode"
            )

            st.text_input(
                "Masukkan Teks",
                key="super_text"
            )

        with right:

            st.text_input(
                "Kunci Caesar (k)",
                key="super_caesar"
            )

            st.text_input(
                "Kunci Vigenère",
                key="super_vigenere"
            )

            st.text_input(
                "Kunci XOR",
                key="super_xor"
            )

            st.text_input(
                "Seed LFSR (biner)",
                key="super_lfsr"
            )

        st.button(
            "Proses Super Encryption",
            type="primary",
            use_container_width=True,
            key="super_button"
        )


    # ========================================================
    # HASIL SUPER ENCRYPTION
    # ========================================================

    left, right = st.columns([1.25, 1], gap="large")


    with left:

        with st.container(border=True):

            st.markdown(
                '<div class="panel-title">Tahapan Proses</div>',
                unsafe_allow_html=True
            )

            st.markdown("""
            <div class="placeholder">

                <b>1.</b> Caesar Cipher<br><br>
                <b>2.</b> Vigenère Cipher<br><br>
                <b>3.</b> XOR Cipher<br><br>
                <b>4.</b> LFSR Stream Cipher

            </div>
            """, unsafe_allow_html=True)


    with right:

        with st.container(border=True):

            st.markdown(
                '<div class="panel-title">Hasil Akhir</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="placeholder">'
                'Hasil Super Encryption akan diisi Anggota 4.'
                '</div>',
                unsafe_allow_html=True
            )

elif menu == "Tentang Aplikasi":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">Tentang Aplikasi</div>
            <div class="page-subtitle">
                Informasi mengenai aplikasi CryptoLab.
            </div>
        </div>

        <div class="info-card">
            <div class="info-title">CryptoLab</div>
            <div class="info-text">
                CryptoLab merupakan aplikasi pembelajaran kriptografi
                yang digunakan untuk memahami proses enkripsi dan
                dekripsi melalui algoritma klasik, modern, dan
                super encryption.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif menu == "Kelompok":
    st.markdown(
        """
        <div class="page-header">
            <div class="page-title">Kelompok</div>
            <div class="page-subtitle">
                Informasi anggota dan pembagian tugas proyek.
            </div>
        </div>

        <div class="info-card">
            <div class="info-title">Anggota Kelompok</div>
            <div class="info-text">
                Daftar anggota dan pembagian tugas akan ditambahkan
                bersama anggota kelompok.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

footer()

    