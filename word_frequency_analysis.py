def word_frequency(text):
    zmensenie = text.lower()
    lst = []
    empty = ""
    for words in zmensenie:
        if words.isalpha():
            empty += words
        else:
            if empty:
                lst.append(empty)
                empty = ''
    if empty:  
        lst.append(empty)

    dictionary = {}
    for word in lst:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

# testy (upravujte dle libosti)
print(word_frequency("Ksi, Ksa, Ksi, Kse"))       # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Ksi,+Ksa,Ksi;;-;Kse_"))     # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Informatika je nejlepsi"))  # {'informatika': 1, 'je': 1, 'nejlepsi': 1}
