a=str(input('Ho ten: '))
b=int(input('So ngay cong: '))
c=int(input('Don gia ngay cong: '))
d=float(input('He so phu cap: '))
e=int(input('Tam ung: '))
Luong=c*b*d
Thuclinh=Luong-e
#round(Luong,1)
#round(Thuclinh,1)
print('Nhan vien',str(a)+str(','),'Co tien Luong='+str(round(Luong,1))+str(','),'Tam ung='+str(int(e)),'va Thuc linh='+str(round(Thuclinh,1)))
