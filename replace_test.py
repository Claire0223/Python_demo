#coding=utf-8

#替换字符，包括字符串中存在相同的特殊字符
#enumerate（）枚举函数 同时列出数据和数据下标，用于for循环

def duplicate_encode(word):
    demoStr=word.lower()
    #设定一个空字典类型
    counterDict=dict()
    #特殊字符
    specialChar={'(':[],')':[]}

    #枚举字符串,返回下标和值{下标：字符}
    for index,char in enumerate(demoStr):
        #统计字符出现的次数,放在counterDict上[char,times]
        if char in counterDict:
            counterDict[char]+=1 
        
        else:
            counterDict[char]=1

        #判断是不是特殊字符,是的话，就在specialChar中添加索引，dict[key].append(value)
        if char in specialChar:
            specialChar[char].append(index)
    
    #替换
    for char in counterDict:
        #判断是否是特殊字符,是的话跳过本次循环，不参与活动
        if char in specialChar: continue
        if counterDict[char]==1:
            replaceChar='('
        else:
            replaceChar=')'
        demoStr=demoStr.replace(char,replaceChar)
    
    demoList=list(demoStr)
    for char in specialChar:
        if len(specialChar[char])==1:
            replaceChar="("
        else:
            replaceChar=")"
        
        #遍历specialChar里面的value，demoList替换成replaceChar
        for index in specialChar[char]:
            demoList[index]=replaceChar

    demoStr=''.join(demoList)
    print(demoStr)

duplicate_encode('Succe) ss')





