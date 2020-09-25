import wx
import Tools.readCSV as read

class CountriesTree(wx.TreeCtrl):
    def __init__(self, *args, **kwargs):
        wx.TreeCtrl.__init__(self, *args, **kwargs)
        self.root = self.AddRoot('ALL')

        # self.add
        self.SetTreeCountries()
        self.Expand(self.root)

    def SetTreeCountries(self):
        _data = read.ReadCSV().GetCountriesData()
        for cnt in _data:
            country = self.AppendItem(self.root,cnt['iso2'])
            # print(cnt)
            for details in cnt:
                if details in ['country','country_code','iso3','population','are','gdp']:
                    self.AppendItem(country,details +': '+str(cnt[details]))
                elif details == 'cities':
                    cities = self.AppendItem(country,'cities')
                    for city in cnt[details]:
                        self.AppendItem(cities,city +': '+str(cnt[details][city]))
                    # print(cnt[details])


        pass


