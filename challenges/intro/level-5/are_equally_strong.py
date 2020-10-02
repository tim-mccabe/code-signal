def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = max(yourLeft, yourRight)
    friend = max(friendsLeft, friendsRight)
    a = min(yourLeft, yourRight)
    b = min(friendsLeft, friendsRight)
    return you == friend and a == b