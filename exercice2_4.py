import hashlib 
transactions = {
    "Tx₁": "Alice envoie 0.5 BTC à Bob",
    "Tx₂": "Bob envoie 0.2 BTC à Carol",
    "Tx₃": "Carol envoie 0.1 BTC à Dave",
    "Tx₄": "Dave envoie 0.05 BTC à Alice"
}

feuilles = {tx: hashlib.sha256(data.encode('utf-8')).hexdigest() for tx, data in transactions.items()}
H3 = feuilles["Tx₃"]
H33 = hashlib.sha256((H3 + H3).encode('utf-8')).hexdigest()  # duplication

print("H₃₃ =", H33)