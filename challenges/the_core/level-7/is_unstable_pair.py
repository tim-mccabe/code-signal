def isUnstablePair(filename1, filename2):
    if filename2 > filename1:
        return filename2.upper() < filename1.upper()
    elif filename2 < filename1:
        return filename2.lower() > filename1.lower()
    else:
        return False