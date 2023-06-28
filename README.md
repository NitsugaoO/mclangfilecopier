# MClangfilecopier
A piece of python code written to more conveniently update the language files of Minecraft mods.
为了更方便地更新 Minecraft 的语言文件而简单编写的一段 Python 代码。

本人经常在更新汉化文件时遇到这样的情况：
打开 zh_cn.json 和 en_us.json，发现文件的行数不一致。
问题来了：模组的作者究竟是添加了一行，减少了一行，抑或是将文件进行了格式化？
逐行排查实在令人头大，本人也并未找到能完美胜任这一工作的文本对比软件。
于是，在搜索少量 Python 知识后，本人凭借自己薄弱的编程功底写下了这段代码。

# 使用方法
1. 确保你安装了 Python（编写使用版本为 3.10）；
2. 将此 .py 文件与需要处理的 zh_cn.json 和 en_us.json 放到同一目录下；
3. 运行 .py 文件。新的 new.json 即为处理后所得的文件。

# 大致运行原理
1. 从 en_us.json 中逐行提取 id；
2. 将 id 在 zh_cn.json 中搜索，以得到已有的汉化名；若找不到此 id，程序会保留原英文名；
3. 最后将所有结果进行拼接，将文本保存在新建的名为 new.json 的文件中。

# 注意事项
1. 所得的文件已经具备正常语言文件的格式（开头结尾的大括号和正确的行末逗号），替换掉原有的 zh_cn.json 即可在游戏中加载。
2. 默认行首缩进为 2 个空格。
3. 程序不会理会 zh_cn.json 中存在而 en_us.json 中不存在的（即 id 已经更改或删除）的条目，确保两文件的行数一致。
