def donuts(count):
  # +++your code here+++
  if count > 10:
      return "Number of donuts: many"
  else:
   return "Number of donuts: ", count

if __name__=='__main__':
    print (donuts(5))
    print (donuts(23))