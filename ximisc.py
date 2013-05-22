## this file contains miscellaneous useful functions.

import numpy as np
import matplotlib.pyplot as plt
import sys
import copy

def downsample1dsum(a,dfac):
  adown = []
  for i in range(len(a)/dfac):
    aval = (a[i*dfac:(i+1)*dfac]).sum()
    adown.append(aval)
  adown = np.array(adown)
  return adown


def downsample1d(a,dfac):
  adown = []
  for i in range(len(a)/dfac):
    aval = (a[i*dfac:(i+1)*dfac]).sum()
    adown.append(aval)
  adown = np.array(adown)
  adown = adown/float(dfac)
  return adown

def legendre(n,x):
  if(n==0):
    return 1
  if(n==1):
    return x
  if(n==2):
    return 0.5*(3.*x**2-1.)
  if(n==3):
    return 0.5*(5.*x**3 -3.*x)
  if(n==4):
    return 0.125*(35.*x**4 -30.*x**2 + 3.)
  if(n>4 or n<0):
    sys.exit(1)

def one2twod(a,b):
  a2d = np.zeros([len(a), len(b)])
  b2d = np.zeros([len(a), len(b)])
  for i in range(len(a)):
    a2d[i,:] = a[i]
    b2d[i,:] = b

  return a2d, b2d

## generate comparison to see if two results are close (enough).
#these can be any form of xi/wp/xiell, as long as they have the same.
def comparexi(xia, xib,maxfrac=1.e-4,maxdiff=1.e-4):
  """
  maxdiff is the maximum absolute difference allowed.
  maxfrac is maximum fractional deviation tolerated (unless diff less than maxdiff)
  Returns 0 if they're the same.
  Returns 1 if they disagree.
  Returns 2 if they have different shapes.
  """
  xi1 = xia.flatten()
  xi2 = xib.flatten()
  if len(xi1) != len(xi2):
    return 2
  xx = np.where(np.fabs((xi1-xi2)/xi1) > 1.e-4,1,0)
  yy = np.where(np.fabs(xi1-xi2) > 1.e-4,1,0)
  zz = (xx & yy)

  if (zz != 0).any():
    return 1
  else:
    return 0

