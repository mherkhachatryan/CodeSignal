"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""

def adjacentElementsProduct(inputArray):
   prodlist = []
   for i in range(len(inputArray)-1):
      production =  inputArray[i]*inputArray[i+1]
      prodlist.append(production)
   result = max(prodlist)
   return result

