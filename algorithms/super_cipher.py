from algorithms.caesar import caesar_encrypt, caesar_decrypt
from algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from algorithms.xor_cipher import xor_bytes
from algorithms.lfsr import lfsr_xor_bytes

def super_encrypt(text, caesar_key, vigenere_key, xor_key, lfsr_seed):
    stage1 = caesar_encrypt(text, caesar_key)
    stage2 = vigenere_encrypt(stage1, vigenere_key)
    stage3_bytes = xor_bytes(stage2.encode("utf-8"), xor_key)
    stage3 = stage3_bytes.hex()
    stage4_bytes = lfsr_xor_bytes(stage3_bytes, lfsr_seed)
    final = stage4_bytes.hex()

    stages = [
        ("Caesar Cipher", stage1),
        ("Vigenère Cipher", stage2),
        ("XOR Cipher (hex)", stage3),
        ("LFSR Stream Cipher (hex)", final),
    ]
    return final, stages

def super_decrypt(cipher_hex, caesar_key, vigenere_key, xor_key, lfsr_seed):
    stage4_bytes = bytes.fromhex(cipher_hex)
    stage3_bytes = lfsr_xor_bytes(stage4_bytes, lfsr_seed)
    stage3 = stage3_bytes.hex()
    stage2_bytes = xor_bytes(stage3_bytes, xor_key)
    stage2 = stage2_bytes.decode("utf-8")
    stage1 = vigenere_decrypt(stage2, vigenere_key)
    final = caesar_decrypt(stage1, caesar_key)

    stages = [
        ("LFSR Stream Cipher dibalik (hex)", stage3),
        ("XOR Cipher dibalik", stage2),
        ("Vigenère Cipher dibalik", stage1),
        ("Caesar Cipher dibalik", final),
    ]
    return final, stages
