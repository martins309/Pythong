
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True


def pos_neg(a, b, negative):
  posA = a > 0
  negA = a < 0
  posB = b > 0
  negB = b < 0
  
  if(posA and negB) or (negA and posB):
    return True
  elif(posA and negB) and negative == True:
    return True
  else: 
    return False



  #     if(posA and negB) or (negA and posB):
  #   return True
  # elif(posA and negB) and negative == True:
  #   return True
  # elif(negA and posB) and negative == True:
  #   return True
  # elif(negA and negB) and negative == True:
  #   return True
  # else: 
  #   return False






