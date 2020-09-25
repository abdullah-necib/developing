from Tools import writeCSV
import csv
import json


class ReadCSV():
    def __init__(self, fileName='countries.csv', workDir=writeCSV.projectDir):
        self.sourceFile = workDir + '/CSVFiles/' + fileName
        # print('from READ CSV')
        # print(self.sourceFile)
        self._data = []

    def GetCountriesData(self):
        with open(self.sourceFile, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                # we choose row[0] because csv row is divieded by comma (,) as list
                # so the row is [ first, second, third, ...and so on]
                # my data is only one item as json item
                self._data.append(json.loads(row[0]))
                # print('hhhhh    ',type(row[0]),json.loads(row[0]))
        return self._data

if __name__ == '__main__':
    test = ReadCSV()
    _data = test.GetCountriesData()
    for i in _data:
        print(i)