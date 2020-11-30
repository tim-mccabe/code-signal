def permutationCipher(password, key):
    table = {ord('a') + i : ord(k) for i, k in enumerate(key)}
    return password.translate(table)
