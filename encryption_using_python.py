import rsa
from base64 import b64encode, b64decode
msg1 = "Hello Tony, I am Jarvis!"
msg2 = "Hello Toni, I am Jarvis!"
keysize = 2048
(public, private) = rsa.newkeys(keysize)
encrypted = b64encode(rsa.encrypt(str.encode(msg1), private))
decrypted = rsa.decrypt(b64decode(encrypted), private)
decrypted = decrypted.decode()
signature = b64encode(rsa.sign(str.encode(msg1), private, "SHA-512"))
verify = rsa.verify(str.encode(msg1), b64decode(signature), public)
print("Encrypted: " + encrypted.decode())
print("Decrypted: '%s'" % decrypted)
print("Signature: " + signature.decode())
print("Verify: %s" % verify)
#rsa.verify(msg2, b64decode(signature), public)
