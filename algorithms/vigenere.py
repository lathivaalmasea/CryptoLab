import pandas as pd

def _key_values(key):
    return [ord(ch.upper()) - ord("A") for ch in key if ch.isalpha() and ch.isascii()]

def _transform(text, key, direction):
    values = _key_values(key)
    if not values:
        raise ValueError("Kunci Vigenère harus mengandung huruf A-Z.")

    result = []
    ki = 0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - base
            k = values[ki % len(values)]
            result.append(chr((p + direction * k) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return "".join(result)

def vigenere_encrypt(text, key):
    return _transform(text, key, 1)

def vigenere_decrypt(text, key):
    return _transform(text, key, -1)

def vigenere_steps(text, key, process):
    values = _key_values(key)
    if not values:
        raise ValueError("Kunci Vigenère harus mengandung huruf A-Z.")

    direction = 1 if process == "Enkripsi" else -1
    rows, ki = [], 0

    for i, ch in enumerate(text, 1):
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - base
            k = values[ki % len(values)]
            c = (p + direction * k) % 26
            out = chr(c + base)
            rows.append({
                "No": i, "Input": ch, "Nilai": p,
                "Kunci": chr(k + 65), "Nilai K": k,
                "Hasil": c, "Output": out
            })
            ki += 1
        else:
            rows.append({"No": i, "Input": ch, "Nilai": "-", "Kunci": "-", "Nilai K": "-", "Hasil": "-", "Output": ch})

    return pd.DataFrame(rows)
