
def def_k_v(z):
  k=[]
  v=[]

  #determinamos los primeros valores de los vectores k y n
  for elem in z[len(z)-1]:
    if elem in z[0]:
      k.append(elem)
      v.append(elem)

  n = len(z)-2

  j = 0
  sw =True  #variable para ver que caso elejir 
  for i in range(n,-1,-1):
    sw=True

    #Primer caso  (en la operación C/Sn) para definir   
    for elem in z[i]:
      if(elem+v[j] in z[0]):
        k.append(elem+v[j])
        v.append(elem)
        sw = False
        break

    #Segundo caso (en la operación Sn/C)
    if(sw):
      for elem in z[0]:
        if(elem+v[j] in z[i]):
          k.append(elem)
          v.append(elem+v[j])
          break

        
    j = j+1

      #elemento dividido entre z[n-1]

  return k,v