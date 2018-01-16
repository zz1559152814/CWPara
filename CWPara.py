#!/usr/bin/env python2.6
# encoding: utf-8

# select sentence which including labeled words
import os,re

class CWPara():
    def __init__(self, word_files, cont_files, thres):
        self.wordFs = [open(word_file,'r') for word_file in word_files]
        self.contFs = [open(cont_file,'r') for cont_file in cont_files]
        self.pairs = []
        self.cont_sents = []
        self.thres = thres
    def preprocess(self):
        for wordF in self.wordFs:
            word_content = wordF.read()
            for line in word_content.split('\n'):
                if re.match('^- *:*',line):
                    if '：' in line:
                        eng = line[2:].split('：')[0].rstrip('.').lstrip('.').rstrip(',').lstrip(',')
                        chi = line[2:].split('：')[1]
                        self.pairs.append([eng,chi])
                    elif ':' in line:
                        eng = line[2:].split(':')[0].rstrip('.').lstrip('.').rstrip(',').lstrip(',')
                        chi = line[2:].split(':')[1]
                        self.pairs.append([eng,chi])
                    else:
                        print line
        for contF in self.contFs:
            cont_content = contF.read()
            cont_paras = cont_content.split('\n')
            cont_sents = [cont_para.split('.') for cont_para in cont_paras]
            self.cont_sents = sum(cont_sents,[])
            
    def select(self):
        # print self.pairs
        for pair in self.pairs:
            print pair[0],'::',pair[1]
            for sentence in self.cont_sents:
                if len(sentence.split(' '))>= self.thres:
                    if pair[0] in sentence:
                        print sentence+'.'
                        print '\n'
        
a = CWPara(["./RedNotebook-Export_2018-01-16.txt"],['./a.txt'],10)
a.preprocess()
a.select()
