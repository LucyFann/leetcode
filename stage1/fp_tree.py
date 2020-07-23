import pandas as pd
 
class Task:
    def func(self):
        tf_train_list, tf_test_list = loadSimpDat()
        initSet = createInitSet(tf_train_list)
        myFPtree, myHeaderTab = createFPtree(initSet, 5)  # 最小支持
        tag = list()  # 存储的是筛选的标签
        for child in myFPtree.children.values():
            tag.append(child.name)
        recommend_tag = []
 
        for i in range(len(tf_test_list)):
            user_recommend_tag = []
            for j in enumerate(tf_test_list[i]):
                if j[1] in tag:
                    user_tag_list = list()
                    user_recommend_tag.extend(
                        txt_wrap_by("<", ">", str(findPrefixPath(j[1], myHeaderTab).keys()), user_tag_list))
                user_recommend_tag = list(set(user_recommend_tag))[1:15:1]
            u = [str(i) for i in user_recommend_tag]
            v = ','.join(u)
            recommend_tag.append(v)
 
        print(recommend_tag)
        user = [str(x + 1) for x in range(20)]
        df = pd.DataFrame({'id': user, 'recommand_tags': recommend_tag})
        df.to_csv('src/step1/user_recommand.csv', sep=' ', index=False)
 
 
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue#name存放结点名字
        self.count = numOccur#count用于计数
        self.nodeLink = None#用于连接相似的节点
        self.parent = parentNode#用于存放父节点，用于回溯
        self.children = {}#存放儿子节点
 
    def inc(self, numOccur):
        self.count += numOccur
 
    #用于输出调试，显示树
    def disp(self, ind=1):
        print('  '*ind, self.name, ' ', self.count)
        tag = self.name
        tag = list()
        tag.append(self.name)
        for child in self.children.values():
            child.disp(ind+1)
        return tag

# 为了能方便地访问FP树种每一个不同的元素，需要为每种元素（的链表）设置一个头（header），
# 这个header除了指向指定元素的第一个结点外，还可以保存该元素在数据集中的总出现次数。
def updateHeader(nodeToTest, targetNode):
    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
def updateFPtree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        # 判断items的第一个结点是否已作为子结点
        inTree.children[items[0]].inc(count)
    else:
        # 创建新的分支
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        # 更新相应频繁项集的链表，往后添加
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    # 递归
    if len(items) > 1:
        updateFPtree(items[1::], inTree.children[items[0]], headerTable, count)
 

 
 
#创建FP树，默认最小支持度为1
def createFPtree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    # 删除不满足最小支持度的元素
    for k in list(headerTable.keys()):
        if headerTable[k] < minSup:
            del(headerTable[k])
    freqItemSet = set(headerTable.keys()) # 满足最小支持度的频繁项集
 
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] # element: [count, node]
    retTree = treeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():
        localD = {}
        for item in tranSet:
            if item in freqItemSet: # 过滤，只取该样本中满足最小支持度的频繁项
                localD[item] = headerTable[item][0] # element : count
        if len(localD) > 0:
            orderedItem = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateFPtree(orderedItem, retTree, headerTable, count)
    return retTree, headerTable
 
# 查找以目标元素结尾的所有路径（条件模式基）
# 递归回溯
def ascendFPtree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendFPtree(leafNode.parent, prefixPath)
# 条件模式基
def findPrefixPath(basePat, myHeaderTab):
    treeNode = myHeaderTab[basePat][1] # basePat在FP树中的第一个结点
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendFPtree(treeNode, prefixPath) # prefixPath是倒过来的，从treeNode开始到根
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count # 关联treeNode的计数
        treeNode = treeNode.nodeLink # 下一个basePat结点
    return condPats
 
def mineFPtree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1][0], reverse=True)] # 根据频繁项的总频次排序
    for basePat in bigL: # 对每个频繁项
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable) # 当前频繁项集的条件模式基
        myCondTree, myHead = createFPtree(condPattBases, minSup) # 构造当前频繁项的条件FP树
        if myHead != None:
            mineFPtree(myCondTree, myHead, minSup, newFreqSet, freqItemList) # 递归挖掘条件FP树
 
 
# 数据集
def loadSimpDat():
    df_train = pd.read_csv('src/step1/tag_cooccurrence.csv')
    df_test = pd.read_csv('src/step1/user_tag.csv')
 
    tf_train_list = list()
    tf_test_list = list()
    for i in range(len(df_train)):
        #这里的loc表示都取到了第二列从0到xx行
        temp1 = df_train.loc[i][1].split(',')
        tf_train_list.append(temp1)
    for i in range(len(df_test)):
        temp2 = df_test.loc[i][1].split(',')
        # print(temp2)
        tf_test_list.append(temp2)
    return tf_train_list,tf_test_list
 
# 构造成 element : count 的形式
def createInitSet(dataSet):
    retDict={}
    for trans in dataSet:
        key = frozenset(trans)
        if key in retDict:
            retDict[frozenset(trans)] += 1
        else:
            retDict[frozenset(trans)] = 1
    return retDict
 
def txt_wrap_by( start_str, end, txt, user_tag_list):
        start = txt.find(start_str)
        if start >= 0:
            end_txt = txt.find(end, start) + len(end)
 
            if end_txt >= 0:
                user_tag_list.append(txt[start:end_txt].strip())
                txt = txt[end_txt:]
                txt_wrap_by(start_str, end, txt, user_tag_list)
        return user_tag_list
 
a = Task()
b = a.func()
