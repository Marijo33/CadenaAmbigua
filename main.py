from univocamente_decodificable import es_univocamente_decodificable
from generador_cadena_ambigua import generar
import ambiguedad
import read
import write

c = read.read("./in.txt")
z ,sw= es_univocamente_decodificable(c)

#Si el codigo es UD
if(sw):
  print("El codigo es U.D por lo tanto no existe cadena ambigua")
  write.write_ud(c)
  
#El codifp no es UD por lo tanto hallamos cadena ambigua
else:
  print('El codigo no es U.D')
  #determinamos la cadena ambigua
  k,v = ambiguedad.def_k_v(z)
  cad_1,cad_2,w1,w2=generar(k,v,c)

  #El resultado y los pasos que se siguieron se guardan en el archivo out.txt
  write.write_nud(c,z,k,v,w1,w2,cad_1,cad_2)
  print("" .join(cad_1))
  print("".join(cad_2))

  








    

  
  
  

