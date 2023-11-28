
def encode(n: int, plain_text: str) -> str:
    rozklad = []
    for letter in plain_text:
            rozklad.append(letter)
    empty = []
    for i in range(len(rozklad)):
          skupiny = rozklad[i:(i+n)]
          empty.append(skupiny)
    zoskupenia = empty[0:(len(empty)):n]
    for i in range(len(zoskupenia)):
          zoskupenia[i].reverse()
    words_list = [''.join(inner_list) for inner_list in zoskupenia]
    word = ''.join(words_list)
    return word
def decode(n: int, cipher_text: str) -> str:
    rozkla = []
    for lette in cipher_text:
            rozkla.append(lette)
    empt = []
    for i in range(len(rozkla)):
          skupin = rozkla[i:(i+n)]
          empt.append(skupin)
    zoskupeni = empt[0:(len(empt)):n]
    for i in range(len(zoskupeni)):
          zoskupeni[i].reverse()
    word_list = [''.join(inner_list) for inner_list in zoskupeni]
    wor = ''.join(word_list)
    return wor


print(encode(3, "Ahoj"))    # ohAj
print(encode(2, "Ahoj"))    # hAjo
print(encode(10, "Ahoj"))   # johA
print(encode(3, "12345"))   # 32154
print(encode(5, "komunikace"))  # numokecaki
print(decode(2, "hAjo"))    # Ahoj
print(decode(5, "rgorpavomain"))    # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane
