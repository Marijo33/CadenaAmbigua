import utils 

def write_nud(c,z,k,v,w1,w2,cad_1,cad_2):
  aux = list(z)
  a = set(utils.cos_l1l2(c,aux[-1]))
  b = set(utils.cos_l1l2(aux[-1],c))
  aux.append(a|b)
  
  nom_archivo = "out.txt"
  archivo = open(nom_archivo, "w")

  

  archivo.write("EL CODIGO C =" + str(c) + "\n")
  archivo.write("\n")
  archivo.write("METODO DE PATTERSON-SARDINAS\n")
  
  #pasos pa el analisis si el codigo es univocamente decodificable o no
  i = 0
  for elem in aux:
    archivo.write("S"+str(i)+":\n")
    archivo.write(str(elem)+"\n")
    archivo.write("\n")
    i+=1


  
  #Pasos para determinar los valores de k y v
  k = k[::-1]
  v = v[::-1]
  n = len(k)
  
  archivo.write("k" +str(n)+ " = v" + str(n) +" = "+k[-1] +"\n")
  for i in range(n-1,0,-1):
    #Caso 1 (en la operación C/S)
    if(v[i-1]+v[i]==k[i-1]):
      archivo.write(v[i] + " pertenece S"+str(i)+ ", porque v" +str(i-1) +"=" + v[i-1] + " pertenece " + " S" + str(i-1)+ " y k"+str(i-1)+ "="+k[i-1]+ " pertenece C ,en la operación C/S"+str(i-1) +"\n")
    #Caso 2 (en la operación C/S)
    else:
      archivo.write(str(v[i]) + " pertenece S"+str(i)+ ", porque v" +str(i-1) +"=" + v[i-1] + " pertenece " + " S" + str(i-1)+ " y k"+str(i-1)+ "="+k[i-1]+ " 
      pertenece C, en la operación S"+str(i-1)+"/C\n")



  archivo.write("\n")
  archivo.write("\n")
  archivo.write("GENERANDO LA CADENA AMBIGUA\n")

  
  #Pasos para generar la cadena ambigua
  archivo.write("\n") 
    
  archivo.write("cadena 1 = "+ " ".join(cad_1) +" = " + "".join(w1)+"\n")
  archivo.write("cadena 2 = "+" ".join(cad_2) + " = "+"".join(w2)+"\n")

  
  archivo.close()

def write_ud(c):
  nom_archivo = "out.txt"
  archivo = open(nom_archivo, "w")

  archivo.write("EL CODIGO C =" + str(c) + " ES U.D\n")
  archivo.write("\n")
  archivo.close()
