def find_max_number (num1, num2, num3):
   if num1>=num2 and num1>=num3:
      return num1
   elif num2>=num1 and num2>=num1:
      return num2
   else:
      return num3

def find_mean_std (x1, x2, x3):
    mean = (x1 + x2 +x3) / 3
    variance_std= (((x1-mean)**2 + (x2-mean)**2 + (x3-mean)**2) / 3)**0.5
    return mean, variance_std
