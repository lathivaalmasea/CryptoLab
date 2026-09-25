# ============================================================
# AES-128 CIPHER
# Penanggung jawab: Anggota 3
# ============================================================
# Fungsi utama:
# - encrypt()         : Mengenkripsi plaintext menjadi ciphertext heksadesimal
# - decrypt()         : Mendekripsi ciphertext heksadesimal menjadi plaintext
# - get_steps()       : Menghasilkan rincian proses enkripsi/dekripsi
# - get_sbox()        : Mengambil tabel S-Box AES
# - get_inverse_sbox(): Mengambil tabel Inverse S-Box AES
# - get_round_keys()  : Mengambil 11 round key AES-128
#
# Mode: ECB
# Padding: PKCS#7
# Ukuran blok: 16 byte
# Panjang kunci: tepat 16 byte (128 bit) setelah encoding UTF-8
# ============================================================


# ============================================================
# KONSTANTA AES
# ============================================================

RCON = [
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10,
    0x20, 0x40, 0x80, 0x1B, 0x36
]

# ============================================================
# OPERASI DASAR GF(2^8) DAN PEMBENTUKAN S-BOX
# ============================================================

def _gmul(a, b):
    """Mengalikan dua nilai byte pada medan hingga GF(2^8)."""
    result = 0

    for _ in range(8):
        if b & 1:
            result ^= a

        high_bit = a & 0x80
        a = (a << 1) & 0xFF

        if high_bit:
            a ^= 0x1B

        b >>= 1

    return result


def _gpow(value, exponent):
    """Menghitung perpangkatan pada GF(2^8)."""
    result = 1

    while exponent:
        if exponent & 1:
            result = _gmul(result, value)

        value = _gmul(value, value)
        exponent >>= 1

    return result


def _rotate_left_8(value, shift):
    """Melakukan rotasi bit ke kiri pada nilai 8-bit."""
    return ((value << shift) | (value >> (8 - shift))) & 0xFF


def _make_sboxes():
    """
    Membentuk S-Box dan Inverse S-Box AES.

    S-Box dibentuk dari invers perkalian GF(2^8), kemudian
    diterapkan transformasi affine sesuai dengan standar AES.
    """
    sbox = []
    inverse_sbox = [0] * 256

    for value in range(256):
        inverse = 0 if value == 0 else _gpow(value, 254)

        substituted = (
            inverse
            ^ _rotate_left_8(inverse, 1)
            ^ _rotate_left_8(inverse, 2)
            ^ _rotate_left_8(inverse, 3)
            ^ _rotate_left_8(inverse, 4)
            ^ 0x63
        )

        sbox.append(substituted)
        inverse_sbox[substituted] = value

    return sbox, inverse_sbox


SBOX, INV_SBOX = _make_sboxes()


# ============================================================
# KONVERSI DATA DAN MATRIKS STATE
# ============================================================

def _to_state(block):
    """
    Mengubah 16 byte menjadi matriks state 4x4.

    AES mengisi state berdasarkan kolom:
    state[baris][kolom] = block[baris + 4 * kolom].
    """
    return [
        [block[row + 4 * col] for col in range(4)]
        for row in range(4)
    ]


def _from_state(state):
    """Mengubah matriks state 4x4 kembali menjadi 16 byte."""
    return bytes(
        state[row][col]
        for col in range(4)
        for row in range(4)
    )


def _state_to_hex(state):
    """Mengubah setiap byte dalam matriks state menjadi heksadesimal."""
    return [
        [f"{value:02x}" for value in row]
        for row in state
    ]


def _save_step(steps, title, description, state, round_number=None):
    """Menyimpan satu langkah proses agar dapat ditampilkan di Streamlit."""
    steps.append({
        "tahap": title,
        "putaran": round_number,
        "penjelasan": description,
        "state": _state_to_hex(state)
    })


# ============================================================
# TRANSFORMASI AES
# ============================================================

