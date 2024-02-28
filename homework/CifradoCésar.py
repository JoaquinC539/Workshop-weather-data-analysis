extended_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm'
numbers = '0123456789'
def ROT13():

    entry = input('Chose a message to encrypt:\n')
    if numbers in entry:
        return 'This function does not support numbers'
    entry = entry.lower()
    index_list = []
    for letter in entry:
        position = extended_alphabet.index(letter)
        index_list.append(position)
    
    extended_alphabet_alias = extended_alphabet
    counter = -1
    result = ''
    for index in index_list:
        if index + 13 > len(extended_alphabet_alias):
            extended_alphabet_alias = extended_alphabet + extended_alphabet[counter + 1]
            continue
        x = extended_alphabet[index + 13]
        result += x
    
    return result