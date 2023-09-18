#Obtenbemos el conjunto desde un archivo
def read(txt):
  with open(txt, 'r+') as file:
    c = list(file.read().splitlines())
  return c


  
