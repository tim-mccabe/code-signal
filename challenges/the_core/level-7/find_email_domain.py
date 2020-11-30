def findEmailDomain(address):
    l = address.split('@')
    return l[-1]