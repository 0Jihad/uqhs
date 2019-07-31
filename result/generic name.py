# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:26:33 2019

@author: AdeolaOlalekan
"""
#.split(',')
import random
from random import randrange
import pandas as pd
def student_names(sex, size, n = 105):
    df = pd.read_csv('C:/Users/hp/Desktop/fgr/target.csv', encoding='ISO-8859-1')
    sd = []
    for i in range(0, len(df)):
        sd += [df.ix[i, 0]]
    genders = [sd[:n], sd[n:]]
    males = [[i[0] for i in [i.split(',') for i in genders[0]]], [i[1] for i in [i.split(',') for i in genders[0]]]]
    females = [[i[0] for i in [i.split(',') for i in genders[1]]], [i[1] for i in [i.split(',') for i in genders[1]]]]
    surnames = males[0] + females[0]
    if sex == 'male':
        first_names = males[1]
    elif sex == 'female':
        first_names = females[1]
    last_names = surnames
    group = list()
    #group += 'A-JELEEL OLATUNDE '
    for i in range(0, size):
        full_name = random.choice(last_names)+""+random.choice(first_names)
        group += [full_name]
    return group

 
def student_scores(many):
    scores = [[], [], [], []]
    for i in range(0, many):#test
        scores[0] += [randrange(8, 20)]
    for i in range(0, many):#ass
        scores[1] += [randrange(6, 10)]
    for i in range(0, many):#atd
        scores[2] += [randrange(6, 10)]
    for i in range(0, many):#exam
        scores[3] += [randrange(19, 60)]
    return scores

def student_results(males, females):
    a = sorted(student_names('male', males))
    b = sorted(student_names('female', females))
    return [a, b]
    ##########################################
    
def placing_scores(a, b, males, females, group):
    global df_all
    cl = group[0]
    su = group[1]
    male_students = [a, student_scores(males)]
    female_students = [b, student_scores(females)]
    scores = [male_students, female_students]
    serial = []
    for x in range(0, len(scores[0][0])):
        serial += [[scores[0][0][x], scores[0][1][0][x], scores[0][1][1][x], scores[0][1][2][x], scores[0][1][3][x]]]
    #serial += [[]]
    for x in range(0, len(scores[1][0])):
        serial += [[scores[1][0][x], scores[1][1][0][x], scores[1][1][1][x], scores[1][1][2][x], scores[1][1][3][x]]]
    df_all = pd.DataFrame(serial)
    df_male = pd.DataFrame(male_students[0])
    df_female = pd.DataFrame(female_students[0])
    df_all.to_csv(r'C:/Users/hp/Desktop/fgr/all_scores/'+cl+'_'+su+'_scores.txt', header=None, index=None, sep=',', mode='a')
    df_male.to_csv(r'C:/Users/hp/Desktop/fgr/male_names/'+cl+'_'+su+'.csv')
    df_female.to_csv(r'C:/Users/hp/Desktop/fgr/female_names/'+cl+'_'+su+'.csv')
    return [male_students[0], female_students[0]]

def new_class(m, f, g):
    sd = student_results(m, f)
    placing_scores(sd[0], sd[1], m, f, g)
    M = pd.read_csv('C:/Users/hp/Desktop/fgr/male_names/'+g[0]+'_'+g[1]+'.csv', encoding='ISO-8859-1', index_col = 0)
    F = pd.read_csv('C:/Users/hp/Desktop/fgr/female_names/'+g[0]+'_'+g[1]+'.csv', encoding='ISO-8859-1', index_col = 0)
    sub = [g[0], ['MATH1', 'AGR1', 'CIV1', 'COM1', 'IRS1', 'ARB1', 'YOR1', 'BIO1', 'PHY1', 'CHE1', 'ELE1', 'GRM1', 'CTR1', 'ICT1', 'ECO1', 'LIT1', 'ACC1', 'GEO1', 'GOV1']]
    M.columns = ['a']
    F.columns = ['b']
    for i in range(0, len(sub[1])):
        placing_scores(list(M.a), list(F.b), m, f, [sub[0], sub[1][i]])
        
    sub = [g[0], ['ENG2', 'MATH2', 'AGR2', 'CIV2', 'COM2', 'IRS2', 'ARB2', 'YOR2', 'BIO2', 'PHY2', 'CHE2', 'ELE2', 'GRM2', 'CTR2', 'ICT2', 'ECO2', 'LIT2', 'ACC2', 'GEO2', 'GOV2']]
    for i in range(0, len(sub[1])):
        placing_scores(list(M.a), list(F.b), m, f, [sub[0], sub[1][i]])
        
    sub = [g[0], ['ENG3', 'MATH3', 'AGR3', 'CIV3', 'COM3', 'IRS3', 'ARB3', 'YOR3', 'BIO3', 'PHY3', 'CHE3', 'ELE3', 'GRM3', 'CTR3', 'ICT3', 'ECO3', 'LIT3', 'ACC3', 'GEO3', 'GOV3']]
    for i in range(0, len(sub[1])):
        placing_scores(list(M.a), list(F.b), m, f, [sub[0], sub[1][i]])
new_class(43, 31, ['SSS 2', 'ENG1'])
#['MATH1', 'AGR1', 'CIV1', 'COM1', 'IRS1', 'ARB1', 'YOR1', 'BIO1', 'PHY1', 'CHE1', 'ELE1', 'GRM1', 'CTR1', 'ICT1', 'ECO1', 'LIT1', 'ACC1', 'GEO1', 'GOV1']
#['ENG2', 'MATH2', 'AGR2', 'CIV2', 'COM2', 'IRS2', 'ARB2', 'YOR2', 'BIO2', 'PHY2', 'CHE2', 'ELE2', 'GRM2', 'CTR2', 'ICT2', 'ECO2', 'LIT2', 'ACC2', 'GEO2', 'GOV2']
#['ENG3', 'MATH3', 'AGR3', 'CIV3', 'COM3', 'IRS3', 'ARB3', 'YOR3', 'BIO3', 'PHY3', 'CHE3', 'ELE3', 'GRM3', 'CTR3', 'ICT3', 'ECO3', 'LIT3', 'ACC3', 'GEO3', 'GOV3']


words = [
 'look' , 'into' , 'my' , 'eyes' , 'look' , 'into' , 'my' , 'eyes' ,
 'the' , 'eyes' , 'the' , 'eyes' , 'the' , 'eyes' , 'not' , 'around' , 'the' ,
 'eyes' , "don't" , 'look' , 'around' , 'the' , 'eyes' , 'look' , 'into' ,
 'my' , 'eyes' , "you're" , 'under']
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common()
xy = [list(i[:]) for i in top_three]
sd = []
for i in range(0, len(xy)):
    if xy[i][1] > 1:
        sd += [xy[i]]
ds = []
if len(sd) != 0:
    for i in range(0, len(sd)):  
        for r in range(0, sd[i][1]):
            for s in words:
                if s == sd[i][0]:
                    words[words.index(sd[i][0])] = words[words.index(sd[i][0])]+str(words.index(sd[i][0]))
                    
                    
                    
sp = []
for i in range(1, 31):
    sp += [tuple([(str(2018+i)), (str(2018+i-1)+'/'+str(2018+i))])]
    
