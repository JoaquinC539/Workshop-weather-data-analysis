from pprint import pprint
my_dict={'valor1':10,'valor2':20,'valor3':30,'nested':{'valor4':40,'valor5':50}, 'list':[3,4,5]}
pprint(my_dict['list'])
my_dict['list2']=[6,7,8]
my_dict.pop('valor2')

for (key) in my_dict:
    print(key)
    print(my_dict[key])
