import re

def count(sentence):
    l_vowels = len(re.findall('[aeiou]', sentence))
    u_vowels = len(re.findall('[AEIOU]', sentence))
    l_consonants = len(re.findall('[bcdfghjklmnpqrstvwxyz]', sentence))
    u_consonants = len(re.findall('[BCDFGHJKLMNPQRSTVWXYZ]', sentence))
    numbers = len(re.findall('[0-9]', sentence))
    others = len(sentence) - (l_vowels + u_vowels + l_consonants + u_consonants + numbers)

    return {
        'l_vowels': l_vowels,
        'u_vowels': u_vowels,
        'l_consonants': l_consonants,
        'u_consonants': u_consonants,
        'numbers': numbers
    }
while True:
    sentence = input("Enter the sentence ('q' to quit) >>>\n")
    if sentence == '':
        print("Type some text to count...")
    elif sentence == 'q':
        print('Thank you for using the program')
        break
    else:
        result = count(sentence)
        print(f"Lowercase Vowels: {result['l_vowels']}\n"
              f"Uppercase Vowels: {result['u_vowels']}\n"
              f"Lowercase Consonants: {result['l_consonants']}\n"
              f"Uppercase Consonants: {result['u_consonants']}\n"
              f"Numbers: {result['numbers']}\n")

