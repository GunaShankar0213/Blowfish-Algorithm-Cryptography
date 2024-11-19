import text_alg as blowfish
import base64
import datetime

cipher = blowfish.Cipher(b"admin_key")

def encrypt_msg(msg):
    msg = str.encode(msg)
    cipher_text = b"".join(cipher.encrypt_ecb_cts(msg))
    cipher_text = base64.b64encode(cipher_text)
    return cipher_text.decode('utf-8')

def decrypt_msg(msg):
    msg = str.encode(msg)
    cipher_text = base64.b64decode(msg)
    plain_text = b"".join(cipher.decrypt_ecb_cts(cipher_text))
    return plain_text.decode('utf-8')

if __name__ == "__main__":
    t1 = datetime.datetime.now()
    # setting user message
    msg = "Testing the blowfish"
    # calling encrypted message
    val = encrypt_msg(msg)
    print(val)
    val = decrypt_msg(val)
    print(val)
    t2 = datetime.datetime.now()
    print(t2-t1)