def _add_round_key(state, round_key):
    """Melakukan XOR antara state dan round key."""
    key_state = _to_state(round_key)

    for row in range(4):
        for col in range(4):
            state[row][col] ^= key_state[row][col]


def _sub_bytes(state, substitution_box=SBOX):
    """Mengganti setiap byte state menggunakan tabel substitusi."""
    for row in range(4):
        for col in range(4):
            state[row][col] = substitution_box[state[row][col]]


def _shift_rows(state):
    """Menggeser baris state ke kiri secara siklik."""
    for row in range(1, 4):
        state[row] = state[row][row:] + state[row][:row]


def _inverse_shift_rows(state):
    """Menggeser baris state ke kanan secara siklik."""
    for row in range(1, 4):
        state[row] = state[row][-row:] + state[row][:-row]


def _mix_columns(state):
    """
    Mencampur byte pada setiap kolom menggunakan matriks MixColumns
    dalam GF(2^8).
    """
    for col in range(4):
        a0, a1, a2, a3 = [state[row][col] for row in range(4)]

        state[0][col] = (
            _gmul(a0, 2) ^ _gmul(a1, 3) ^ a2 ^ a3
        )
        state[1][col] = (
            a0 ^ _gmul(a1, 2) ^ _gmul(a2, 3) ^ a3
        )
        state[2][col] = (
            a0 ^ a1 ^ _gmul(a2, 2) ^ _gmul(a3, 3)
        )
        state[3][col] = (
            _gmul(a0, 3) ^ a1 ^ a2 ^ _gmul(a3, 2)
        )


def _inverse_mix_columns(state):
    """Melakukan transformasi kebalikan MixColumns."""
    for col in range(4):
        a0, a1, a2, a3 = [state[row][col] for row in range(4)]

        state[0][col] = (
            _gmul(a0, 14) ^ _gmul(a1, 11)
            ^ _gmul(a2, 13) ^ _gmul(a3, 9)
        )
        state[1][col] = (
            _gmul(a0, 9) ^ _gmul(a1, 14)
            ^ _gmul(a2, 11) ^ _gmul(a3, 13)
        )
        state[2][col] = (
            _gmul(a0, 13) ^ _gmul(a1, 9)
            ^ _gmul(a2, 14) ^ _gmul(a3, 11)
        )
        state[3][col] = (
            _gmul(a0, 11) ^ _gmul(a1, 13)
            ^ _gmul(a2, 9) ^ _gmul(a3, 14)
        )


# ============================================================
# KEY EXPANSION (PEMBANGKITAN ROUND KEY)
# ============================================================

