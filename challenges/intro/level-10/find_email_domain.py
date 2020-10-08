def findEmailDomain(address):
    x = address.split("@")
    return x[-1]
