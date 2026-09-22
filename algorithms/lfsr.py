import pandas as pd

def _next_state(state):
    # State: b4 b3 b2 b1.
    # Feedback mengikuti contoh materi: b1 XOR b4.
    feedback = int(state[0]) ^ int(state[3])
    return state[1:] + str(feedback)

def lfsr_keystream(num_bits, seed):
    state = seed
    bits = []
    for _ in range(num_bits):
        output = state[-1]
        bits.append(output)
        state = _next_state(state)
    return "".join(bits)

def lfsr_xor_bytes(data, seed):
    stream = lfsr_keystream(len(data) * 8, seed)
    out = bytearray()
    for i, b in enumerate(data):
        k = int(stream[i*8:(i+1)*8], 2)
        out.append(b ^ k)
    return bytes(out)

def lfsr_steps(seed, num_bytes):
    state = seed
    rows = []
    for i in range(num_bytes * 8):
        output = state[-1]
        feedback = int(state[0]) ^ int(state[3])
        rows.append({
            "Iterasi": i + 1,
            "Register": state,
            "Output Bit": output,
            "Feedback": feedback
        })
        state = state[1:] + str(feedback)
    return pd.DataFrame(rows)
