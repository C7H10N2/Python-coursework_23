# Lab4

## Qiang
```python
class QiangJinJiu: 
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.load_file()
    
    def load_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
    
    def print_lines(self):
        for line in self.lines:
            print(line.strip())
    
    def print_chars(self):
        for i in range(len(self.lines)):
            line = self.lines[i]
            print(line[i].strip())

if __name__ == '__main__':
    qiang = QiangJinJiu('./lab4/qiang.txt')
    qiang.print_lines()
    qiang.print_chars()
```

```txt
君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
烹羊宰牛且为乐，会须一饮三百杯。
岑夫子，丹丘生，将进酒，杯莫停。
与君歌一曲，请君为我倾耳听。
钟鼓馔玉不足贵，但愿长醉不复醒。
古来圣贤皆寂寞，惟有饮者留其名。
陈王昔时宴平乐，斗酒十千恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马、千金裘，呼儿将出换美酒，与尔同销万古愁。
```
## 运行结果
```
君不见黄河之水天上来，奔流到海不复回。
君不见高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
烹羊宰牛且为乐，会须一饮三百杯。
岑夫子，丹丘生，将进酒，杯莫停。
与君歌一曲，请君为我倾耳听。
钟鼓馔玉不足贵，但愿长醉不复醒。
古来圣贤皆寂寞，惟有饮者留其名。
陈王昔时宴平乐，斗酒十千恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马、千金裘，呼儿将出换美酒，与尔同销万古愁。

君
不
得
材
且
丘
请
，
惟
酒
沽
出
```

## 程序解释
我写了一个Python类，名为QiangJinJiu，用来处理古诗《将进酒》。这个类的构造函数__init__接收一个文件名作为参数，将文件名保存在实例变量self.filename中，并调用load_file方法加载文件内容。

load_file方法使用Python的with语句打开指定的文件，并以utf-8编码读取文件内容。读取到的内容保存在实例变量self.lines中，每行内容作为列表中的一个元素。

接下来，我实现了两个方法来处理这个古诗。

print_lines方法遍历实例变量self.lines中的每行内容，并使用print函数输出。我在输出之前使用了strip方法去除每行内容的首尾空白字符（包括换行符）。

print_chars方法遍历实例变量self.lines中的每行内容，然后使用索引i获取该行中的第i个字符，并输出该字符。需要注意的是，索引从0开始，因此第1行第1个字符对应的是line[0]。

在if __name__ == '__main__':语句块中，我创建了一个QiangJinJiu实例，并调用了它的两个方法：print_lines、print_chars。这些方法会依次输出《将进酒》的每行内容、每行中的特定字符。

## 总结
从上述程序中，我学到了如何使用Python读取文件，以及如何操作文件中的数据。通过这个例子，我也学习到了如何使用Python中的列表来存储和操作多个数据。另外，还学会了如何使用类来组织代码，使得程序更加清晰易懂，并且可复用性更高。