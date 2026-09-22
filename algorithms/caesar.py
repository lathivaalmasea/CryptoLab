import pandas as pd

def _shift_char(ch, key):
    if ch.isalpha() and ch.isascii():
        base = ord("A") if ch.isupper() else ord("a")
        return chr((ord(ch) - base + key) % 26 + base)
    return ch

def caesar_encrypt(text, key):
    return "".join(_shift_char(ch, key) for ch in text)

def caesar_decrypt(text, key):
    return "".join(_shift_char(ch, -key) for ch in text)

def caesar_steps(text, key, process):
    rows = []
    shift = key if process == "Enkripsi" else -key
    for i, ch in enumerate(text, 1):
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - base
            c = (p + shift) % 26
            out = chr(c + base)
            rows.append({"No": i, "Input": ch, "Nilai": p, "Kunci": shift, "Hasil": c, "Output": out})
        else:
            rows.append({"No": i, "Input": ch, "Nilai": "-", "Kunci": "-", "Hasil": "-", "Output": ch})
    return pd.DataFrame(rows)
