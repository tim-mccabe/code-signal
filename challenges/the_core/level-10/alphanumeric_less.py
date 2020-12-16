def alphanumericLess(s1, s2):
    return tokenize(s1) < tokenize(s2)


def tokenize(s):
    tokens = re.findall('\d+|.', s)
    return (
        [
            (0, int(token)) if token.isdigit() else (1, token)
            for token in tokens
        ],
        [-len(token) for token in tokens]
    )