import os
import datetime
base_dir = "Network_Logs"
today = "2026-04-24"
target_path = os.path.join(base_dir,today) #拼接
print(target_path)
real_today = str(datetime.date.today())
print(real_today)