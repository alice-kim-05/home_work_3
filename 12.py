ATT, COMP, YDS,TD,INT=map(float,input().split())
a=(COMP/ATT-0.3)*5
b=(YDS/ATT-3)*0.25
c=(TD/ATT)*20
d=2.375-(INT/ATT*25)
passer_raiting=((a+b+c+d)/6*100)
print(passer_raiting)