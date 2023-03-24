# Lab3

## TempConv

面向对象
```python
class TempConv:
    def __init__(self, temp):
        self.unit = temp[-1].upper()
        self.value = float(temp[:-1])
        
    def c2k(self):
        return self.value + 273.15
    
    def k2c(self):
        return self.value - 273.15
    
    def convert(self):
        if self.unit == "C":
            kelvin = self.c2k()
            return "{:.2f}K".format(kelvin)
        elif self.unit == "K":
            celsius = self.k2c()
            return "{:.2f}C".format(celsius)
        else:
            return "无效"

temp = str(input("请输入温度:"))
converter = TempConv(temp)
result = converter.convert()
print(result)
```
面向过程
```python
temperature = str(input("请输入温度:"))
unit = temperature[-1].upper()
value = float(temperature[:-1])

if unit == "C":
    kelvin = value + 273.15
    result = "{:.2f}K".format(kelvin)
elif unit == "K":
    celsius = value - 273.15
    result = "{:.2f}C".format(celsius)
else:
    result = "无效"

print(result)
```

## 运行示例

```
请输入温度:1C
输出：274.15K

请输入温度:273.15K
输出：0.00C

请输入温度:100F
输出：无效
```

以上示例中，第一个输入表示将1摄氏度转换为开氏度，预期输出为274.15K。

第二个输入表示将273.15开氏度转换为摄氏度，预期输出为0.00C。

第三个输入表示输入的温度单位不是"C"或"K"，预期输出为"无效"。

## 总结

本次实验要求设计一个系统，将摄氏温度转换为开氏温度，或将开氏温度转换为摄氏温度。
首先定义了一个名为TempConv的类，包含了初始化方法、将摄氏温度转换为开氏温度的方法、将开氏温度转换为摄氏温度的方法、以及转换方法。初始化方法接收一个表示温度的字符串，将其解析为数值和单位，并保存在实例变量中。将摄氏温度转换为开氏温度的方法和将开氏温度转换为摄氏温度的方法分别计算转换后的温度，并返回结果。转换方法根据实例变量中保存的单位调用相应的转换方法，并将转换后的温度格式化为字符串返回。主程序中，首先提示用户输入温度，并创建一个TempConv实例。然后调用convert方法进行转换，并将结果保存在result变量中。最后输出转换后的温度。