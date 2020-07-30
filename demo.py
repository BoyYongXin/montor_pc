import psutil   # pip install psutil

# 获取本机磁盘使用率和剩余空间G信息
def get_disk_info():
    # 循环磁盘分区
    content = ""
    for disk in psutil.disk_partitions():
        # 读写方式 光盘 or 有效磁盘类型
        if 'cdrom' in disk.opts or disk.fstype == '':
            continue
        disk_name_arr = disk.device.split(':')
        disk_name = disk_name_arr[0]
        disk_info = psutil.disk_usage(disk.device)
        # 磁盘剩余空间，单位G
        free_disk_size = disk_info.free//1024//1024//1024
        # 当前磁盘使用率和剩余空间G信息
        info = "%s盘使用率：%s%%， 剩余空间：%iG \n" % (disk_name, str(disk_info.percent), free_disk_size)
        # print(info)
        # 拼接多个磁盘的信息
        content = content + info
    print(content)
    # return content

# cpu信息
def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_info = "CPU使用率：%i%%" % cpu_percent
    print(cpu_info)
    # return cpu_info

# 内存信息
def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = virtual_memory.used/1024/1024/1024
    free_memory = virtual_memory.free/1024/1024/1024
    memory_percent = virtual_memory.percent
    memory_info = "内存使用：%0.2fG，使用率%0.1f%%，剩余内存：%0.2fG" % (used_memory, memory_percent, free_memory)
    print(memory_info)
    # return memory_info
# 内存信息
def get_memory_info2():
    virtual_memory = psutil.virtual_memory()
    virtual_memory_count = bytes2human(virtual_memory.total)
    used_memory = bytes2human(virtual_memory.used)
    free_memory = bytes2human(virtual_memory.free)
    memory_percent = virtual_memory.percent
    memory_info = "总共内存：%s, 内存使用：%s，使用率%0.1f%%，剩余内存：%s" % (virtual_memory_count,used_memory, memory_percent, free_memory)
    print(memory_info)
    # return memory_info

def bytes2human(n):
    """
    内存单位转换
    :param n:
    :return:
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return '%sB' % n

get_disk_info()
get_cpu_info()
# get_memory_info()
get_memory_info2()