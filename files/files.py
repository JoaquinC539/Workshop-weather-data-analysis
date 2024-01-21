# import os

from os import path

x=5
# r = READ
# a = append
#  w = write
# x = create

############## READ OPERATION ############

# try:
    # fnames= open('nombres.txt','r')
#     text=fnames.read()
#     print(text)
#     # for line in text:
#     #     print(line)
   
    
# except Exception as error:
#     print(f'Hubo un error: {error}')
# finally:
#     fnames.close()

############## APPEND OPERATION ############

# try:
#     fnames2 = open('nombres2.txt', 'a')
#     fnames2.writelines(["\nJames","\nPeter",'Homer'])
#     fnames2.close()
#     fnames2=open('nombres2.txt','r')
#     print(fnames2.read())
# except OSError:
#     print(f'Hubo un error: {OSError}')
# finally:
#     fnames2.close()

############## WRITE OPERATION ############

# try:
#     context = open('context.txt', 'w')
#     context.write('I deleted the context')
#     context.close()
#     context=open('context.txt','r')
#     print(context.read())
#     pass
# except OSError:
#     print(f'Error was: {OSError}')
# finally:
#     context.close()

############## CREATE OPERATION ############

try:
    # fDiary=path.exists('./daniDiary.txt')
    if not path.exists('./daniDiary.txt'):
        fDiary=open('daniDiary.txt', 'x')
        fDiary.write('Soy el diario')
        fDiary.close()
    else:
        fDiary=open('daniDiary.txt','w')
        fDiary.write('Ya existe el diario')
        fDiary.close()
   
except Exception:
    print(f'Error was: {Exception}')

