import math, sys

class SU3:

  "SU3 group elements as matrices"

  def one(self):
    self.e00=complex(1.,0.)
    self.e01=complex(0.,0.)
    self.e02=complex(0.,0.)
    self.e10=complex(0.,0.)
    self.e11=complex(1.,0.)
    self.e12=complex(0.,0.)
    self.e20=complex(0.,0.)
    self.e21=complex(0.,0.)
    self.e22=complex(1.,0.)

  def __init__(self):
    self.one()

  def setElement(self, i, j, z):
    if i==0 and j==0:
      self.e00=z
    elif i==0 and j==1:
      self.e01=z
    elif i==0 and j==2:
      self.e02=z
    elif i==1 and j==0:
      self.e10=z
    elif i==1 and j==1:
      self.e11=z
    elif i==1 and j==2:
      self.e12=z
    elif i==2 and j==0:
      self.e20=z
    elif i==2 and j==1:
      self.e21=z
    elif i==2 and j==2:
      self.e22=z
    else:
      print("setElement: ERROR--invalid component.")
      sys.exit(-1)

  def printMatrix(self):
    print(self.e00, self.e01, self.e02)
    print(self.e10, self.e11, self.e12)
    print(self.e20, self.e21, self.e22)

  def __add__(self,other):
    h = SU3()
    h.setElement(0,0,self.e00+other.e00)
    h.setElement(0,1,self.e01+other.e01)
    h.setElement(0,2,self.e02+other.e02)
    h.setElement(1,0,self.e10+other.e10)
    h.setElement(1,1,self.e11+other.e11)
    h.setElement(1,2,self.e12+other.e12)
    h.setElement(2,0,self.e20+other.e20)
    h.setElement(2,1,self.e21+other.e21)
    h.setElement(2,2,self.e22+other.e22)
    return h



g = SU3()
g.one()
h = SU3()
h.one()
s=g+h
s.printMatrix()
