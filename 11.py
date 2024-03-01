import math
a,b,c=map(float,input().split())
alpha=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
beta=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
print(alpha, beta, 180-alpha-beta)
