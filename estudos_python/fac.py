def FirstFactorial(num):
  n = num

  while n > 1:
    n -= 1
    num = num*n

  # code goes here
  return num

def lu(roda):
  if roda <= 10:
    print('Roda é menor ou igual a 10')

  elif roda <= 20:
    print('Roda é menor que 20 e maior que 10')

  else: 
    print('Roda é maior que 20')

# keep this function call here 
print(FirstFactorial(8))

#lu('Oi')

