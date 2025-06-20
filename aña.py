
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip() 
    words = morse_code.split('  ') 
    decoded_words = []
    
    for word in words:
        letters = word.split() 
        decoded_word = ''.join(MORSE_CODE[letter] for letter in letters)
        decoded_words.append(decoded_word)
        
    return ' '.join(decoded_words)

def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(
        min(max(r, 0), 255),
        min(max(g, 0), 255),
        min(max(b, 0), 255)
    )

