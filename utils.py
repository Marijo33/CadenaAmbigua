def cos_lu(l,u):
  l=list(l)
  c=[]
  for elem in l:
    if(len(u) < len(elem)):
      if(elem[0:len(u)] == u):
        c.append(elem[len(u):len(elem)])
    elif((len(u)==len(elem))and(elem==u)):
      c.append("lambda")
  return c


def cos_l1l2(l1,l2):
  l1 = list(l1)
  l2 = list(l2)
  c = []
  for elem_l2 in l2:
    c = c + cos_lu(l1,elem_l2)
  return(c)


def cos_u1u2(u1,u2): #(u1 /u2)
 
  c=""
  if(len(u2) < len(u1)):
    if(u1[0:len(u2)] == u2):
      c+=(u1[len(u2):len(u1)])
  return c
