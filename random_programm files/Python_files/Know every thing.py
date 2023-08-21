import platform, socket, uuid, psutil
import time
import wmi
import GPUtil

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system.Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")

print(f"\n\nPython version: {platform.python_version()}")
print(f"Platform: {platform.system()}")
print(f"edition: {platform.win32_edition()}")
print(f"processor: {platform.processor()}")
print(f"Something: {platform.uname()}")
print(f"machine{platform.architecture()}")
print(f"machine{platform.architecture()}")
archi = platform.architecture()
print(archi[0])

print(f"\n\nhostname: {socket.gethostname()}")
print(f"IP: {socket.gethostbyname(socket.gethostname())}")
print(f"Mac Address: {uuid.getnode()}")
print(f"DNS or something: {uuid.NAMESPACE_DNS}")

print(f"\n\nRAM: {round(psutil.virtual_memory().total / 1024 ** 3, 2)}GB")
print(f"RAM using: {psutil.virtual_memory().percent}%")
print(f"Ram free: {round(100 - psutil.virtual_memory().percent, 1)}%\n\n")
# print(f"RAM: {psutil.virtual_memory()}\n\n")


# let's print CPU information
print("=" * 40, "CPU Info", "=" * 40)
# number of cores
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Total cores: {psutil.cpu_count(logical=True)}")
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {psutil.cpu_freq().max:.2f}Mhz")
print(f"Min Frequency: {psutil.cpu_freq().min:.2f}Mhz")
print(f"Current Frequency: {psutil.cpu_freq().current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")

print(f"Total CPU Usage: {psutil.cpu_percent()}%\n\n")




def get_gb_value(value):
    return round(value // 1024 ** 3, 3)


# Disk Information
print("=" * 40, "Disk Information", "=" * 40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_gb_value(partition_usage.total)} GB")
    print(f"  Used: {get_gb_value(partition_usage.used)} GB")
    print(f"  Free: {get_gb_value(partition_usage.free)} GB")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_gb_value(disk_io.read_bytes)} GB")
print(f"Total write: {get_gb_value(disk_io.write_bytes)} GB\n\n")

spaces = "   "
end = time.ctime(time.time() + 100)
bar = "█"

# while True:
#     cpu_usage = psutil.cpu_percent()
#     print(f"\rCPU usage: {cpu_usage}% ", end="")
#     print(f"{bar*int(cpu_usage)}",end="")
#     time.sleep(1)
#     if end < time.ctime():
#         print("█"*50)
#         break


# import torch
# print(GPUtil.getAvailable())
# print(torch.cuda.is_available())


# print(f"{psutil.net_if_stats()}\n")
# print(f"{psutil.net_if_addrs()}")



