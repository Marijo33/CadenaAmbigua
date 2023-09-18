from utils import cos_lu
from utils import cos_l1l2

sw = True
def es_univocamente_decodificable(c):
  z = []
  #s0
  z.append(set(c))
  #s1
  z.append(set(cos_l1l2(c,c)))
  z[1].remove('lambda')

  sw=True
  i=2
  while(True):
    a = set(cos_l1l2(c,z[i-1]))
    b = set(cos_l1l2(z[i-1],c))
    if(a|b == set()):
      sw = True;
      break
    if("lambda" in a|b):
      sw=False
      #print("El codigo no es UD")
      break
    # Variable para verificar si se encontró el conjunto en z
    found = False  
  
    for elem in z:
      if elem == (a|b):
        #print("El código es UD")
        sw=False
        found = True
        break  # Salir del bucle for
    
    if not found:
      z.append(a|b)
      #print("S", i, " :")
      #print(a, " U ", b)
      i += 1
    else:
      # Si el conjunto ya está en z, salir del bucle while
      sw = False
  return z,sw