def getBlockContactList():
    blockContactList = set()
    file = open('blockContactList.txt','r')
    line = file.readline()
    while line:
        blockContactList.add(line)
        line = file.readline()
    file.close()  
    return blockContactList

# l = getBlockContactList()
# print(l)
# for i in l:
#     print(i)

def getMsg():
    file = open('msg.txt','r')
    line = file.readline()
    msg = ''
    while line:
        msg+="*"+line[:-1]+"*"+"\n"
        line = file.readline()
    msg+='\n'
    file.close()  
    return msg

# print(getMsg())
