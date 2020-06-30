import pandas as pd
import csv
import urllib.request
import os.path


keyword = 'living table'
f = open('./'+keyword+'_1.csv','r',encoding='CP949')
rdr = csv.reader(f)
i = 1
print(0)
for line in rdr:
    name = line[2].replace(',','')
    if os.path.isfile('./table image/'+name+'.png') != True:
        urllib.request.urlretrieve(line[3],'./table image/'+name+'.png')
    else:
        urllib.request.urlretrieve(line[3], './table image/' + name + '_'+str(i)+'.png')
        i = i+1

