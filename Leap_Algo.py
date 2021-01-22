if (year % 4) == 0:
  if(year % 100) != 0:
    print("This is a Leap Year")
  elif(year % 400) == 0:
    print("This is a Leap Year")
else:
  print("This is not a leap year")
