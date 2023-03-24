# Lab1

## What day of the week is today?

```py
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
```

## 代码解析

代码定义了一个名为 `Week` 的类，其中包含一个名为 `get_day_name` 的方法，该方法接受一个整数参数 `day_num`，并返回对应星期几的名称。  

使用构造函数 `__init__` 中定义了一个字符串 `week_name`，包含了星期一到星期日的名称，这些名称被组合成一个长字符串。  

`get_day_name` 方法首先检查传入的参数是否在合法范围内（1到7之间），如果不是，将输出一条错误信息并退出程序。如果参数合法，则计算出对应名称在 `week_name` 字符串中的位置，并从该位置开始提取3个字符，即星期几的名称。  

最后，该代码创建了一个 `Week` 类的实例 `week`，并要求用户输入今天是星期几的数字，然后调用 `week` 实例的 `get_day_name` 方法来获取对应的星期几名称，并输出结果。

## 运行示例
```
What num is today: 2
Today is: Tue

What num is today: 8
Invalid day number
```

用户输入了数字 2，代表今天是星期二，程序输出了对应的星期二名称 "Tue"。  
用户输入了数字 8，超出了合法范围，因此程序输出了一条错误信息 "Invalid day number"，并退出程序。

## 总结

通过本次实验，本次实验主要围绕 Python 字符串类型展开，旨在让我们熟悉并掌握 Python 字符串类型的基本操作。实验要求我们编写一个程序，接受用户输入一个数字，代表一周中的某一天，然后利用字符串基本操作输出对应的英文名称的缩写。