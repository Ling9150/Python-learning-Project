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
    stdin,stdout,stderr = ssh.exec_command('show ip')
    result = stdout.read().decode('utf-8')
    print(f"文件:{result}")
except Exception as e:
    res = stderr.read().decode('utf-8')
    print(res)
    print(f"失败:{stderr}")
finally:
    ssh.close()
    print("结束")