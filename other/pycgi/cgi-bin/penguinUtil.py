
def file2map(iPath):
    map={}
    f=open(iPath,"r")
    for line in f:
        array=line.split()
        if len(array) >= 3 :
            #map[array[1]] = [array[0],array[2]]
            # ip ,name ,comment
            map[array[0]] = [array[1],array[2]]
    f.close()
    return map

def enumMap(map):
    keyList=map.keys()
    for key in keyList:
        print("%s => %s" % (key,map[key]))

def indexList(map):
    index=[]
    keyList=map.keys()
    for key in keyList:
        ip = key
        valList = map[key]
        name = valList[0]
        message = valList[1]
        val ='<dl><dt><A HREF="http://%s/index.html">%s</A></dt><dd> %s</dd></dl>\n' % (ip,name,message)
        #print(val)
        index.append(val)
    return index

def map2file(oPath,map):
    f=open(oPath,"w")
    keyList=map.keys()
    for key in keyList:
        valList = map[key]
        ip = valList[0]
        message = valList[1]
        f.write('%s\t%s\t%s\n' % (key,ip,message))
    f.close()

def test():
    map = file2map("name_ip.txt")
    enumMap(map)
    map2file("UQ.txt",map)




