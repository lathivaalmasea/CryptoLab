# ============================================================
# VIGENÈRE CIPHER
# Penanggung jawab: Anggota 2
# ============================================================
# Fungsi:
# - generate_vigenere_table(): Membuat Bujursangkar Vigenère
# - encrypt()              : Enkripsi Vigenère Cipher
# - decrypt()              : Dekripsi Vigenère Cipher
# - get_steps()            : Menampilkan langkah perhitungan algoritma
# ============================================================



# ============================================================
# 1. BUJURSANGKAR VIGENÈRE
# ============================================================

def generate_vigenere_table():
    """
    Membuat Bujursangkar Vigenère 26x26.

    Setiap baris merupakan pergeseran Caesar.
    A = 0, B = 1, ..., Z = 25
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    table = []


    for row in range(26):

        temp = []

        for col in range(26):

            value = (
                row + col
            ) % 26


            temp.append(
                alphabet[value]
            )


        table.append(temp)


    return table



# ============================================================
# 2. MEMBUAT KEY BERULANG
# ============================================================

def generate_key(text, key):
    """
    Membuat key berulang sesuai panjang plaintext.

    Karakter non alfabet tidak dihitung.
    """

    key = key.upper()

    result = ""

    index = 0


    for char in text:


        if char.isalpha() and char.isascii():

            result += key[
                index % len(key)
            ]

            index += 1


        else:

            result += char


    return result



# ============================================================
# 3. ENKRIPSI VIGENERE
# ============================================================

def encrypt(text, key):
    """
    Enkripsi menggunakan Vigenere Cipher.

    Konsep:
    C = (P + K) mod 26

    Menggunakan konsep Bujursangkar Vigenère.
    """


    key_repeat = generate_key(
        text,
        key
    )


    result = ""


    for text_char, key_char in zip(
        text,
        key_repeat
    ):


        if text_char.isalpha() and text_char.isascii():


            base = (
                ord('A')
                if text_char.isupper()
                else ord('a')
            )


            p = (
                ord(text_char)
                - base
            )


            k = (
                ord(key_char.upper())
                -
                ord('A')
            )


            c = (
                p + k
            ) % 26



            result += chr(
                base + c
            )


        else:

            result += text_char



    return result




# ============================================================
# 4. DEKRIPSI VIGENERE
# ============================================================

def decrypt(text, key):
    """
    Dekripsi menggunakan Vigenere Cipher.

    Konsep:
    P = (C - K) mod 26
    """


    key_repeat = generate_key(
        text,
        key
    )


    result = ""


    for text_char, key_char in zip(
        text,
        key_repeat
    ):


        if text_char.isalpha() and text_char.isascii():


            base = (
                ord('A')
                if text_char.isupper()
                else ord('a')
            )


            c = (
                ord(text_char)
                - base
            )


            k = (
                ord(key_char.upper())
                -
                ord('A')
            )


            p = (
                c - k
            ) % 26



            result += chr(
                base + p
            )


        else:

            result += text_char



    return result




# ============================================================
# 5. LANGKAH PERHITUNGAN
# ============================================================

def get_steps(text, key, mode):
    """
    Menampilkan proses per karakter.
    """

    key_repeat = generate_key(
        text,
        key
    )


    steps = []


    for index, (
        text_char,
        key_char
    ) in enumerate(
        zip(text, key_repeat),
        start=1
    ):


        if text_char.isalpha() and text_char.isascii():


            text_value = (
                ord(text_char.upper())
                -
                ord('A')
            )


            key_value = (
                ord(key_char.upper())
                -
                ord('A')
            )



            if mode.lower() in (
                "enkripsi",
                "encrypt"
            ):


                result_value = (
                    text_value
                    +
                    key_value
                ) % 26



                result_char = chr(
                    ord('A')
                    +
                    result_value
                )



                formula = (
                    f"({text_value} + {key_value}) "
                    f"mod 26 = {result_value}"
                )



            else:


                result_value = (
                    text_value
                    -
                    key_value
                ) % 26



                result_char = chr(
                    ord('A')
                    +
                    result_value
                )



                formula = (
                    f"({text_value} - {key_value}) "
                    f"mod 26 = {result_value}"
                )



            steps.append(

                {
                    "No": index,

                    "Plain/Cipher":
                    text_char,

                    "Kunci":
                    key_char,

                    "Nilai Text":
                    text_value,

                    "Nilai Key":
                    key_value,

                    "Perhitungan":
                    formula,

                    "Hasil":
                    result_char
                }

            )


        else:


            steps.append(

                {
                    "No": index,

                    "Plain/Cipher":
                    text_char,

                    "Kunci":
                    "-",

                    "Nilai Text":
                    "-",

                    "Nilai Key":
                    "-",

                    "Perhitungan":
                    "Karakter tidak berubah",

                    "Hasil":
                    text_char
                }

            )


    return steps




# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":


    text = "INFORMATIKA"

    key = "KEY"



    cipher = encrypt(
        text,
        key
    )


    print(
        "Plaintext :",
        text
    )


    print(
        "Ciphertext:",
        cipher
    )


    print(
        "Decrypt   :",
        decrypt(
            cipher,
            key
        )
    )



    print("\nBujursangkar Vigenere:")


    table = generate_vigenere_table()


    for row in table[:5]:

        print(row)



    print("\nLangkah:")


    for step in get_steps(
        text,
        key,
        "Enkripsi"
    ):

        print(step)
