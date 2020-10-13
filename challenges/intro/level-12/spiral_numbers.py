def spiralNumbers(n):
    a = [[None] * n for i in range(n)]
    b = [[i + 1, i + 1] for i in reversed(range(n))]
    b = sum(b, [])[1:]
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]] * (int((len(b) + 4) / 4))
    x, y, val = -1, 0, 0
    for steps, (dx, dy) in zip(b, dxdy):
        x, y, val = x + dx, y + dy, val + 1
        for j in range(steps):
            a[y][x] = val
            if j != steps - 1:
                x, y, val = x + dx, y + dy, val + 1
    return a
