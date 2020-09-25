import os
result = []
counter = 0

def getDirContent(mypath):
    isDirectory = os.path.isdir(mypath)
    result.append(mypath)
    global counter
    counter = counter + 1
    #print(isDirectory)
    if isDirectory:
        #result.append(mypath)
        for sub in os.listdir(mypath):
            newDir = mypath+'/'+sub.replace('\\','/')
            #print(newDir)
            getDirContent(newDir)
    return result

if __name__ == '__main__':
    result = getDirContent('/home/abdullah/Desktop/level0')
    mypath = '/home/abdullah/Desktop/test_projects'
    print(len(result))
    print(counter)
    for idx in result:
        print(idx)