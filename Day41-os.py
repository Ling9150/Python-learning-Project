import os
print(f"我现在的位置是{os.getcwd()}") #我在哪？
files = os.listdir('.')
print(files)
os.makedirs("test_dir",exist_ok=True)
base_dir = "Network_Logs"
today = "2026-04-18"
target_path = f"{base_dir}/{today}"
r = os.path.exists(target_path)
if r == True:  #也可以是if r：
    print("已存在")
else:
    os.makedirs(target_path)
    print("文件夹已就绪")

