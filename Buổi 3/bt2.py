class SieuNhan:
    def __init__(self, name: str, weapon: str, color: str):
        self.name=name
        self.weapon=weapon
        self.color=color
    def __str__(self):
        return (f"Siêu nhân {self.name}  "
                f"Vũ khí: {self.weapon}  "
                f"Màu sắc: {self.color}")
sieu_nhan_A = SieuNhan("A", "Kiếm", "Đỏ")
sieu_nhan_B = SieuNhan("B", "Khiên", "Đen")
print(sieu_nhan_A)
print(sieu_nhan_B)