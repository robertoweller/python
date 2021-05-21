def recursao(lista, p=0, n=0):
  
  n += lista[p]
  p += 1
  
  if len(lista) == p:
    
    return n
  
  else:
    return recursao(lista, p, n)
  
print(recursao([1, 5, 8]))