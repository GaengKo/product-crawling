import pandas as pd
import csv
import matplotlib.pyplot as plt

keyword = 'roborock'
f = open('./amazon_review/Roborock S5 Robot.xlsx','r',encoding='cp949')
rdr = csv.reader(f)
word = {}
rdr = pd.read_excel('./amazon_review/Roborock S5 Robot.xlsx')

print(rdr.iloc[0,1])
print(len(rdr))
for i in range(len(rdr)):
    line = rdr.iloc[i,:]
    print(line)
    if line[0] == 'title' or float(line[1].split(' ')[0]) > 2:
        print(line[0])
    else:
        print('123123123')
        print(str(line))
        temp = pd.DataFrame({'memo':str(line[2])},index=[0])
        print('123123123')
        print(temp)
        temp['memo'] = temp['memo'].str.replace(pat=r'[^A-Za-z0-9]', repl=r' ', regex=True)
        temp['memo'] = temp['memo'].str.replace(pat=r'[\s\s+]', repl=r' ', regex=True)
        temp = temp['memo'][0].lower().split()

        print('1231231234')
        print(temp)

        for i in temp:
            if i in word:
                word[i] = word[i] + 1
            else:
                word[i] = 1


print(word)
word = sorted(word.items(),reverse=True,key=lambda item:item[1])
with open('./'+keyword+'_1.txt','w',-1,'utf-8',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(word)
"""
#del word[keyword]
del word['table']
del word['living']
del word['for']
del word['to']
del word['a']
del word['of']
del word['the']
del word['with']
del word['and']
del word['in']


n_word = 0
etc = 0
print(word)
plot_key = []
plot_items = []
i=0
while i < len(word):
    key = word[i][0]
    index = word[i][1]
    if index < 2000:
        etc = etc + index
        del word[i]
        i= i-1
        #word.remove(key)
    else:
        plot_key.append(key)
        plot_items.append(index)
    print(key," : ",index)
    n_word = n_word + index
    i = i+1

plot_key.append('etc')
plot_items.append(etc)
    #word.update
print("총 단어의 수 : ",n_word)

plt.pie(plot_items,labels=plot_key,autopct='%1.2f%%',startangle=90)
plt.axis('equal')
plt.title('Pie Chart of Result : '+keyword )
plt.show()


"""