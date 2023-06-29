o1 = open("zh_cn.json", "r", encoding = "UTF-8").readlines()
o2 = open("en_us.json", "r", encoding = "UTF-8").readlines()
fw = open("new_zh_cn.json", "w", encoding = "UTF-8")
end = -1
while not "\"" in o2[end]:
    end = end - 1
for i in o2:
    flag = False
    if "\"" in i:
        s = i.split("\"")
        for j in o1:
            if "\"" in j:
                if s[1] == j.split("\"")[1]:
                    if i == o2[end]:
                        fw.write(j.split(",")[0].split("\n")[0] + "\n")
                    else:
                        fw.write(j)
                    flag = True
                    break
    if flag == False:
        fw.write(i)
fw.close()
