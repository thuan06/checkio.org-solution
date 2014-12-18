__author__ = 'Thuan'
def find_message(text):
    s=''.join([i for i in text if i.isupper()])
    return str(s)
print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
