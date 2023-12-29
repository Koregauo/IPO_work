from urllib.parse import urlparse

url=urlparse ('//www.bbc.com/news/world-us-canada-67770912')
url._replace(scheme='https')#здесь мы должны были добавить протокол, но он не выводится, так же как и на лекции не работает
print(url)