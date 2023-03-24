class Week:
    def __init__(self):
        self.week_name = "MonTueWedThuFriSatSun"

    def get_day_name(self, day_num):
        if day_num < 1 or day_num > 7:
            print("Invalid day number")
            exit ()
        pos = (day_num - 1) * 3
        return self.week_name[pos:pos + 3]

week = Week()
day_num = eval(input("What num is today: "))
day_name = week.get_day_name(day_num)
print(f"Today is: {day_name}")