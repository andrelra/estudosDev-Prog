obj = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(obj))
#print('Só tem espaço? ', obj.isspace())
#print('É um número? ', obj.isnumeric())
#print('É alfabético? ', obj.isalpha())
#print('É alfanumérico? ', obj.isalnum())
#print('Está em maiúscula? ', obj.isupper())
#print('Está em minúscula? ', obj.islower())
#print('Está capitalizada? ', obj.istitle())

print('Tipo Primitivo: {}; Só tem espaço? {}; É um número? {}; É alfabético? {}; É alfanumérico? {}; Está em maiúscula? {}; Está em minúscula? {}; Está capitalizada? {}.' .format(type(obj), obj.isspace(), obj.isnumeric(), obj.isalpha(), obj.isalnum(), obj.isupper(), obj.islower(), obj.istitle()))
