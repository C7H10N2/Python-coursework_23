# Lab6

## jieba库的应用
通过对`三国演义.txt`文件进行词频统计，分析作者罗贯中对小说中人物偏向，对魏蜀吴三个国家的喜好。
```python
import jieba
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

# 国家偏好分析
analyzer = TextAnalyzer(content, excludes)
analyzer.cut_words()
analyzer.analyze(CountryAnalyzer())
analyzer._print_top_n_counts(3)
analyzer.generate_wordcloud()
```
输出示例
```
诸葛亮        1383
刘备         1252 
曹操          960 
关羽          519
张飞          358
吕布          300
赵云          278
孙权          264
司马懿         221
周瑜          217
袁绍          191
马超          185
魏延          180
黄忠          168
姜维          151
---------------------
蜀           462
吴           140
魏           104
```
绘制词云
![词云](./img/0x00.png)

根据你提供的词频统计结果，可以看出罗贯中对小说中的人物偏爱程度。诸葛亮、刘备和曹操是三个出现频率最高的人物，其中诸葛亮出现的频率最高，说明罗贯中比较偏爱诸葛亮这个角色。

从三国时期的历史背景来看，魏蜀吴是三个势力，而罗贯中笔下的人物大多与这三个势力有关。根据词频统计结果，出现频率最高的人物中，属于蜀汉势力的人物（如诸葛亮、刘备、张飞、马超、魏延、黄忠、姜维等）出现的次数最多，说明罗贯中比较偏爱蜀汉这个势力。

但这个结论是基于人物名字以及国家名字出现的频率统计，可能并不完全准确。

## 程序解释

为了对对《三国演义》这本小说进行文本分析，需要使用`jieba`将中文文本分成词语，并应用两个不同的分析器来提取人物和国家偏好。

程序包含三个类：

DataAnalyzer：一个类，用于从文件中读取文本数据。

TextAnalyzer：一个类，用于对文本进行分析。它包含一个 cut_words() 方法来将文本内容分词，一个 analyze() 方法来对分词后的词语应用不同的分析器，以提取人物或国家偏好，还有一个 generate_wordcloud() 方法来生成词云图。在初始化时，可以指定排除某些词语，以避免这些词语干扰偏好分析。

CharacterAnalyzer 和 CountryAnalyzer：两个类，分别用于提取人物和国家偏好。它们都实现了 call() 方法，以接受分词后的词语和排除列表作为参数，分析文本并返回一个字典，其中键是人物或国家名称，值是对应人物或国家在文本中出现的次数。

程序首先使用 DataAnalyzer 类从文件中读取文本内容，然后创建 TextAnalyzer 实例，传入读取的文本内容和要排除的词语。接着，分别对文本内容应用 CharacterAnalyzer 和 CountryAnalyzer 两个分析器，提取人物和国家偏好信息。最后，打印出前 15 个最常出现的人物和前 3 个最常出现的国家，并生成相应的词云图展示。

## 不足及改进空间
在上述程序中，使用了一个字符分析器来统计人物出现的次数，并且根据一些关键词（如“诸葛亮”、“关公”、“玄德”和“孟德”等）进行了简单的合并，以减少名称变体对分析结果的影响。然而，这种合并方式并不完美，因为它是基于固定的关键词进行的，可能会忽略一些别名或变体名称，导致统计结果不准确。

为了进一步提高统计结果的准确性，可以使用命名实体识别（NER）来识别文本中的实体，例如人名、地名和组织机构名等，并将它们合并在一起以减少名称变体的影响。在这种情况下，可以使用jieba库中的`jieba.analyse.extract_tags()`函数，该函数可以对文本中的关键词进行提取，并使用tf-idf算法来计算它们的重要性。通过设置`allowPOS`参数来指定只提取特定词性的词语，例如人名或地名等。

另外，可以使用更高级的NLP工具，如spaCy或Stanford NER，来进行命名实体识别和合并，这些工具具有更高的准确性和更广泛的覆盖范围。但是，这些工具需要更多的计算资源和更长的处理时间。因此，在实际应用中，需要根据具体情况进行权衡和选择。