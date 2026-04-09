class NhanVien:
    Luong_Max = 50_000_000
    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong):
        self.__tenNhanVien=ten_nhan_vien
        self.__luongCoBan=luong_co_ban
        self.__heSoLuong=he_so_luong
    def getTenNhanVien(self):
        return self.__tenNhanVien
    def getLuongCoBan(self):
        return self.__luongCoBan
    def getHeSoLuong(self):
         self.__heSoLuong
    def setTenNhanVien(self, value):
        self.__tenNhanVien = value
    def setLuongCoBan(self, value):
        if value < 0:
            print ("Lương không được âm")
            return 
            self.__luongCoBan=value
    def setHeSoLuong(self, value):
        if value <= 0:
            print ("Hệ số lương phải > 0")
            return
            self.__heSoLuong=value
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong
    def inTTin(self):
        luong = self.tinhLuong()
        print("============== Thông tin nhân viên ================")
        print(f"Tên: {self.__tenNhanVien}")
        print(f"Lương cơ bản: {self.__luongCoBan:,.0f} VNĐ")
        print(f"Hệ số lương: {self.__heSoLuong:.1f}")
        print(f"Lương thực tế: {luong:,.0f} VNĐ")
        print("===================================================")
    def tangLuong(self, delta):
        he_so_luong_moi = self.__heSoLuong + delta
        luong_moi = self.__luongCoBan * he_so_luong_moi
        if luong_moi > NhanVien.Luong_Max:
            print(f"Lương mới ({luong_moi:,.0f} VNĐ) vượt Luong_Max. Không tăng!")
            return False
        self.__heSoLuong = he_so_luong_moi
        print(f"Đã tăng lương! Lương mới: {self.tinhLuong():,.0f} VNĐ")
        return True
nv = NhanVien("Nguyễn Văn A", 10_000_000, 3.0)
nv.inTTin() 
print("\n--- Test tăng lương ---")
nv.tangLuong(0.5)
nv.inTTin()
nv.tangLuong(2.0)
print("\n--- Test getters và setters ---")
print("Tên nhân viên:", nv.getTenNhanVien())
nv.setLuongCoBan(12_000_000)
print("Lương cơ bản mới:", nv.getLuongCoBan())
print("lương thực tế mới:", nv.tinhLuong())