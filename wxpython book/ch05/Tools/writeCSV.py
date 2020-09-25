import csv
import datetime as dt
import os
import os.path

# do not chnage this variables from here change it from WriteToVSC()
# when you create the object
test_fileName = 'test_file.csv'
timeStampFormat = '%d.%m.%Y %H:%M:%S %f'
projectDir = '/'.join(__file__.split('/')[:-2])
csvDirName = 'CSVFiles'
#######################################################################


class WriteToCSV():
    def __init__(self, fileName= test_fileName, workDir= projectDir):
        path_list = workDir.split('/')
        path_list.append(csvDirName)
        path = '/'.join(path_list)
        if not os.path.exists(path):
            os.mkdir(path)
        self.sourceFilePath = path+'/'+fileName

    def WriteJSON(self, *args):
        _data = args
        try:
            with open(self.sourceFilePath, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(_data)
        except Exception as err:
            print(type(err),' >>>  ', err)

    def WriteCSVFormat(self, *args):
        _data = args
        try:
            with open(self.sourceFilePath, 'a',newline='') as file:
                writer = csv.DictWriter(file)
                writer.writerow(_data)
        except Exception as err:
            print(type(err),' >>>  ', err)


    def DT_ToString(self,dt_=dt.datetime.now(), format_=timeStampFormat):
        return dt_.strftime(format_)

if __name__ == '__main__':
    f = WriteToCSV()
    print(f.DT_ToString(dt.datetime.now()))
    test_dict = {'name':'Abdullah','age':42}
    cnt = 0
    for i in range(10000):
        f.WriteJSON(cnt, ' >>>> ', test_dict, f.DT_ToString(dt.datetime.now()))
        cnt +=1
    print('***************** DONE ***************')
    print(f.DT_ToString(dt.datetime.now()))

