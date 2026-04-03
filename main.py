import hashlib
import sys

def clear_screen():
    print("\n" * 50)

def main_menu():
    while True:
        clear_screen()
        print("="*60)
        print("          CALCULATRICE CRYPTO - SHA-256 & MERKLE TREE")
        print("="*60)
        print("1. Exercice 1.1 - Hash de plusieurs mots")
        print("2. Exercice 1.2 - Comparaison de deux hashes")
        print("3. Exercice 1.3 - SHA-256 simple et double")
        print("4. Exercice 1.4 - Trouver l'entrée d'un hash cible (0-9)")
        print("5. Exercice 2.1a - Hashes individuels des transactions")
        print("6. Exercice 2.1bc - Arbre de Merkle complet")
        print("7. Exercice 2.4 - H33 (double H3)")
        print("0. Quitter")
        print("="*60)
        
        choix = input("\nChoisis un exercice (0-7) : ").strip()
        
        if choix == "1":
            exercice_1_1()
        elif choix == "2":
            exercice_1_2()
        elif choix == "3":
            exercice_1_3()
        elif choix == "4":
            exercice_1_4()
        elif choix == "5":
            exercice_2_1a()
        elif choix == "6":
            exercice_2_1bc()
        elif choix == "7":
            exercice_2_4()
        elif choix == "0":
            print("Au revoir ! 👋")
            sys.exit()
        else:
            print("Choix invalide !")
        
        input("\nAppuie sur Entrée pour revenir au menu...")

# ====================== EXERCICES ======================

def exercice_1_1():
    print("\n--- Exercice 1.1 : Hash de plusieurs mots ---")
    mots = ["Bitcoin", "bitcoin", "Blockchain", "blockchain", "Abidjan2025"]
    print(f"{'Entrée':<18} | SHA-256")
    print("-" * 80)
    for mot in mots:
        hash_calcule = hashlib.sha256(mot.encode('utf-8')).hexdigest()
        print(f"{mot:<18} | {hash_calcule}")

def exercice_1_2():
    print("\n--- Exercice 1.2 : Comparaison de hashes ---")
    h1 = hashlib.sha256(b'Bitcoin').hexdigest()
    h2 = hashlib.sha256(b'bitcoin').hexdigest()
    diff = sum(a != b for a, b in zip(h1, h2))
    print(f"SHA-256('Bitcoin')  = {h1}")
    print(f"SHA-256('bitcoin')   = {h2}")
    print(f"Caractères différents : {diff} / 64")
    print(f"Pourcentage : {round(diff / 64 * 100, 1)}%")

def exercice_1_3():
    print("\n--- Exercice 1.3 : SHA-256 simple et double ---")
    h1 = hashlib.sha256(b'Bitcoin').hexdigest()
    h2 = hashlib.sha256(hashlib.sha256(b'Bitcoin').digest()).hexdigest()
    print(f"SHA-256('Bitcoin')          = {h1}")
    print(f"Double SHA-256('Bitcoin')   = {h2}")

def exercice_1_4():
    print("\n--- Exercice 1.4 : Trouver l'entrée du hash cible ---")
    target_hash = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"
    for i in range(10):
        test_input = str(i)
        test_hash = hashlib.sha256(test_input.encode()).hexdigest()
        print(f"SHA-256(\"{test_input}\") = {test_hash}")
        if test_hash == target_hash:
            print(f"\n✅ TROUVÉ ! L'entrée est : \"{test_input}\"")
            break
    else:
        print("Aucun chiffre de 0 à 9 ne correspond.")

def exercice_2_1a():
    print("\n--- Exercice 2.1a : Hashes individuels ---")
    transactions = {
        "Tx₁": "Alice envoie 0.5 BTC à Bob",
        "Tx₂": "Bob envoie 0.2 BTC à Carol",
        "Tx₃": "Carol envoie 0.1 BTC à Dave",
        "Tx₄": "Dave envoie 0.05 BTC à Alice"
    }
    feuilles = {tx: hashlib.sha256(data.encode('utf-8')).hexdigest() for tx, data in transactions.items()}
    for tx, h in feuilles.items():
        print(f"{tx} = {h}")

def exercice_2_1bc():
    print("\n--- Exercice 2.1bc : Arbre de Merkle complet ---")
    transactions = {
        "Tx₁": "Alice envoie 0.5 BTC à Bob",
        "Tx₂": "Bob envoie 0.2 BTC à Carol",
        "Tx₃": "Carol envoie 0.1 BTC à Dave",
        "Tx₄": "Dave envoie 0.05 BTC à Alice"
    }
    feuilles = {tx: hashlib.sha256(data.encode('utf-8')).hexdigest() for tx, data in transactions.items()}
    niveau1 = list(feuilles.values())
    niveau2 = [
        hashlib.sha256((niveau1[0] + niveau1[1]).encode('utf-8')).hexdigest(),
        hashlib.sha256((niveau1[2] + niveau1[3]).encode('utf-8')).hexdigest()
    ]
    root = hashlib.sha256((niveau2[0] + niveau2[1]).encode('utf-8')).hexdigest()
    print("Niveau intermédiaire :", niveau2)
    print("Merkle Root :", root)

def exercice_2_4():
    print("\n--- Exercice 2.4 : H33 (double H3) ---")
    transactions = {
        "Tx₁": "Alice envoie 0.5 BTC à Bob",
        "Tx₂": "Bob envoie 0.2 BTC à Carol",
        "Tx₃": "Carol envoie 0.1 BTC à Dave",
        "Tx₄": "Dave envoie 0.05 BTC à Alice"
    }
    feuilles = {tx: hashlib.sha256(data.encode('utf-8')).hexdigest() for tx, data in transactions.items()}
    H3 = feuilles["Tx₃"]
    H33 = hashlib.sha256((H3 + H3).encode('utf-8')).hexdigest()
    print("H₃₃ =", H33)

# Lancement du programme
if __name__ == "__main__":
    main_menu()