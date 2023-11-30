from hashlib import sha256
key = "Cau"
x = sha256( key.encode() ).hexdigest()


def key_cracking(hashed: str) -> str:
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                for d in range(97, 123):
                    password = chr(a) + chr(b) + chr(c) + chr(d)
                    if sha256(password.encode() ).hexdigest() == hashed:
                        return password












print(key_cracking("a746222f09d85605c52d4e636788d6ffdc274698b98b8c5f3244c06958683a69"))  # snow
print(key_cracking("e6ad06ca7b0a33fbb0ea8d52e482eacca927a5735101bd2a0712d2f230233089"))  # iglu





