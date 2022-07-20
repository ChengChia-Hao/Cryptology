int_val = 1234
str_val = 'h'
float_val = 12.04

tuple_val = (1, 2, 3, 4, 5)

list_val = [1, 2, 3, 4, 5]

print('Inteager hash : '+str(hash(int_val)))
print('String hash : '+str(hash(str_val)))
print('String hash PURE : ' , (hash(str_val)))
print('Float hash : '+str(hash(float_val)))
print('Tuple hash : '+str(hash(tuple_val)))
# print('List hash : '+str(hash(list_val)))