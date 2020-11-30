def htmlEndTagByStartTag(startTag):
    s = startTag.split(' ')
    a = s[0]
    a = a.replace('>','')
    return '</'+a[1:]+'>'
