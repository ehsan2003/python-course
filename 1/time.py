t = int(input("enter t value for time :"))

h = t // 3600
s = t % 60
m = ( t//60 ) % 60

print(h,m,s)
