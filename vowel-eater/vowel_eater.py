user_word = input('Hey! please enter a word you like: ')

user_word = user_word.upper()

word_without_vowels = ''

for char in user_word:

    if char == 'A':
        continue
    elif char == 'E':
        continue
    elif char == 'I':
        continue
    elif char == 'O':
        continue
    elif char == 'U':
        continue
    else:
        word_without_vowels += char
    
print(word_without_vowels)



