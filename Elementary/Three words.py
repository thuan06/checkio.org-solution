__author__ = 'Thuan'
def threeword(text):
    words=list(text.split(' '))
    c=0
    for word in words:
        if word.isalpha():
            c+=1
            if c==3:
                return True
        else:
            c=0
    return False
print threeword("He is 123 man")