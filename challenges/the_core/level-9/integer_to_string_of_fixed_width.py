def integerToStringOfFixedWidth(number, width):
    s = str(number)
    l = len(s)
    a = list(s)
    if width > l:
        return '0'*(width-l) + s
    if width == l:
        return s
    if width < l:
        x = l - width
        b = a[x:]
        return ''.join(b)