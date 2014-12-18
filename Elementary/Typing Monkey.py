__author__ = 'Thuan'

def count_words(sentence, check):
    count =0
    sentence = sentence.lower()
    for word in check:
        if word in sentence:
            count+=1


    return count
print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
