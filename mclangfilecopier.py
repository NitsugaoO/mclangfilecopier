o1 = open("zh_cn.json", "r", encoding = "UTF-8").readlines()
o2 = open("en_us.json", "r", encoding = "UTF-8").readlines()    #readlines方法将文件内容以列表形式返回
f3 = open("new_zh_cn.json", "w", encoding = "UTF-8")
def wf(a, b):   #判断a是否为末项，是则将b的逗号去掉后写入f3，否则直接写入
    if a == o2[-2]:
        f3.write(b[0:-2] + "\n")
    else:
        f3.write(b)
for i in o2:    #在英文文件中遍历i
    if "\"" in i:   #若i中有双引号，则为有效条目，需要判断id与name
        s = i.split("\"")   #将i按双引号进行切割，s的第2位即s[1]对应此条目的id
        b = False   #旗标变量，代表是否在中文文件中找到对应id
        for j in o1:    #在中文文件中遍历j
            if "\"" in j:   #若j为有效条目
                if s[1] == j.split("\"")[1]:    #若找到j的id与i的id对应
                    wf(i, j)    #将中文条目代替英文写入
                    b = True    #记录找到对应id
                    break   #跳出此循环
        if b == False:  #若没找到
            wf(i, i)    #将原英文条目写入
    else:
        f3.write(i) #若是换行或大括号等非有效条目则直接写入
f3.close()
