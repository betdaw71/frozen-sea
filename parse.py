import requests 
from bs4 import BeautifulSoup

import csv
 
# def csv_dict_writer(fieldnames, data):
# 	path = "dict_output.csv"
#     with open(path, "w+", newline='') as out_file:
#         writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)

def get_html(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url,headers=headers).text

def get_all_pages():
	arr = []
	for i in range(1,121):
		arr.append('http://hdkino.vip/serialy/?page{}'.format(str(i)))
	return arr

def get_all_articles(html):
	soup = BeautifulSoup(html,'lxml')
	articles_div = soup.find('div', id = 'allEntries').find_all('div',class_='post-film')
	articles = []
	for article in articles_div:
		articles.append(article.find('a').get('href'))
	return articles

def get_info(html):
	soup = BeautifulSoup(html,'lxml')
	try:
		main = soup.find('ul',class_='film-main-info').find_all('li')
		info = []
		information = {'title':'','original_name':'','body':'','rating':0,'iframe':'','ganre':'','img':'',
		'category':'Serials','data':2019,'length':'0','actor':'','director':'','country':'','quolity':'',
		'translation':'','trailer':''}	
		for inf in main:
			info.append(inf.find('span',class_='data-film-text').getText())
		i = soup.find('ul',class_='film-main-info')
		try:
			information['country'] = i.find('span',id='film-page-country').getText()
		except:
			pass
		try:
			information['data'] = i.find('span',id='film-page-year').getText()
		except:
			pass
		try:
			information['length'] = i.find('span',id='film-page-time').getText()
		except:
			pass
		try:
			information['translation'] = i.find('span',id='translate-page').getText()
		except:
			pass
		try:
			information['director'] = i.find('span',id='director-page').getText()
		except:
			pass
		try:
			information['actor'] = i.find('span',id='actors-page').getText()
		except:
			pass
		try:
			genre_str = ''
			ab = i.find('span',id='film-page-genre').find_all('a')
			for i in ab:
				genre_str += i.getText()+','
			information['ganre'] = genre_str 
		except:
			pass
		try:
			information['img'] = str('http://hdkino.vip'+soup.find('div',class_='film-poster').find('img').get('src'))
		except:
			pass

		try:	
			information['title'] = soup.find('h2',class_='main-header').getText()
		except:
			pass
		try:
			information['original_name'] = soup.find('span',id='film-page-original-name').getText()
			bodya = soup.find('div',class_='film-description').find('span').find_all('p')
			bod=''
			for i in bodya:
				bod += i.getText()+'\n'
			information['body'] = bod
		except:
			pass
		try:
			information['iframe'] =  str(soup.find('div',class_='player-output')).replace('&gt;','>').replace('&lt;','<').replace('\n',' ')
		except:
			pass
		try:
			information['trailer'] = str(soup.find('div',id='film-play-list').find('iframe'))
		except:
			pass
	except:
		information = {'title':'','original_name':'','body':'','rating':0,'iframe':'','ganre':'','img':'',
		'category':'Films','data':0,'length':'0','actor':'','director':'','country':'','quolity':'',
		'translation':'','trailer':''}	
	# info.insert(0,soup.find('h2',class_='main-header').getText())
	# a  = str(soup.find('div',class_='player-output')).replace('&gt;','>').replace('&lt;','<').replace('\n',' ')
	# info.append(str('http://hdkino.vip'+soup.find('div',class_='film-poster').find('img').get('src')))
	# info.append(str(soup.find('div',id='film-play-list').find('iframe')))
	# info.append(a)
	# info.append(soup.find('span',id='film-page-original-name').getText())

	return information


def get_all_ganres(html):
	ganrs = []
	soup = BeautifulSoup(html,'lxml')
	g = soup.find('table',class_='catsTable').find_all('tr')
	print(g)
	for i in g:
		print(i)
		ganrs.append(i.find('td',class_='catsTd').find('a',class_='catName').getText())
	return ganrs

def main():
	url = 'http://hdkino.vip/serialy/'
	path = "dict_output1.csv"
	fieldnames = ['title','original_name','body','rating','iframe','ganre','img','category','data','length','actor','director','country','quolity','translation','trailer']
	with open(path, "w+", newline='') as out_file:
		writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
		writer.writeheader()

		urls = get_all_pages()
		for url in urls:
			html = get_html(url)

			articles = get_all_articles(html)

			for article in articles:
				html_article = get_html('http://hdkino.vip'+article)
				print(get_info(html_article))
				writer.writerow(get_info(html_article))




	# ganrs = get_all_ganres(get_html(url))
	# print(ganrs)
	# with open('pared.txt','w') as f:
	# 	for i in ganrs:
	# 		f.write(i+'\n')

if __name__ == '__main__':
	main()