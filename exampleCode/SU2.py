class SU2:

  "SU2 group elements as matrices."

  __e00=complex(1.,0.)
  __e01=complex(0.,0.)
  __e10=complex(0.,0.)
  __e11=complex(1.,0.)

  def one(self):
    self.__e00=complex(1.,0.)
    self.__e01=complex(0.,0.)
    self.__e10=complex(0.,0.)
    self.__e11=complex(1.,0.)

  def __init__(self):
    pass 

  def setElement(self, i, j, z):
    if i==0 and j==0:
      self.__e00=z+0j
    elif i==0 and j==1:
      self.__e01=z+0j
    elif i==1 and j==0:
      self.__e10=z+0j
    elif i==1 and j==1:
      self.__e11=z+0j
    else:
      print("setElement: ERROR--invalid component.")
      exit(-1)

  def __str__(self):
    return ( f"{self.__e00} {self.__e01}\n" 
            +f"{self.__e10} {self.__e11}"  )

  def __add__(self,other):
    g = SU2()
    g.setElement(0,0,self.__e00+other.__e00)
    g.setElement(0,1,self.__e01+other.__e01)
    g.setElement(1,0,self.__e10+other.__e10)
    g.setElement(1,1,self.__e11+other.__e11)
    return g



g = SU2()
g.setElement(0,0,2)
h = g
s = g + h
print(s)
g.one()
print(g)

g = SU2()
print(g.__e00)
