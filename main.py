def leaf(year):
  if(year % 4== 0 and year % 100 !=0) or year % 400 == 0:
    return True
  else:
    return False

year=int(input("Enter the Year : "))
if leaf(year):
  print("is Leaf Year: {} ".format(year))
else:
  print("is not a Leaf Year : {} ".format(year))