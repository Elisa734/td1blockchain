import hashlib

# Le hash à trouver
target_hash = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"

# Tester tous les chiffres de 0 à 9
for i in range(10):
    test_input = str(i)
    test_hash = hashlib.sha256(test_input.encode()).hexdigest()
    
    print(f"SHA-256(\"{test_input}\") = {test_hash}")
    
    if test_hash == target_hash:
        print(f"\n✅ TROUVÉ ! L'entrée est : \"{test_input}\"")
        break