import jieba
import jieba.analyse
import jieba.posseg as pseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class DataAnalyzer:
    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

class TextAnalyzer:
    def __init__(self, content, excludes=set()):
        self.content = content
        self.excludes = excludes
    
    def cut_words(self):
        self.words = jieba.lcut(self.content)

    def analyze(self, analyzer):
        self.counts = analyzer(self.words, self.excludes)

    def _print_top_n_counts(self, top_n):
        item = list(self.counts.items())
        item.sort(key=lambda x:x[1], reverse=True)
        for i in range(top_n):
            word, count = item[i]
            print("{0:<10}{1:>5}".format(word, count))
    
    def generate_wordcloud(self, top_n):
        item = list(self.counts.items())
        item.sort(key=lambda x:x[1], reverse=True)
        top_n_counts = {word: count for word, count in item[:top_n]}
        wc = WordCloud(font_path='msyh.ttc', width=800, height=600, background_color='white')
        wc.generate_from_frequencies(top_n_counts)
        plt.imshow(wc)
        plt.axis('off')
        plt.show()

class CharacterAnalyzer:
    def __call__(self, words, excludes):
        character_count = {}
        for word in words:
            if len(word) == 1 or word in excludes:
                continue
            elif word in ["诸葛亮", "孔明曰", "孔明"]:
                rword = "诸葛亮"
            elif word in ["关公", "云长"]:
                rword = "关羽"
            elif word in ["玄德", "玄德曰"]:
                rword = "刘备"
            elif word in ["孟德", "丞相"]:
                rword = "曹操"
            else:
                rword = word
            character_count[rword] = character_count.get(rword, 0) + 1
        return character_count

class CountryAnalyzer:
    def __call__(self, words, excludes):
        countries = ['魏', '蜀', '吴']
        country_count = {'蜀': 0, '魏': 0, '吴': 0}
        for i in countries:
            country_count[i] = words.count(i)
        return country_count
    
analyzer = DataAnalyzer()
content = analyzer.read_file('./lab6/三国演义.txt') 
excludes = {'何故', '先锋', '都督', '汉中', '先主', '今日', '然后', '不可', '军马', '陛下', '二人', '丞相', '商议', '大喜', '左右', '云长', '众将', '大军', '次日', '于是', '不知', '引兵', '军士', '不敢', '大叫', '却说', '不能', '将军', '天下', '荆州', '太守', '如何', '如此', '人马', '主公', '一人', '后主','东吴','魏兵','只见','背后','此人','上马','蜀兵','后人','一面','何不','城中','不如','忽报','不如','夫人','先生','令人','百姓','原来','天子','赶来','江东','下马','喊声','正是'}

# 人物偏好分析
analyzer = TextAnalyzer(content, excludes)
analyzer.cut_words()
analyzer.analyze(CharacterAnalyzer())
analyzer._print_top_n_counts(15)
analyzer.generate_wordcloud(15)
print('---------------------')

# 国家偏好分析
analyzer = TextAnalyzer(content, excludes)
analyzer.cut_words()
analyzer.analyze(CountryAnalyzer())
analyzer._print_top_n_counts(3)
#analyzer.generate_wordcloud()
