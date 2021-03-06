import socket


def main():
    # 1. 买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("", 7890))

    # 3. 将手机设置正常的响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    while True:
        print("等待客户端连接")
        # 4. 等待别人的电话到来（等待客户端的连接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("客户端已连接%s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端发送过来的请求：%s" % recv_data.decode("utf-8"))

        # 回送一部分数据给客户端
        new_client_socket.send("ok".encode("utf-8"))

        # 关闭套接字
        # 关闭accept返回套接字意味着不会再为这个客户端服务
        new_client_socket.close()
        print("已经完成连接")
        
    # 如果将监听套接字关闭了，那会导致不能再次等待新的客户端的连接，即xxx.accept就会失败    
    tcp_server_socket.close()

if __name__ == "__main__":
    main()