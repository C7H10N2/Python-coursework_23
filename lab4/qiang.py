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