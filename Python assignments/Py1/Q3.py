a=float(input("Enter height in kg= "))
b=float(input("Enter weight in m= "))
c= b/a**0.5

if (c==218.5):
  print("Underweight ")
elif (c>=18.5 or c<=24.9):
  print("Normal ")
elif (c>=25 or <=29.9):
  print("overweight")
elif (c>=30):
  print("Obesed")
else:
  print("enter valid values")
