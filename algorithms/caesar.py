
# ============================================================
# CAESAR CIPHER
# Penanggung jawab: Anggota 1
# ============================================================
# Fungsi:
# - encrypt()  : Enkripsi Caesar Cipher
# - decrypt()  : Dekripsi Caesar Cipher
# - get_steps(): Menampilkan langkah perhitungan algoritma
# ============================================================


def encrypt(text, key):
    """
    Mengenkripsi teks menggunakan Caesar Cipher.
    Huruf besar dan kecil dipertahankan.
    Spasi, angka, dan simbol tidak diubah.
    """
    key = int(key) % 26
    result = ""

    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def decrypt(text, key):
    """
    Mendekripsi teks menggunakan Caesar Cipher.
    """
    key = int(key) % 26
    return encrypt(text, -key)


def get_steps(text, key, mode):
    """
    Menghasilkan rincian langkah per karakter.

    mode:
    - 'Enkripsi' atau 'encrypt'
    - 'Dekripsi' atau 'decrypt'

    Hasil berupa list of dictionaries agar dapat
    ditampilkan sebagai tabel di Streamlit.
    """
    key = int(key) % 26

    if mode.lower() in ("enkripsi", "encrypt"):
        shift = key
        process_name = "Enkripsi"
    elif mode.lower() in ("dekripsi", "decrypt"):
        shift = -key
        process_name = "Dekripsi"
    else:
        raise ValueError(
            "Mode harus 'Enkripsi' atau 'Dekripsi'."
        )

    steps = []

    for index, char in enumerate(text, start=1):
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            original_value = ord(char) - base
            result_value = (original_value + shift) % 26
            result_char = chr(base + result_value)

            if shift >= 0:
                formula = (
                    f"({original_value} + {shift}) mod 26"
                    f" = {result_value}"
                )
            else:
                formula = (
                    f"({original_value} - {abs(shift)}) mod 26"
                    f" = {result_value}"
                )

            steps.append({
                "No": index,
                "Karakter Asli": char,
                "Nilai Huruf": original_value,
                "Perhitungan": formula,
                "Hasil": result_char
            })

        else:
            steps.append({
                "No": index,
                "Karakter Asli": char,
                "Nilai Huruf": "-",
                "Perhitungan": "Karakter tidak diubah",
                "Hasil": char
            })

    return steps


# ============================================================
# PENGUJIAN MODUL
# Jalankan file ini secara langsung untuk menguji fungsi.
# ============================================================

if __name__ == "__main__":
    teks = "Hello World!"
    kunci = 3

    hasil_enkripsi = encrypt(teks, kunci)
    hasil_dekripsi = decrypt(hasil_enkripsi, kunci)

    print("Teks asli      :", teks)
    print("Kunci          :", kunci)
    print("Hasil enkripsi :", hasil_enkripsi)
    print("Hasil dekripsi :", hasil_dekripsi)

    print("\nLangkah Enkripsi:")
    for langkah in get_steps(teks, kunci, "Enkripsi"):
        print(langkah)

    print("\nLangkah Dekripsi:")
    for langkah in get_steps(
        hasil_enkripsi, kunci, "Dekripsi"
    ):
        print(langkah)