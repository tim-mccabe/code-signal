def timedReading(maxLength, text):
    # initializing punctuations string  
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    # Removing punctuations in string 
    # Using loop + punctuation string 
    for ele in text:  
        if ele in punc:  
            text = text.replace(ele, "") 
    c = 0
    l = text.split()
    print(l)
    for i in l:
        if len(i) <= maxLength:
            c += 1
    return c