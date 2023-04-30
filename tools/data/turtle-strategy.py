#https://zhuanlan.zhihu.com/p/111011337
#pip3 install tushare
#pip3 install lxml pandas requests bs4

import tushare as ts
#设置ts令牌
ts.set_token('cc565ac3e2c4d369ce20ae45e771857fd622b85aeebe1d')
#300274为股票代号，直接通过get_hist_data()获取的数据是逆序的，正序数据需要加上sort.index()
data=ts.get_hist_data('300274',start='2022-01-01',end='2022-12-31').sort_index()
print(data)
#选择需要标签存储股票数据
data.to_csv('C:/Users/himdd/code/backtrader/datas/testbacktrader/tushare/300274.csv',
columns=['open','high','low','close','volume'])
#data.to_csv('C:/testbacktrader/tushare/300274.csv')