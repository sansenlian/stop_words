# -*- coding:utf-8 -*-
import os

if __name__ == "__main__":
    for root, dirs, files in os.walk("./lib", topdown=False):
        for name in dirs:
            print('='*20)
            print(name+'\n')
            stopWordsSet = set()
            for f in os.listdir(os.path.join(root, name)):
                f = os.path.join(os.path.join(root, name, f))
                print(f)
                with open(f, 'r', encoding='utf-8') as fp:
                    for word in fp.readlines():
                        stopWordsSet.add(word.strip())

            stopWords = sorted(list(stopWordsSet))
            with open('{}.txt'.format(name), 'w', encoding='utf-8') as f:
                for word in stopWords:
                    f.write("%s\n" % word)
