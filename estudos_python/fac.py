def FirstFactorial(num):
  n = num
  while n > 1:
    n -= 1
    num = num*n

  # code goes here
  return num

# keep this function call here 
print(FirstFactorial(8))