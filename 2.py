time=int(input())
hour=time//3600
minute=(time%3600)//60
second=(time%3600)%60
print('Текущее время: ', hour,'-',minute,'-', second)
