#正则表达式regular expression
import re

ping_log = "数据包: 已发送 = 4，已接收 = 0，丢失 = 4 (100% 丢失)"
result = re.findall(r"\d+%",ping_log)
print(result)