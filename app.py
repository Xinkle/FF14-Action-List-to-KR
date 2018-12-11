import pandas

ENG_Action_DF = pandas.read_csv('Action.en-US.csv')
KOR_Action_DF = pandas.read_csv('SkillList_KR.txt', sep="|", names=['idx', 'name'])

for (index, row) in KOR_Action_DF.iterrows():
    dec_index = int(row[0], 16)
    ENG_Action_DF['0'][dec_index+2] = row[1]

ENG_Action_DF.to_csv('Action.ko-KR.csv', index=False)