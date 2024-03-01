X,Y=map(int,input().split())
number_min=min(abs(X), abs(Y))
number_max=max(abs(X), abs(Y))
print(number_max%number_min)
