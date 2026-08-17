import re
import csv
import os
import platform
import subprocess
from datetime import datetime

import paramiko
import psutil

class MetricsCollector:
    def __init__(self,host=None,port=22,username=None,password=None,key_filename=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.is_remote = bool(host and username)

    def _exec_ssh_command(self,client,command):
        try:
            stdin,stdout,stderr = client.exec_command(command,timeout=5)
            return stdout.read().decode('uft-8',errors='ignore').strip()
        except Exception as e:
            return ""

