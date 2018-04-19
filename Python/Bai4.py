class SinhVien:
    MSSV=""
    HoTen=""
    MaKhoa=""
    count=0
    def __init__(self,MSSV,HoTen,MaKhoa):
        self.MSSV = MSSV
        self.HoTen = HoTen
        self.MaKhoa = MaKhoa
        SinhVien.count += 1
    def getMSSV(self):
        return self.MSSV
    def getHoTen(self):
        return self.HoTen
    def getMaKhoa(self):
        return self.MaKhoa
    def setMSSV(self,MaSoSV):
        self.MSSV = MaSoSV
    def setHoTen(self,HoTen):
        self.HoTen = HoTen
    def setMaKhoa(self,MaKhoa):
        self.MaKhoa = MaKhoa
    def toString(self):
        print self.MSSV,("\t"),self.HoTen,("\t"),self.MaKhoa

class Khoa:
    MaKhoa=""
    TenKhoa=""
    def __init__(self,MaKhoa,TenKhoa):
        self.MaKhoa = MaKhoa
        self.TenKhoa = TenKhoa
    def getMaKhoa(self):
        return self.MaKhoa
    def getTenKhoa(self):
        return self.TenKhoa
    def setMaKhoa(self,MaKhoa):
        self.MaKhoa = MaKhoa
    def setTenKhoa(self,TenKhoa):
        self.TenKhoa = TenKhoa
    def toString(self):
        print self.MaKhoa,("\t\t"),self.TenKhoa

#Tao Sinh Vien
svList=[]
svList.append(SinhVien("001","Mai A","01"))
svList.append(SinhVien("002","Tran B","01"))
svList.append(SinhVien("003","Van c","02"))
svList.append(SinhVien("004","Thi K","01"))
#Tao Khoa
KhoaList=[]
KhoaList.append(Khoa("01","CNTT"))
KhoaList.append(Khoa("02","Ke Toan"))
KhoaList.append(Khoa("03","Co Khi"))
KhoaList.append(Khoa("04","Nuoi"))

#In ra man hinh 2 bang du lieu tren
print "MSSV\tHo Ten\tMa Khoa"
for i in svList:
    i.toString()
print "Ma Khoa\tTen Khoa"
for i in KhoaList:
    i.toString()
#In ra ds cac sinh vien khoa CNTT
print("Sinh vien khoa CNTT")
for i in svList:
    if(i.getMaKhoa()=="01"):
        i.toString()