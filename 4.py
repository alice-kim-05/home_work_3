X,Y,N=map(int,input().split())
K=(Y*N)%100
R=X*N+(Y*N)//100
print(R,'руб.',K,'коп.')
