import pandas as pd
import matplotlib.pyplot as plt

keyword = 'living table'
f = open('./'+keyword+'_1.txt','r')
word = {}
cat = [[],[],[],[],[]]
lines = f.readlines()
for line in lines:
    temp = line.split(' ')
    print(temp)
    temp2 = temp[0].split(',')
    if temp[1].find('용도') != -1:
        cat[0].append(temp2)
    if temp[1].find('형태') != -1:
        cat[1].append(temp2)
    if temp[1].find('재질') != -1 or temp[1].find('커버') != -1:
        cat[2].append(temp2)
    if temp[1].find('색상') != -1:
        cat[3].append(temp2)
    if temp[1].find('브랜드') != -1:
        cat[4].append(temp2)



plt.figure(figsize=(18,20))

plt.subplot(2,2,1)
plt.title('fabric')

df = pd.DataFrame(cat[2])
plt.pie(df[1],labels=df[0],autopct='%1.1f%%',startangle=90)
plt.axis('equal')


plt.subplot(2,2,2)
plt.title('shape')

df = pd.DataFrame(cat[1])
plt.pie(df[1],labels=df[0],autopct='%1.1f%%',startangle=90)
plt.axis('equal')

plt.subplot(2,2,3)
plt.title('use')

df = pd.DataFrame(cat[0])
plt.pie(df[1],labels=df[0],autopct='%1.1f%%',startangle=90)
plt.axis('equal')


plt.subplot(2,2,4)

plt.title('color & pattern')

df = pd.DataFrame(cat[3])
plt.pie(df[1],labels=df[0],autopct='%1.1f%%',startangle=90)
plt.axis('equal')

plt.show()