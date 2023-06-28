f1 = open("zh_cn.json","r",encoding="UTF-8")
f2 = open("en_us.json","r",encoding="UTF-8")
f3 = open("new_zh_cn.json","w",encoding="UTF-8")
o1 = f1.read()
o2 = f2.read()
f2.seek(0)
f3.write("{\n")
n = False
for line in f2:
    if not line.find("\"") == -1:
        if not n == False:
            f3.write(",\n")
        else:
            n = True
        left = line.split("\"")[1]
        l1 = o1.find(left)
        if l1 == -1:
            l1 = o2.find(left)
            l2 = o2.find("\": \"", l1) + 4
            l3 = o2.find("\"",  l2)
            right = o2[l2-1:l3]
        else:
            l2 = o1.find("\": \"", l1) + 4
            l3 = o1.find("\"",  l2)
            right = o1[l2-1:l3]
        f3.write("  \""+left+"\": "+right+"\"")
f3.write("\n}")
print("Done!")
f1.close()
f2.close()
f3.close()
