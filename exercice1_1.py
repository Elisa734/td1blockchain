import hashlib

mots = ["Bitcoin", "bitcoin", "Blockchain", "blockchain", "Abidjan2025"]

print("Entrée            | SHA-256")
print("-" * 80)

for mot in mots:
    hash_calcule = hashlib.sha256(mot.encode('utf-8')).hexdigest()
    print(f"{mot:18} | {hash_calcule}")