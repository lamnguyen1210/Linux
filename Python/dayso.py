n = input("Nhap n:")
#a) In ra man hinh day so tu 1 -> n
for i in range (n):
   print i+1
#b) Tinh tong cac phan tu chan cua day
s=0
for i in range (n):
   if((i+1) % 2 ==0):
      s=s+i+1
print "Tong cac phan tu chan cua day: ",s

