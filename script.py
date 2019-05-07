from film_article.models import Article,Genre,Category
import csv
import requests

with open('dict_output2.csv','r',newline='') as file:
	reader = csv.reader(file,delimiter=',')
	i = False
	for row in reader:
		if i == True:
			genres = []
			for i in row[5].split(','):
				try:
					genres.append(Genre.objects.get(title=i))
				except:
					pass
			
			try:
				p = requests.get(row[6])
				a = '/home/betdav71/Рабочий стол/proj/cinema/media/%s.jpg'%(str(row[1]).replace(' ','_').replace('/','-'))
				n = '/media/%s.jpg'%(str(row[1]).replace(' ','_').replace('/','-'))
				out = open(a,'wb')
				out.write(p.content)
				out.close
			except:
				n = '/media/%s.jpg'%(str(row[1]).replace(' ','_').replace('/','-'))
			try:
				leng =int(row[9].strip().split(' ')[0])
			except:
				leng = 0
			cate = Category.objects.get(title='Films')
			artic = Article.objects.create(title=row[0],original_name=row[1],
				body=row[2],rating=row[3],iframe=row[4],img=n,category=cate,
				data=row[8],length=leng,actor=row[10],director=row[11],country=row[12],quolity=row[13],
				translation=row[14],trailer=row[15])

			artic.ganre.set(genres)
		i = True
