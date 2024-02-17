# print(__name__)
greeting = {
        'Spanish': 'Hola',
        'English': 'Hello',
        'German': 'Hallo'
    }
def say_hello(name, lang):
    
    message = f'{greeting[lang]} {name}!'
    return message

if __name__ == "__main__":

    import argparse
    
    x = []
    for  element in greeting:
        x.append(element)

    parser = argparse.ArgumentParser(
        description ="Return a greeting"
    )

    parser.add_argument(
        "-n","--name", metavar = "name",
        required = True, help = "The name of the person to greet"
    )
    
    parser.add_argument(
        '-l', '--language', '--lang', metavar = 'language',
        required = True, help = 'The language selction',
        choices = x
    )
    args=parser.parse_args()

    print(say_hello(args.name,args.language))
