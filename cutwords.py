import jieba
import jieba.analyse
content = open('/Users/kaihanandy/Desktop/original.txt', 'rb').read()
words = jieba.cut(content, cut_all=False)
print("Running!!")
output = open('/Users/kaihanandy/Desktop/cut.txt', 'w')
output.writelines(",".join(words))
output.close
print("Done!!")