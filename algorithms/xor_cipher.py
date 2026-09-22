import pandas as pd

def xor_bytes(data, key):
    return bytes(b ^ key for b in data)

def xor_encrypt(text, key):
    return xor_bytes(text.encode("utf-8"), key).decode("utf-8", errors="replace")

def xor_decrypt(text, key):
    return xor_bytes(text.encode("utf-8"), key).decode("utf-8", errors="replace")

def xor_steps(text, key, process):
    rows = []
    for i, b in enumerate(text.encode("utf-8"), 1):
        out = b ^ key
        rows.append({
            "Byte": i,
            "Input": b,
            "Input (biner)": format(b, "08b"),
            "Kunci": key,
            "Kunci (biner)": format(key, "08b"),
            "XOR": format(out, "08b"),
            "Hasil": out
        })
    return pd.DataFrame(rows)
