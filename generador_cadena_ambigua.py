
def generar(k,v,c):
  k = k[::-1]
  v = v[::-1]
  n = len(k)-1

  cad_1 = []
  cad_1.append(k[0])
  cad_2 = []
  cad_2.append(v[0])
  cad_2.append(k[1])

  for i in range(1,n):
    #caso 1  Si vi=ki·vi+1
    if(v[i] == k[i]+v[i+1]):
      # añadir la subcadena ki+1 al final de la cadena que contenga ki.
      if(k[i] == cad_1[-1]):
        cad_1.append(k[i+1])
      else:
        cad_2.append(k[i+1])

    #caso 2 Si ki=vi·vi+1
    if(k[i] == v[i]+v[i+1]):
      #añadir la subcadena ki+1 al final de la cadena que no contenga ki
      if(k[i] == cad_1[-1]):
        cad_2.append(k[i+1])
    
      else:
        cad_1.append(k[i+1])

  w1=[]
  w2=[]
  
  for i in range(len(cad_1)):
    w1.append("w"+str(c.index(cad_1[i])+1)+" ")

  for i in range(len(cad_2)):  
    w2.append("w"+str(c.index(cad_2[i])+1)+" ")

  return cad_1,cad_2,w1,w2
  
  
  

