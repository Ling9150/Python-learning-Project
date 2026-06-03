import subprocess
result = subprocess.run(['ping','-n','2','114.114.114.114'],capture_output=True,text=True,encoding='gbk')
reply = result.stdout
print("结果：",reply)