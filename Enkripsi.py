# Menggunakan XOR untuk enkripsi
# M Taufik Hidayat Ti.20.D.4
def encrypt(plaintext, key):
  ciphertext = ""
  for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
  return ciphertext

plaintext = "saya akan lulus tepat waktu dan menjadi sarjana"
key = "biasaaja"

ciphertext = encrypt(plaintext, key)
print("Teks terenkripsi:", ciphertext)