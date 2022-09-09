import datetime
hgs = {}
total_balance = {}
dates = set()
class ADMIN():
    @staticmethod
    def total_balance_computer(total_balance):
        for date in dates:
            sum = 0
            for k, v in total_balance.items():
                if k.split()[0] == date:
                    sum += v
            print(f"Date: {date} | Total Revenue: {sum}TL")

    @staticmethod
    def report(hgs):
        for k, v in hgs.items():
            print(f"On {v[0]}, {v[1].capitalize()} {v[2].capitalize()} passed through {v[4].title()} with a Type {v[3]} vehicle.")



class HGS():
    types = [1, 2, 3]
    bridges = ["15 Temmuz Şehitler Köprüsü", "Fatih Sultan Mehmet Köprüsü", "Yavuz Sultan Selim Köprüsü"]
    @staticmethod
    def f(date):
        return date.strftime("%d/%m/%y")
    list1 = [datetime.datetime.strptime("04/05/22", '%d/%m/%y') - datetime.timedelta(days=x) for x in range(3)]
    date_list1 = list(map(f, list1))
    list2 = [datetime.datetime.strptime("09/07/22", '%d/%m/%y') - datetime.timedelta(days=x) for x in range(4)]
    date_list2 = list(map(f, list2))
    list3 = [datetime.datetime.strptime("15/07/22", '%d/%m/%y')]
    date_list3 = list(map(f, list3))
    holidays = date_list1 + date_list2 + date_list3

    def __init__(self, hgs_num, name:str, surname:str, type:int, date_time:str, bridge:str ,available_balance:float):
        assert type in range(1, 4), f"Type {type} should be between 1 and 3."
        assert available_balance >= 0, f"Available Balance {available_balance} should be greater or equal to 0"
        assert bridge in HGS.bridges
        assert len(hgs_num) == 10, f"Your HGS Number must be a 10 digit number."
        self.hgs_num = hgs_num
        self.name = name
        self.surname = surname
        self.type = type
        self.date_time = date_time
        self.bridge = bridge
        self.available_balance = available_balance
        dates.add(self.date_time.split()[0])
        hgs[self.hgs_num] = [self.date_time, self.name, self.surname, self.type, self.bridge]

    def __repr__(self):
        return f"{self.__class__.__name__}(Number : {self.hgs_num}, Type : {self.type})"

    def compute_price(self):
        if self.type == HGS.types[0]:
            if self.bridge != HGS.bridges[-1]:
                self.price = 8.25
                print(f"Price: {self.price}")
            else:
                self.price = 19
                print(f"Price: {self.price}")
        elif self.type == HGS.types[1]:
            if self.bridge != HGS.bridges[-1]:
                self.price = 10.75
                print(f"Price: {self.price}")
            else:
                self.price = 25
                print(f"Price: {self.price}")
        else:
            if self.bridge != HGS.bridges[-1]:
                self.price = 23.25
                print(f"Price: {self.price}")
            else:
                self.price = 46.50
                print(f"Price: {self.price}")

    def apply_discount(self):
        if self.bridge != HGS.bridges[-1]:
            if self.date_time.split()[0] in HGS.holidays:
                self.price = 0
                print(f"Holiday Discount Applied, New Price: {self.price}")
        else:
            print("No Applicable Discounts Available")

    def compute_balance(self):
        self.compute_price()
        self.apply_discount()
        total_balance[self.date_time] = self.price
        self.available_balance -= self.price
        print(f"{self.hgs_num} paid {self.price}. Total Available Balance is {self.available_balance}")

class Type_1(HGS):
    vehicles_1 = []

    def __init__(self, hgs_num, name:str, surname:str, type:int, date_time:str, bridge:str, available_balance:float):
        assert type == 1, f"Type {type} should be 1."
        super().__init__(
            hgs_num, name, surname, type, date_time, bridge, available_balance
        )

        Type_1.vehicles_1.append(self)

class Type_2(HGS):
    vehicles_2 = []

    def __init__(self, hgs_num, name: str, surname: str, type: int, date_time: str, bridge: str,
                 available_balance: float):
        assert type == 2, f"Type {type} should be 2."
        super().__init__(
            hgs_num, name, surname, type, date_time, bridge, available_balance
        )

        Type_2.vehicles_2.append(self)

class Type_3(HGS):
    vehicles_3 = []

    def __init__(self, hgs_num, name: str, surname: str, type: int, date_time: str, bridge: str,
                 available_balance: float):
        assert type == 3, f"Type {type} should be 3."
        super().__init__(
            hgs_num, name, surname, type, date_time, bridge, available_balance
        )

        Type_3.vehicles_3.append(self)

hgs_dene = HGS("1234567890", "doruk", "okur", 1, "05/08/22 11:05:20", "15 Temmuz Şehitler Köprüsü", 125.8)
hgs_dene.__repr__()
hgs_dene.compute_balance()

tip1_dene = Type_1("2345678901", "doga", "okur", 1, "05/08/22 11:05:19", "15 Temmuz Şehitler Köprüsü", 190)
tip1_dene.__repr__()
tip1_dene.compute_balance()
tip1_dene.compute_price()

tip2_dene = Type_2("1111113456", "yigit", "batkı", 2, "03/05/22 11:05:19", "15 Temmuz Şehitler Köprüsü", 125.8)
tip2_dene.__repr__()
tip2_dene.compute_balance()
tip2_dene.compute_price()
tip2_dene.apply_discount()

tip3_dene = Type_3("1234567890", "anancı", "veled", 3, "03/05/22 11:06:19", "Yavuz Sultan Selim Köprüsü", 125.8)
tip3_dene.__repr__()
tip3_dene.compute_balance()
tip3_dene.compute_price()
tip3_dene.apply_discount()

hgs
total_balance
dates

admin = ADMIN()
admin.total_balance_computer(total_balance)
admin.report(hgs)