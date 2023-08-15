
import requests
from bs4 import BeautifulSoup

# 目标网页的URL
url = 'https://blog.csdn.net/weixin_39699121/article/details/109941706#:~:text=with%20open%20%28%27file1%27%29%20as%20f1%3A%20with%20open%20%28%27file2%27%29,%28filename3%2C%20%27rb%27%29%20as%20fp3%3A%20for%20i%20in%20fp'

# 发送GET请求
response = requests.get(url)
print(response.text)

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有的<a>标签
print(soup)
links = soup.find_all('a')
print(links)
# 打印所有的链接
for link in links:
    print(link.get('href'))


