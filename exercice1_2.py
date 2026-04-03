import hashlib
h1 = hashlib.sha256(b'Bitcoin').hexdigest()
h2 = hashlib.sha256(b'bitcoin').hexdigest()

diff = sum(a != b for a, b in zip(h1, h2))
print("Caractères différents :", diff, "/ 64")
print("Pourcentage :", round(diff / 64 * 100, 1), "%")