def _expand_key(key):
    """
    Membentuk 11 round key AES-128 dari kunci 16 byte.

    Setiap round key berukuran 16 byte. AES-128 menggunakan
    Round Key 0 sampai Round Key 10.
    """
    if len(key) != 16:
        raise ValueError(
            "Kunci AES-128 harus tepat 16 byte (128 bit) "
            "setelah di-encode UTF-8."
        )

    # Kunci awal dibagi menjadi 4 word, masing-masing 4 byte.
    words = [
        list(key[index:index + 4])
        for index in range(0, 16, 4)
    ]

    # AES-128 membutuhkan total 44 word atau 11 round key.
    for index in range(4, 44):
        temp = words[index - 1][:]

        if index % 4 == 0:
            # RotWord: rotasi byte ke kiri.
            temp = temp[1:] + temp[:1]

            # SubWord: substitusi setiap byte dengan S-Box.
            temp = [SBOX[value] for value in temp]

            # XOR dengan konstanta round RCON.
            temp[0] ^= RCON[index // 4]

        new_word = [
            words[index - 4][byte] ^ temp[byte]
            for byte in range(4)
        ]
        words.append(new_word)

    round_keys = []

    for round_number in range(11):
        start = round_number * 4
        round_key_words = words[start:start + 4]
        round_key = bytes(
            value
            for word in round_key_words
            for value in word
        )
        round_keys.append(round_key)

    return round_keys


# ============================================================
# PADDING PKCS#7
# ============================================================

def _pad(data):
    """Menambahkan padding agar panjang data menjadi kelipatan 16 byte."""
    padding_length = 16 - (len(data) % 16)
    return data + bytes([padding_length]) * padding_length


def _unpad(data):
    """Menghapus dan memvalidasi padding PKCS#7 setelah dekripsi."""
    if not data:
        raise ValueError("Data hasil dekripsi kosong.")

    padding_length = data[-1]

    if (
        padding_length < 1
        or padding_length > 16
        or data[-padding_length:] != bytes([padding_length]) * padding_length
    ):
        raise ValueError(
            "Padding tidak valid. Pastikan ciphertext dan kunci benar."
        )

    return data[:-padding_length]


# ============================================================
# PROSES ENKRIPSI PER BLOK
# ============================================================

def _encrypt_block(block, round_keys, steps=None, block_number=1):
    """Mengenkripsi satu blok data berukuran 16 byte."""
    state = _to_state(block)

    if steps is not None:
        _save_step(
            steps,
            f"Blok {block_number} - State Awal",
            "16 byte plaintext disusun menjadi matriks state 4x4 per kolom.",
            state
        )

    # Initial Round: AddRoundKey.
    _add_round_key(state, round_keys[0])

    if steps is not None:
        _save_step(
            steps,
            "AddRoundKey (Initial Round)",
            "State di-XOR dengan Round Key 0.",
            state,
            0
        )

    # Putaran 1 sampai 9.
    for round_number in range(1, 10):
        _sub_bytes(state)
        if steps is not None:
            _save_step(
                steps, "SubBytes",
                "Setiap byte diganti menggunakan tabel S-Box AES.",
                state, round_number
            )

        _shift_rows(state)
        if steps is not None:
            _save_step(
                steps, "ShiftRows",
                "Baris 0 tetap; baris 1, 2, dan 3 digeser ke kiri "
                "masing-masing 1, 2, dan 3 byte secara siklik.",
                state, round_number
            )

        _mix_columns(state)
        if steps is not None:
            _save_step(
                steps, "MixColumns",
                "Setiap kolom dicampur menggunakan matriks AES di GF(2^8).",
                state, round_number
            )

        _add_round_key(state, round_keys[round_number])
        if steps is not None:
            _save_step(
                steps, "AddRoundKey",
                f"State di-XOR dengan Round Key {round_number}.",
                state, round_number
            )

    # Final Round: tidak menggunakan MixColumns.
    _sub_bytes(state)
    if steps is not None:
        _save_step(
            steps, "SubBytes (Final Round)",
            "Substitusi byte menggunakan S-Box pada putaran terakhir.",
            state, 10
        )

    _shift_rows(state)
    if steps is not None:
        _save_step(
            steps, "ShiftRows (Final Round)",
            "Pergeseran siklik baris pada putaran terakhir.",
            state, 10
        )

    _add_round_key(state, round_keys[10])
    if steps is not None:
        _save_step(
            steps, "AddRoundKey (Final Round)",
            "State di-XOR dengan Round Key 10. MixColumns tidak dilakukan.",
            state, 10
        )

    return _from_state(state)


# ============================================================
# PROSES DEKRIPSI PER BLOK
# ============================================================

def _decrypt_block(block, round_keys, steps=None, block_number=1):
    """Mendekripsi satu blok ciphertext berukuran 16 byte."""
    state = _to_state(block)

    if steps is not None:
        _save_step(
            steps,
            f"Blok {block_number} - State Ciphertext",
            "Ciphertext 16 byte disusun menjadi matriks state 4x4.",
            state
        )

    # Mulai dengan Round Key 10.
    _add_round_key(state, round_keys[10])
    if steps is not None:
        _save_step(
            steps, "AddRoundKey (Round 10)",
            "State di-XOR dengan Round Key 10.",
            state, 10
        )

    # Putaran 9 sampai 1.
    for round_number in range(9, 0, -1):
        _inverse_shift_rows(state)
        if steps is not None:
            _save_step(
                steps, "InvShiftRows",
                "Baris digeser ke kanan: 1, 2, dan 3 byte secara siklik.",
                state, round_number
            )

        _sub_bytes(state, INV_SBOX)
        if steps is not None:
            _save_step(
                steps, "InvSubBytes",
                "Setiap byte disubstitusi menggunakan Inverse S-Box.",
                state, round_number
            )

        _add_round_key(state, round_keys[round_number])
        if steps is not None:
            _save_step(
                steps, "AddRoundKey",
                f"State di-XOR dengan Round Key {round_number}.",
                state, round_number
            )

        _inverse_mix_columns(state)
        if steps is not None:
            _save_step(
                steps, "InvMixColumns",
                "Transformasi kebalikan MixColumns pada setiap kolom.",
                state, round_number
            )

    # Tahap akhir dekripsi menggunakan Round Key 0.
    _inverse_shift_rows(state)
    if steps is not None:
        _save_step(
            steps, "InvShiftRows (Final)",
            "Pergeseran baris kebalikan pada tahap akhir.",
            state, 0
        )

    _sub_bytes(state, INV_SBOX)
    if steps is not None:
        _save_step(
            steps, "InvSubBytes (Final)",
            "Substitusi byte menggunakan Inverse S-Box.",
            state, 0
        )

    _add_round_key(state, round_keys[0])
    if steps is not None:
        _save_step(
            steps, "AddRoundKey (Initial Key)",
            "State di-XOR dengan Round Key 0 untuk memperoleh plaintext berpadded.",
            state, 0
        )

    return _from_state(state)


# ============================================================
# FUNGSI UTAMA: ENKRIPSI DAN DEKRIPSI
# ============================================================

def encrypt(text, key):
    """
    Mengenkripsi teks menggunakan AES-128 mode ECB dan padding PKCS#7.

    Parameter:
    - text: plaintext berupa string.
    - key : kunci string dengan panjang tepat 16 byte setelah UTF-8.

    Hasil:
    - Ciphertext dalam bentuk string heksadesimal.
    """
    plaintext = text.encode("utf-8")
    key_bytes = key.encode("utf-8")

    padded_data = _pad(plaintext)
    round_keys = _expand_key(key_bytes)

    encrypted_blocks = []

    for start in range(0, len(padded_data), 16):
        block = padded_data[start:start + 16]
        encrypted_blocks.append(_encrypt_block(block, round_keys))

    return b"".join(encrypted_blocks).hex()


def decrypt(ciphertext_hex, key):
    """
    Mendekripsi ciphertext heksadesimal menggunakan AES-128 ECB.

    Parameter:
    - ciphertext_hex: ciphertext dalam format heksadesimal.
    - key           : kunci string dengan panjang tepat 16 byte.

    Hasil:
    - Plaintext dalam bentuk string UTF-8.
    """
    try:
        ciphertext = bytes.fromhex(ciphertext_hex.strip())
    except ValueError as error:
        raise ValueError(
            "Ciphertext harus berupa teks heksadesimal yang valid."
        ) from error

    if not ciphertext or len(ciphertext) % 16 != 0:
        raise ValueError(
            "Panjang ciphertext harus kelipatan 16 byte "
            "(32 digit heksadesimal per blok)."
        )

    round_keys = _expand_key(key.encode("utf-8"))
    decrypted_blocks = []

    for start in range(0, len(ciphertext), 16):
        block = ciphertext[start:start + 16]
        decrypted_blocks.append(_decrypt_block(block, round_keys))

    plaintext_padded = b"".join(decrypted_blocks)
    plaintext = _unpad(plaintext_padded)

    return plaintext.decode("utf-8")


# ============================================================
# FUNGSI LANGKAH PROSES UNTUK STREAMLIT
# ============================================================

def get_steps(text, key, mode="Enkripsi"):
    """
    Menghasilkan rincian tahapan AES untuk ditampilkan di Streamlit.

    Parameter:
    - text: plaintext untuk mode Enkripsi, ciphertext hex untuk Dekripsi.
    - key : kunci AES-128.
    - mode: 'Enkripsi'/'encrypt' atau 'Dekripsi'/'decrypt'.

    Hasil berupa list of dictionaries dengan informasi tahap,
    putaran, penjelasan, dan matriks state.
    """
    steps = []
    round_keys = _expand_key(key.encode("utf-8"))
    normalized_mode = mode.strip().lower()

    if normalized_mode in ("dekripsi", "decrypt"):
        try:
            ciphertext = bytes.fromhex(text.strip())
        except ValueError as error:
            raise ValueError(
                "Ciphertext harus berupa teks heksadesimal yang valid."
            ) from error

        if not ciphertext or len(ciphertext) % 16 != 0:
            raise ValueError(
                "Ciphertext harus memiliki panjang kelipatan 16 byte."
            )

        for start in range(0, len(ciphertext), 16):
            block_number = start // 16 + 1
            block = ciphertext[start:start + 16]
            _decrypt_block(block, round_keys, steps, block_number)

        steps.append({
            "tahap": "Hapus Padding PKCS#7",
            "putaran": "-",
            "penjelasan": (
                "Byte padding dihapus setelah seluruh blok selesai didekripsi."
            ),
            "state": [["-"]]
        })

    elif normalized_mode in ("enkripsi", "encrypt"):
        plaintext = text.encode("utf-8")
        padded_data = _pad(plaintext)
        padding_length = padded_data[-1]

        steps.append({
            "tahap": "Padding PKCS#7",
            "putaran": "-",
            "penjelasan": (
                "Data UTF-8 ditambah padding agar panjangnya kelipatan "
                f"16 byte. Padding yang ditambahkan: {padding_length} byte."
            ),
            "state": [
                [f"{value:02x}" for value in padded_data[start:start + 16]]
                for start in range(0, len(padded_data), 16)
            ]
        })

        for start in range(0, len(padded_data), 16):
            block_number = start // 16 + 1
            block = padded_data[start:start + 16]
            _encrypt_block(block, round_keys, steps, block_number)

    else:
        raise ValueError(
            "Mode harus 'Enkripsi'/'encrypt' atau 'Dekripsi'/'decrypt'."
        )

    return steps


# ============================================================
# FUNGSI TABEL S-BOX DAN ROUND KEY
# ============================================================

def get_sbox():
    """Mengambil tabel S-Box AES dalam bentuk matriks 16x16 heksadesimal."""
    return [
        [f"{SBOX[row * 16 + col]:02x}" for col in range(16)]
        for row in range(16)
    ]


def get_inverse_sbox():
    """Mengambil tabel Inverse S-Box AES dalam bentuk matriks 16x16."""
    return [
        [f"{INV_SBOX[row * 16 + col]:02x}" for col in range(16)]
        for row in range(16)
    ]


def get_round_keys(key):
    """
    Mengambil Round Key 0 sampai 10 dalam bentuk matriks 4x4 heksadesimal.
    """
    round_keys = _expand_key(key.encode("utf-8"))
    return [
        _state_to_hex(_to_state(round_key))
        for round_key in round_keys
    ]


# ============================================================
# PENGUJIAN MODUL
# Jalankan file ini secara langsung untuk menguji fungsi.
# ============================================================

if __name__ == "__main__":
    plaintext = "Hello World!"
    key = "1234567890ABCDEF"

    encrypted_text = encrypt(plaintext, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Teks asli      :", plaintext)
    print("Kunci          :", key)
    print("Hasil enkripsi :", encrypted_text)
    print("Hasil dekripsi :", decrypted_text)

    print("\nLangkah Enkripsi:")
    for step in get_steps(plaintext, key, "Enkripsi"):
        print(step)

    print("\nLangkah Dekripsi:")
    for step in get_steps(encrypted_text, key, "Dekripsi"):
        print(step)
