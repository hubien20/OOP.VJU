class ConCho:
    def __init__(self, name, color, breed, emotion):
        self.name=name
        self.color=color
        self.breed=breed
        self.emotion=emotion
    def bark(self):
        print(f"{self.name}: Gâu gâu!")
    def wagtail(self):
        print(f"{self.name} đang vẫy đuôi")
    def eat(self, food):
        print(f"{self.name} đang ăn {food}.")
    def run(self, speed):
        print(f"{self.name} đang chạy với tốc độ {speed} km/h")
class OTo:
    def __init__(self, brand, size, color, prize):
        self.brand=brand
        self.size=size
        self.color=color
        self.prize=prize
        self.speed=0
    def speed_up(self, add):
        self.speed += add
        print(f"Xe đang tăng tốc. Tốc độ hiện tại: {self.speed} km/h")
    def slow_down(self, minus):
        self.speed = max(0, self.speed - minus)
        print(f"Xe đang giảm tốc. Tốc độ hiện tại: {self.speed} km/h")
    def crash(self):
        print(f"Xe {self.brand} đã đâm.")
        self.speed = 0
class TaiKhoan:
    def __init__(self, name, account_number, bank, balance=0):
        self.name = name
        self.account_number = account_number
        self.bank = bank
        self.__balance = balance
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Rút {amount:,} VNĐ. Số dư còn: {self.__balance:,}")
        else:
            print("Số dư không đủ.")
    def deposit(self, amount):
        self.__balance += amount
        print(f"Đã gửi {amount:,} VNĐ. Số dư mới: {self.__balance:,}")

    def check_balance(self):
        print(f"[{self.name}] Số dư: {self.__balance:,} VNĐ")
cho = ConCho("Milo", "vàng", "Golden Retriever", "Vui")
cho.bark(); cho.eat("xương")

xe = OTo("BMW", "sedan", "trắng", 800_000_000)
xe.speed_up(60); xe.speed_up(40); xe.slow_down(30)

tk = TaiKhoan("Nguyễn A", "123456789", "Techcombank", 5_000_000)
tk.deposit(2_000_000); tk.withdraw(10_000_000); tk.check_balance()