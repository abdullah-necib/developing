import json
x= 5
data = {
    "No":0,
    "president": 'Abdullah'}

"""
with open('/home/abdullah/Desktop/test_projects/test.json','a') as file:
    for i in range(1,100000):
        data['No'] = i
        json.dump(data,file)
        file.write('\n')"""
    
with open('/home/abdullah/Desktop/test_projects/test.json','r') as file:
    for line in file.readlines():
        jobject = json.loads(line)
        if jobject['No'] > 1000 and jobject['No'] < 1010 :
            print(jobject['No'],'          ',jobject['president'])
