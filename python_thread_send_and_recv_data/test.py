import socket
import threading

def fa(udp_socket,recv_ip,recv_data):
    # 3 发送信息
    while True:
        data = input("输入你要发送的数据：")
        udp_socket.sendto(data.encode("utf-8"),(recv_ip,recv_data))
def shou(udp_socket):
    # 4接收数据
    while True:
        user_data = udp_socket.recvfrom(1024)
        a = user_data[0]
        b = user_data[1]
        print("用户:%s发来的数据为:%s" % (str(b), a.decode("utf-8")))
def main():
    # １创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2 绑定本地信息
    udp_socket.bind(("",7892))
    recv_ip = input("输入对方ip:")
    recv_data = int(input("输入对方端口："))

    t1 = threading.Thread(target=fa,args=(udp_socket,recv_ip,recv_data))
    t2 = threading.Thread(target=shou,args=(udp_socket,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
