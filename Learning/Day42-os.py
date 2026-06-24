import os
import datetime
base_dir = "../Network_Logs"
today = "2026-04-24"
target_path = os.path.join(base_dir,today) #拼接
print(target_path)
real_today = str(datetime.date.today())
print(real_today)
switches = ["Core_SW1","Core_SW2","Access_SW3"]
for switch in switches:
    data = os.path.join(real_today,switch)
    os.makedirs(data,exist_ok=True)
    print(f"已完成{data}的创建")