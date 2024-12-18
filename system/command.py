#执行linux系统命令
import os
import subprocess
import sys
import asyncio,threading
from typing import Callable
import logging
import time

#打开终端端口执行命令
def open_terminal_execute_cmd(cmd):
    try:
        print("execute cmd:"+cmd)
        #bash避免终端关闭
        subprocess.Popen("xterm -T mininet -e '"+cmd+"; bash'", shell=True)  # Linux系统
        return True
    except Exception as e:
        print(e)
        return False
def open_gnome_terminal_execute_cmd(cmd):
    try:
        print("execute cmd:"+cmd)
        #bash避免终端关闭
        subprocess.Popen("gnome-terminal -t Mininet -e \"bash -c '"+cmd+"; exec bash'\"", shell=True)  # Linux系统
        return True
    except Exception as e:
        print(e)
        return False
    
#同步执行指令
def execute_cmd(cmd,wait_time = None):
    try:
        if wait_time != None:
            time.sleep(wait_time)
        print("execute cmd:"+cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        result = p.stdout.read().decode('utf-8')
        logging.info("execute result:"+result)
        return result
    except Exception as e:
        print(e)
        return None
#执行指令不等待返回
def execute_cmd_nowait(cmd):
    try:
        print("execute cmd:"+cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except Exception as e:
        print(e)
def execute_cmd_list_sync(cmd_list):
    """
        按顺序执行命令组
    """
    for cmd in cmd_list:
        execute_cmd(cmd)
def execute_cmd_list_thread(cmd_list):
    try:
        thread = threading.Thread(target=execute_cmd_list_sync, args=(cmd_list,), daemon=True).start()
        return thread
    except Exception as e:
        logging.info(e)
        return None
def execute_cmd_thread(cmd,wait_time = None):
    try:
        thread = threading.Thread(target=execute_cmd, args=(cmd,wait_time,), daemon=True).start()
        return thread
    except Exception as e:
        logging.info(e)
        return None
