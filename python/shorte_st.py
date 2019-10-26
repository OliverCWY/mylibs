import requests
headers = {
    'public-api-token': '6604e5a89c06785e48fd82b7f9106e44',
}

def shorten(url,output=False):
	data = {
	  'urlToShorten': url
	}
	response = requests.put('https://api.shorte.st/v1/data/url', headers=headers, data=data).json()
	if(output):
		print(url)
		print(response)
	if response['status']=='ok':return response['shortenedUrl']
	else:return ''

def shortenUrls(urls,output=False):
	return [shorten(i,output) for i in urls]

import string
def shortenText(text,output=False):
	urls=[]
	valid=string.digits+string.ascii_letters+".?/=,#-+|$@*:"
	i=text.find("http")
	while(i!=-1):
		url=""
		while(i<len(text) and text[i] in valid):
			url+=text[i]
			i+=1
		urls.append(url)
		i=text.find("http",i)
	shortened=shortenUrls(urls,output)
	for i in range(len(urls)):
		text=text.replace(urls[i],shortened[i])
	return text;

def inputText(output=False):
	text=""
	inp=input()
	while(inp!=""):
		text+=inp+"\n"
		inp=input()
	return shortenText(text,output)
