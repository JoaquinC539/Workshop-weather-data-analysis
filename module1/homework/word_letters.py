def main():
    letters = {}
    msg = user_input()
    select_letters(letters, msg)
    print('Count of charcters:\n')
    for key in letters:
        print(key+'            ' + str(letters[key]))

def user_input():
    result = input('Select a message to count:\n')
    return result

def select_letters(dict, message):
    for letter in message:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict

if __name__ == '__main__':
    try:
        main()
        print('')

    except Exception as error:
        print('There was an error:', error)
    finally:
        print('Goodbye!')