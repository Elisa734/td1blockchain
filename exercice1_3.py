import hashlib
resultats = {}
resultats["SHA-256('Bitcoin')"] = hashlib.sha256(b'Bitcoin').hexdigest()
resultats["Double SHA-256"] = hashlib.sha256(hashlib.sha256(b'Bitcoin').digest()).hexdigest()

for k, v in resultats.items():
    print(k, "=", v)