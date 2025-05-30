import wmi
import platform
from datetime import datetime

def collect_system_info(x = '*'):
    computer = wmi.WMI()
    system_info = {}
    system_info['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    system_info['platform'] = platform.system()
    system_info['platform_version'] = platform.version()
    system_info['Cpu Name'] = computer.win32_processor()[0].Name
    system_info['Memory'] = computer.win32_physicalmemory()
    system_info['Gpu Name'] = computer.win32_videocontroller()[0].Name
    if x == '*':
        return system_info
    else:
        return system_info[x]


print(collect_system_info())