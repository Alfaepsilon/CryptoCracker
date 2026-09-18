import secrets


#Example of PKCS#1 v1.5 padding for encryption
"""
def pkcs1_v15_pad(message, k):
    ps_len = k - len(message) - 3

    ps = bytearray()

    while len(ps) < ps_len:
        b = secrets.randbelow(255) + 1
        ps.append(b)

    return b"\x00\x02" + bytes(ps) + b"\x00" + message
"""


def padding_oracle(block):
    # Must start with 0x00 0x02

    if block[0] != 0x00:
        return False

    if block[1] != 0x02:
        return False

    # Find separator byte
    try:
        sep = block.index(0x00, 2)
    except ValueError:
        return False

    # PKCS#1 v1.5 requires at least 8 bytes of padding
    if sep < 10:
        return False

    return True


def decrypt_and_check(ciphertext, d, N):
    m = pow(ciphertext, d, N)

    k = (N.bit_length() + 7) // 8
    block = m.to_bytes(k, "big")

    return padding_oracle(block)


message = b"HELLO"

block = pkcs1_v15_pad(message, 128)

print(len(block))
print(block[:16].hex())