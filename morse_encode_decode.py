import string

translation_dict = dict([('a', '.-'), ('t', '-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'), ('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'), ('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'), ('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'), ('y', '-.--'), ('z', '--..'), (' ', ''), ('/', '-..-.'), ('-', '-....-'), ('.', '.-.-.-'), (',', '--..--'), ("1", ".----"), ("2", "..---"), ("3", "...--"), ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."), ("9", "----."), ("0", "-----")])

alphabet = {}
morse = {}

for key, value in translation_dict.items():
    alphabet[key] = value
    morse[value] = key  # Corrected: Use morse dictionary for decoding

def encode(plaintext: str) -> str:
    plaintext = plaintext.lower()
    morse_text = ""
    for char in plaintext:
        if char in alphabet:
            morse_text += alphabet[char] + "/"
    morse_text += "//"
    return morse_text

def decode(morse_text: str) -> str:
    morse_array = morse_text.split("/")
    plain_text = ""
    for i in range(len(morse_array)):
        current_element = morse_array[i]
        if current_element in morse:
            plain_text += morse[current_element]
    return plain_text



print(encode("abcdefghijklmnopqrstuvwxyz0123456789 /.,-?!"))
print(decode(".-/-.../-.-./-.././..-./--./..../../.---/-.-/.-../--/-./---/.--./--.-/.-./.../-/..-/...-/.--/-..-/-.--/--../-----/.----/..---/...--/....-/...../-..../--.../---../----.//-..-./.-.-.-/--..--/-....-///"))