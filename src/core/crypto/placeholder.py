#шифрование
class AES256Placeholder:
    def encrypt(self, data: str, key: str) -> str:
        return f"[LOCKED]{data}"

    def decrypt(self, ciphertext: str, key: str) -> str:
        return ciphertext.replace("[LOCKED]", "")