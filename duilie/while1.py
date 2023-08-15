# while 循环数据
import socket
count=0
while count<10:
    count+=1
    print("count is :",count)

for letter in 'python':
    print(letter)

s=socket.socket()
host=socket.gethostname()
port=12345
print(host,port)
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print('连接地址:',addr)
    c.send("欢迎菜鸟论文")
    c.close()