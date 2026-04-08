class SieuNhan:
    def __init__(self, name: str, weapon: str, color: str):
        self.name=name
        self.weapon=weapon
        self.color=color
    def __str__(self):
        return (f"Siêu nhân {self.name}  "
                f"Vũ khí: {self.weapon}  "
                f"Màu sắc: {self.color}")
danh_sach = []
print("=== NHẬP DANH SÁCH SIÊU NHÂN ===")
print("(Nhấn Enter để kết thúc)\n")

while True:
    name = input("Tên siêu nhân: ")
    if name == "":
        break
    weapon = input("Vũ khí: ")
    color = input("Màu sắc: ")
    danh_sach.append(SieuNhan(name, weapon, color))
    print(f"  → Đã thêm {name}!\n")
print(f"\n=== DANH SÁCH {len(danh_sach)} SIÊU NHÂN ===")
for i, sn in enumerate(danh_sach, 1):
    print(f"{i}.", sn)