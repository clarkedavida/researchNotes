#!/bin/python3

def countLines(filename):
  file = open(filename,'r')
  nlines = 0
  for line in file:
    nlines += 1
  file.close()
  return nlines
