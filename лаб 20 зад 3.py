from urllib.parse import urlunparse

sborca = ('https', '//www.bbc.com', '/news/world-us-canada-67770912', '', '', '')
# Собираем URL обратно в строку
url = urlunparse(sborca)
print(url)