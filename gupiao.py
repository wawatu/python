import requests
import re
from bs4 import BeautifulSoup
import traceback

#获取url网页
def getHTMLText(url):
	return""

#获取股票信息列表	
def getStockList(lst, stockURL): #列表类型存储股票的信息，股票URL网站
	return""
	
#获取每只个股信息
def getStockInfo(lst, stockURL, fpath):
	return""
	
	
def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist'
	stock_info_url = 'https://gupiao.baidu.com/stock'
	output_file = 'D://BaiduStockInfo.txt' #保存信息路径
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url)
