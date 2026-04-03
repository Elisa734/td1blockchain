import hashlib
transactions = {
    "Tx₁": "Alice envoie 0.5 BTC à Bob",
    "Tx₂": "Bob envoie 0.2 BTC à Carol",
    "Tx₃": "Carol envoie 0.1 BTC à Dave",
    "Tx₄": "Dave envoie 0.05 BTC à Alice"
}

feuilles = {tx: hashlib.sha256(data.encode('utf-8')).hexdigest() for tx, data in transactions.items()}
niveau1 = [feuilles["Tx₁"], feuilles["Tx₂"], feuilles["Tx₃"], feuilles["Tx₄"]]
niveau2 = [
    hashlib.sha256((niveau1[0] + niveau1[1]).encode('utf-8')).hexdigest(),
    hashlib.sha256((niveau1[2] + niveau1[3]).encode('utf-8')).hexdigest()
]
root = hashlib.sha256((niveau2[0] + niveau2[1]).encode('utf-8')).hexdigest()

print("Niveau intermédiaire :", niveau2)
print("Merkle Root :", root)