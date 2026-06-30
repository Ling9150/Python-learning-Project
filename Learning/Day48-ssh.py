import paramiko
ssh = paramiko.SSHClient() #创建客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #关闭拦截
try:
    ssh.connect(
        hostname = 'test.rebex.net',
        port = 22,
        username = 'demo',
        password = 'password',
        timeout = 10
    )
    print("--sucess--")
    stdin,stdout,stderr = ssh.exec_command('ls')
    result = stdout.read().decode('utf-8')
    print(f"文件:{result}")
except Exception as e:
    print(f"失败:{e}")
finally:
    ssh.close()
    print("结束")