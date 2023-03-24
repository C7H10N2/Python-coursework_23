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
