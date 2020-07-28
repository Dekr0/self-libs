#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
需修复和优化：
1. 异常处理
2. 上传和下载
3. 多余的交互和逻辑判断
4. 代码外观
"""

import bar
import json
import os
import struct
import socket
import sys
from tqdm.utils import CallbackIOWrapper

USERDATAS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'usersdata')
BUFFER_SIZE = 1024

class Client:

    def __init__(self, args):
        self.r_args = args
        self.rscdict = {
            10: 'Success',
            30: 'This field is required',
            31: 'Arguments required',
            41: 'Not enough arguments',
            42: 'Invalid formatting',
            43: 'This is not a built-in command',
            44: 'Invalid port',
            45: 'Incorrect respond',
            404: '',
            408: 'Requested Timeout',
        }
        self.__arg_parse()
        self.__handle()

    def __arg_parse(self):
        """
        解析传入的参数
        :return:
        """
        if self.r_args:
            try:
                p_args = self.r_args[1:6]
            except IndexError:
                self.__statushandler(41)
                sys.exit()
            else:
                if '-i' in p_args and '-p' in p_args:
                    if hasattr(self, p_args[0]):
                        func = getattr(self, p_args[0])
                        try:
                            self.ip = p_args[p_args.index('-i') + 1]
                            self.port = int(p_args[p_args.index('-p') + 1])
                        except ValueError:
                            self.__statushandler(44)
                            sys.exit()
                        else:
                            func()
                    else:
                        self.__statushandler(43)
                        sys.exit()
                else:
                    self.__statushandler(42)
                    sys.exit()
        else:
            self.__statushandler(31)
            sys.exit()

    def __auth(self):
        """
        用户名和密码验证
        :return:
        """
        auth = 0

        # 获取登录用户的用户名和密码
        usr = input("Username: ").strip()
        if not usr:
            self.__statushandler(30)
            return 0

        pwd = input("Password: ").strip()
        if not pwd:
            self.__statushandler(30)
            return 0

        # json序列化登录用户信息字典，并发送
        self.socket.sendall(bytes("auth|{}".format(json.dumps({"usr": usr, "pwd": pwd})), encoding='utf-8'))

        # 接收用户名存在的返回值，密码正确的返回值
        status, respond = str(self.socket.recv(BUFFER_SIZE), encoding='utf-8').split(':', 1)
        if status == '21':
            self.cusr = usr
            self.cwd = '~'
            auth = 1

        print('{}: {}'.format(status, respond))
        return auth

    def __connect(self):
        """
        服务器连接
        :return:
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
        except (TimeoutError, socket.gaierror, ConnectionRefusedError) as ex:
            sys.exit('Failed to connect server: {}'.format(ex))

    def __handle(self):
        """
        处理程序的运转步骤
        :return:
        """
        if self.__auth():
            try:
                self.__shell()
            except KeyboardInterrupt:
                print("Forced to exit")
        sys.exit(0)

    def __shell(self):
        while True:
            command = input('{}:{}$ '.format(self.cusr, self.cwd)).strip()
            if not command:
                continue
            func = command.split()[0]
            if func in ['exit', 'quit']:
                self.socket.sendall(bytes(func, encoding='utf-8'))
                self.socket.close()
                break
            if hasattr(self, func):
                if len(command.split()) == 1:
                    self.socket.sendall(bytes(command.replace(func, func + '|'), encoding='utf-8'))
                else:
                    self.socket.sendall(bytes(command.replace(func + ' ', func + '|'), encoding='utf-8'))
                func = getattr(self, func)
                func()
            else:
                self.__statushandler(43)

    def __statushandler(self, rsn):
        print('{}: {}'.format(rsn, self.rscdict[rsn]))

    def cd(self):
        pass

    def cmd(self):
        status, respond = self.socket.recv(BUFFER_SIZE).decode().split(':', 1)
        if status == '33' or status == '34':
            print('{}:{}'.format(status, respond))
        elif status == '0':
            header_struct = self.socket.recv(4)
            unpack_header = struct.unpack('i', header_struct)
            total_size = unpack_header[0]
            has_recv = 0
            total_data = b''
            while has_recv < total_size:
                fetch_data = self.socket.recv(BUFFER_SIZE)
                has_recv += len(fetch_data)
                total_data += fetch_data
            print(str(total_data, encoding='utf-8', errors='ignore'))

    def download(self):
        pass

    def register(self):
        """
        注册界面
        :return:
        """
        self.__connect()

        # 获取注册用户名和密码， 并将其储存到字典内
        usr = input("Username: ").strip()
        if not usr:
            self.__statushandler(30)
            sys.exit(30)

        pwd = input("Password: ").strip()
        if not pwd:
            self.__statushandler(30)
            sys.exit(30)

        # json序列化注册信息字典，并发送
        self.socket.sendall(bytes("register|{}".format(json.dumps({"usr": usr, "pwd": pwd})), encoding='utf-8'))

        status, respond = self.socket.recv(BUFFER_SIZE).decode().split(':', 1)  # 从服务端获取用户存在的返回值

        if status != '30':
            userdata_dir = os.path.join(USERDATAS_DIR, usr)
            if not os.path.exists(userdata_dir):
                os.makedirs(userdata_dir)

        self.socket.close()
        sys.exit('{}: {}'.format(status, respond))

    def start(self):
        """
        登录界面
        :return:
        """
        self.__connect()

    def upload(self):
        """
        可扩展：在不终止双方连接的情况下进行上传暂停
        :return:
        """
        # 交互1，接收参数格式正确值
        status, respond = self.socket.recv(BUFFER_SIZE).decode().split(':', 1)

        # 刷新缓冲区 - 1
        self.socket.sendall(b'Reset Buffer')

        if status != '34':
            # 交互2，接收当前文件路径
            local_path = self.socket.recv(BUFFER_SIZE).decode()

            # 如果所上传的文件在本机存在，获取所发送的本机文件的大小
            if os.path.exists(local_path):
                file_total_size = os.stat(local_path).st_size

                # 交互3，向服务端发送文件大小
                self.socket.sendall(bytes('{}|{}'.format(1, file_total_size), encoding='utf-8'))

                # 交互4
                status, respond = self.socket.recv(BUFFER_SIZE).decode().split(":", 1)

                # 刷新缓冲区 - 2
                self.socket.sendall(b'Reset Buffer')

                if status != "35":
                    # 交互5
                    exist = self.socket.recv(BUFFER_SIZE).decode()  # 出现粘包现象

                    # 刷新缓冲区 - 3
                    self.socket.sendall(b'Reset Buffer')

                    has_sent = 0

                    pbar = bar.ModifiedTqdm(total=file_total_size, desc="Uploading {} ({})".format(
                        os.path.basename(local_path), bar.ModifiedTqdm.size_convert(file_total_size)),
                                            bar_format="{desc} {total_time}: {percentage:.0f}%|{bar}{r_bar}", unit="B",
                                            unit_scale=True, unit_divisor=BUFFER_SIZE)
                    file = open(local_path, 'rb')
                    callback = CallbackIOWrapper(pbar.update, file, "read")

                    if exist == "3061":
                        # 交互6
                        same, respond = self.socket.recv(BUFFER_SIZE).decode().split(":", 1)
                        if same != "36":
                            # 选择重新上传或继续上传
                            resume = input("\n1. Re-upload the file\n2. Continue to upload: ").strip()

                            if resume == '1':
                                # 重新上传，交互7
                                self.socket.sendall(bytes("3062", encoding='utf-8'))

                                # 刷新缓冲区 - 4
                                self.socket.recv(BUFFER_SIZE).decode()

                                # 发送头报，即所需上传文件的大小，避免粘包，交互8
                                header_struct = struct.pack('i', file_total_size)
                                self.socket.sendall(header_struct)

                                # 上传文件，交互9
                                while has_sent < file_total_size:
                                    data = callback.read(BUFFER_SIZE)
                                    if not data:
                                        break
                                    self.socket.sendall(data)

                            elif resume == '2':
                                # 继续上传，交互7
                                self.socket.sendall(bytes("3063", encoding='utf-8'))

                                # 刷新缓冲区 - 4
                                self.socket.recv(BUFFER_SIZE).decode()

                                # 尚未上传完成的文件的大小，交互8
                                has_sent = int(self.socket.recv(BUFFER_SIZE).decode())

                                pbar.n = has_sent
                                file.seek(has_sent)
                                while has_sent < file_total_size:
                                    data = callback.read(BUFFER_SIZE)
                                    if not data:
                                        break
                                    self.socket.sendall(data)
                            else:
                                # 错误选择，中断交互
                                self.__statushandler(45)
                        else:
                            print("{}:{}".format(same, respond))
                    else:
                        # 不存在，直接传

                        # 发送头报，避免粘包，交互6
                        header_struct = struct.pack('i', file_total_size)
                        self.socket.sendall(header_struct)

                        # 上传文件数据，交互7
                        while has_sent < file_total_size:
                            data = callback.read(BUFFER_SIZE)
                            if not data:
                                break
                            self.socket.sendall(data)
                    file.close()
                else:
                    print("{}:{}".format(status, respond))
            else:
                self.socket.sendall(bytes("{}|{}".format(0, 0), encoding='utf-8'))
                print("File not existed")
        else:
            print("{}:{}".format(status, respond))
