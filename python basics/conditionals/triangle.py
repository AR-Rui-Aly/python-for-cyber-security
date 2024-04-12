side1 = float(input("enetr the length of side 1: "))
side2 = float(input("enetr the length of side 2: "))
side3 = float(input("enetr the length of side 3: "))

if side1 == side2 == side3:
  print("Equilateral Triangle")

elif side1 == side2 or side1 == side3 or side2 == side3:
  print("Isosceles Triangle")

elif side1 != side2 != side3:
  print("Scalne Triangle")

else:
  print("not a Triangle")
