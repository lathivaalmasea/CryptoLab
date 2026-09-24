
# ============================================================
# LFSR STREAM CIPHER
# ============================================================
# Fungsi:
# - encrypt()           : Enkripsi teks
# - decrypt()           : Dekripsi ciphertext hexadecimal
# - get_steps()         : Menampilkan langkah perhitungan
# - generate_keystream(): Membuat keystream dari seed LFSR
# ============================================================


# ============================================================
# 1. VALIDASI SEED
# ============================================================

def validate_seed(seed):
    seed = seed.strip()

    if len(seed) != 8 or any(bit not in "01" for bit in seed):
        raise ValueError(
            "Seed harus berupa 8 bit biner, contoh: 10110010."
        )

    if seed == "00000000":
        raise ValueError(
            "Seed tidak boleh 00000000."
        )

    return [int(bit) for bit in seed]


# ============================================================
# 2. GENERATE KEYSTREAM
# ============================================================

def generate_keystream(seed, jumlah_byte):
    register = validate_seed(seed)
    keystream = []

    jumlah_bit = jumlah_byte * 8

    for _ in range(jumlah_bit):
        # Bit paling kiri menjadi output
        output_bit = register[0]

        # XOR tap pada posisi 1, 3, 4, dan 5 dari kiri
        feedback = (
            register[0]
            ^ register[2]
            ^ register[3]
            ^ register[4]
        )

        keystream.append(output_bit)

        # Geser register ke kiri dan masukkan feedback
        register = register[1:] + [feedback]

    # Kelompokkan setiap 8 bit menjadi 1 byte
    hasil = []

    for i in range(0, len(keystream), 8):
        byte_biner = "".join(
            str(bit) for bit in keystream[i:i + 8]
        )
        hasil.append(int(byte_biner, 2))

    return hasil


# ============================================================
# 3. ENKRIPSI
# ============================================================

def encrypt(text, seed):
    data = text.encode("utf-8")
    keystream = generate_keystream(seed, len(data))

    hasil = bytes(
        byte ^ key
        for byte, key in zip(data, keystream)
    )

    return hasil.hex().upper()


# ============================================================
# 4. DEKRIPSI
# ============================================================

def decrypt(ciphertext, seed):
    try:
        data = bytes.fromhex(ciphertext)
    except ValueError:
        raise ValueError(
            "Ciphertext harus berupa hexadecimal yang valid."
        )

    keystream = generate_keystream(seed, len(data))

    hasil = bytes(
        byte ^ key
        for byte, key in zip(data, keystream)
    )

    try:
        return hasil.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(
            "Hasil dekripsi bukan teks UTF-8 yang valid. "
            "Pastikan ciphertext dan seed benar."
        )


# ============================================================
# 5. LANGKAH-LANGKAH PROSES
# ============================================================

def get_steps(data_input, seed, mode):
    if mode == "Enkripsi":
        data = data_input.encode("utf-8")
    else:
        try:
            data = bytes.fromhex(data_input)
        except ValueError:
            raise ValueError(
                "Ciphertext harus berupa hexadecimal yang valid."
            )

    keystream = generate_keystream(seed, len(data))

    hasil = bytes(
        byte ^ key
        for byte, key in zip(data, keystream)
    )

    langkah = []

    for i, (byte_input, key, byte_output) in enumerate(
        zip(data, keystream, hasil),
        start=1
    ):
        langkah.append({
            "Byte ke-": i,
            "Byte Input (Hex)": f"{byte_input:02X}",
            "Keystream (Hex)": f"{key:02X}",
            "Operasi XOR": f"{byte_input:08b} XOR {key:08b}",
            "Byte Output (Hex)": f"{byte_output:02X}",
        })

    return langkah