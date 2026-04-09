class CanBo:
    def __init__(self, name, age, sex, address):
        self._name=name
        self._age=age
        self._sex=sex
        self._address   = address
    def loai_cb(self):
        return "Cán bộ"
    def hien_thi(self):
        print(f"  Họ và tên : {self._name}")
        print(f"  Tuổi      : {self._age}")
        print(f"  Giới tính : {self._sex}")
        print(f"  Địa chỉ   : {self._address}")
    def __str__(self):
        return f"{self.loai_cb():<10s} | {self._name}"
class CongNhan(CanBo):
    def __init__(self, name, age, sex, address, bac):
        super().__init__(name, age, sex, address)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc phải từ 1 đến 10!")
        self.__bac = bac
    def loai_cb(self):
        return "Công nhân"
    def hien_thi(self):
        print(f"── CÔNG NHÂN ──")
        super().hien_thi()
        print(f"  Bậc       : {self.__bac}")
class KySu(CanBo):
    def __init__(self, name, age, sex, address, nganh_dt):
        super().__init__(name, age, sex, address)
        self.__nganh_dt = nganh_dt
    def loai_cb(self):
        return "Kỹ sư"
    def hien_thi(self):
        print(f"── KỸ SƯ ──")
        super().hien_thi()
        print(f"  Ngành ĐT  : {self.__nganh_dt}")
class NhanVienSX(CanBo):
    def __init__(self, name, age, sex, address, cong_viec):
        super().__init__(name, age, sex, address)
        self.__cong_viec = cong_viec
    def loai_cb(self):
        return "Nhân viên"
    def hien_thi(self):
        print(f"── NHÂN VIÊN ──")
        super().hien_thi()
        print(f"  Công việc : {self.__cong_viec}")
class QLCB:
    def __init__(self):
        self.__ds_can_bo = []
    def them_moi(self):
        print("\n── THÊM CÁN BỘ MỚI ──")
        print("  1. Công nhân")
        print("  2. Kỹ sư")
        print("  3. Nhân viên")
        loai = input("  Chọn loại (1/2/3): ").strip()
        name    = input("  Họ và tên    : ")
        age      = int(input("  Tuổi      : "))
        sex = input("  Giới tính : ")
        address   = input("  Địa chỉ   : ")
        if loai == "1":
            bac = int(input("  Bậc (1-10): "))
            cb = CongNhan(name, age, sex, address, bac)
        elif loai == "2":
            nganh = input("  Ngành ĐT  : ")
            cb = KySu(name, age, sex, address, nganh)
        elif loai == "3":
            cv = input("  Công việc : ")
            cb = NhanVienSX(name, age, sex, address, cv)
        else:
            print("Loại không hợp lệ!")
            return

        self.__ds_can_bo.append(cb)
        print(f"Đã thêm: {cb}")

    def tim_kiem(self):
        tu_khoa = input("\n  Nhập họ tên cần tìm: ").strip().lower()
        ket_qua = [cb for cb in self.__ds_can_bo
                   if tu_khoa in cb._name.lower()]
        if not ket_qua:
            print("  Không tìm thấy!")
        else:
            print(f"  Tìm thấy {len(ket_qua)} kết quả:")
            for cb in ket_qua:
                print()
                cb.hien_thi()

    def hien_thi_ds(self):
        if not self.__ds_can_bo:
            print("\n  Danh sách trống!")
            return
        print(f"\n══ DANH SÁCH CÁN BỘ ({len(self.__ds_can_bo)} người) ══")
        for i, cb in enumerate(self.__ds_can_bo, 1):
            print(f"\n--- #{i} ---")
            cb.hien_thi()

    def chay(self):
        while True:
            print("\n============================")
            print("        QUẢN LÝ CÁN BỘ        ")
            print("==============================")
            print("  1. Thêm mới cán bộ          ")
            print("  2. Tìm kiếm theo tên        ")
            print("  3. Hiển thị danh sách       ")
            print("  4. Thoát                    ")
            print("==============================")

            chon = input("  Lựa chọn: ").strip()

            if   chon == "1": self.them_moi()
            elif chon == "2": self.tim_kiem()
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4":
                print("  Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ!")
if __name__ == "__main__":
    ql = QLCB()
    ql.chay()