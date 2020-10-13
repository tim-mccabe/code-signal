def longestWord(text):
    a = re.split('[^a-zA-Z]',text)
    w = a[0]
    l = len(a[0])
    for i in a:
        if l < len(i):
            l = len(i)
            w = i
    return w 