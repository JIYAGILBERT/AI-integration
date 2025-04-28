                                    # DAY-1 CLZ

# import numpy

import numpy as np

# l=(1,2,3,4,5)
# print(type(l))


# arr = numpy.array(l)
# print(arr)
# print(type(arr))


# arr = np.array(42)
# print(arr)
# print(type(arr))


# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr = np.array([[1,2],[4,5]])
# print(arr)
# print(type(arr))

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# print(type(arr))


# arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# print(arr)
# print(type(arr))
# print(arr.ndim)


# arr = np.array([1,2,3,4,5],ndimin=5)
# print(arr)
# print(arr.ndim)

# >>>>>>..    ndimin : key word aayatt pass cheythaa mathhi

# >>>>>>>>>>>>>>..indux positioning

# 1)

# arr = np.array([[1,2],[4,5]])
# print(arr[0] [1])


# import pandas 
import pandas as pd
import csv

# data ={
#     "name" : ['akhil' 'aswin' 'athul']
#     "age" : [20,21,22]
# }
# print(data)
# mydata=pd.DataFrame(data)
# print(mydata)

# arr =[1,2,3,5]
# arr = {'day1':400, "day2":420, "day3":380}
# myarr = pd.series(arr,index=["day1","day2"])
# print(myarr)

# ithrem cheythatt dummy datas aann





#  > data set ine aanu access cheyyan ponee (sir google vazhi korachu values eduthh kaanikkuneee) 
    # > google ill ninn edutha datas  ""data.csv "" file illekk store aakanam

# df = pd.read_csv(data.csv)
# print(df)

# df = pd.read_csv('data.csv')
# print(df)
# print(df.to_string())

# df = pd.read_csv('data.csv')
# print(df)
# print(df.to_string())
# print(df.head())
# print(df.head(12))



# > json data koodeee google ill ninnu sir edukkunondd "data.json" file illekk aaa copie cheythaa data save akkanam 

df=pd. read_json('data.json')
print(df)

# > kittunna datas ill ninnu blank ayyi kedakunna datas enganne remove cheyyam athannu iny  nokkunathh
# > empty data, wrong cells , duplicate texts etc.. anganne enthumm aavam

#  empty data enganee remove cheyyam 
# df = pd.read_csv('data.csv')
# new_df = df.dropna()
# # print(new_df)
# print(new_df.to_string())


# duplicate datas check cheyyan
# df = pd.read_csv('data.csv')
# print(df.duplicate().to_string())

# new_data = df.drop_duplicates()
# print(new_data)

# calories mathram edukkan(calories aayatt related aaya data annu eduthekkunee athannu calories nokkunee)
# df = pd.read_csv('data.csv')

# print(df["Calories"].mean())

# print(df["Calories"].sum())




# oru file illekk read cheyyunna kaaryangall annu ipo nokkiyathh iny write cheyyanathhu nokkam 
#  > oru object data indavanamm 

# data = {
#     "name" : ["amala", "aswin", "manu"],
#     "age" : [20,21,22],
#     "place" : ['ekm', 'tvm', 'tsr']
# }

# headers = data.keys()
# row = zip(*data.values())


# with open('output.csv', 'w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(row)





# xl files varunna datas inne enganne write cheyyum enn nokkam iny
# sir inte kayill olla project ill ninnanuu kaanichu tharunnathh
#  oru prediction inte project annu(flood prediction project) 
# 1901 - 2018 varee olla datas olla oru sheet like 'xl' file ayyatt annu ollathh


# > rainbow.csv extention download cheyyanam (colorfull ayyi view cheyyam)

                                    
                                    
                                    # DAY-1 CLZ FINISHED