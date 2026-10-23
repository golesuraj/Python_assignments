s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))
if s1 == s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
