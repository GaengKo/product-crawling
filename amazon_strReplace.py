import pandas as pd
import csv

check = True
while check:
    keyword = input('xlsx 파일명 입력 ex) code_zero.xlsx : ')
    try:
        rdr = pd.read_excel('./amazon_review/'+keyword)
        check = False
    except Exception as e:
        print('파일을 찾을 수 없습니다.')

num = int(input('수집할 리뷰의 최대 평점 입력 (1~5): '))
word = {}
#rdr = pd.read_excel('./amazon_review/Roborock S5 Robot.xlsx')

print(rdr.iloc[0,1])
print(len(rdr))
asdasdasd = 0 # 저장 리뷰 카운트
for i in range(len(rdr)):
    line = rdr.iloc[i,:]
    print(line)
    if line[0] == 'title' or float(line[1].split(' ')[0]) > num:
        pass
    else:
        asdasdasd = asdasdasd + 1
        string_temp = str(line[0]+' '+str(line[2]))
        temp = pd.DataFrame({'memo':string_temp},index=[0])

        temp['memo'] = temp['memo'].str.replace(pat=r'[^A-Za-z0-9]', repl=r' ', regex=True)
        temp['memo'] = temp['memo'].str.replace(pat=r'[\s\s+]', repl=r' ', regex=True)
        temp = temp['memo'][0].lower().split()


        for i in temp:
            if i in word:
                word[i] = word[i] + 1
            else:
                word[i] = 1


print(word)
f2 = open("except_word.txt",'r')
lines = f2.readlines()
for line in lines:
    print(line)
    try:
        del word[str(line).split('\n')[0]]
    except Exception as e:
        print(e)
f2.close()
word = sorted(word.items(),reverse=True,key=lambda item:item[1])
with open('./'+keyword.split('.')[0]+'_'+str(asdasdasd)+'__'+str(len(rdr))+'_word.txt','w',-1,'utf-8',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(word)
