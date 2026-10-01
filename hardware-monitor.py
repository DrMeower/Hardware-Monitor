# Hardware Monitor
import psutil
# CPU Info
cpu_usage = psutil.cpu_percent(interval=1)
cpu_logical_processors = psutil.cpu_count()
cpu_physical_cores = psutil.cpu_count(logical=False)
cpu_frequency = psutil.cpu_freq()

# Memory Info
ram_usage = psutil.virtual_memory()

# Disk
disk = psutil.disk_usage(r"C:\\")
io = psutil.disk_io_counters()


selected_program = input("Which program do you want to start?\n"
                         "\n"
                         "1. Hardware Monitor\n"
                         "2. Process Viewer\n")


if selected_program == "1":
    print(f"""
    ================
    Hardware Monitor
    ================
    CPU
        CPU Usage: {cpu_usage}
        CPU Frequency: {cpu_frequency}MHz
        CPU Cores: {cpu_physical_cores}
        CPU Threads: {cpu_logical_processors}

    Memory
        Total RAM: {ram_usage.total / (1024 ** 3):.2f} GB
        Used: {ram_usage.percent}% {ram_usage.used / (1024 ** 3):.2f} GB
        Available: {ram_usage.available / (1024 ** 3):.2f} GB

    Disk
        Total Disk Space: {disk.total / (1024 ** 3):.2f} GB
        Disk Space Used: {disk.used / (1024 ** 3):.2f} GB {disk.percent}%
        Free Disk Space: {disk.free / (1024 ** 3):.2f} GB
        Read: {io.read_bytes}
        Write: {io.write_bytes}

    Network
    """)

    # Network Info
    for interface, addresses in psutil.net_if_addrs().items():
        print("\nInterfaces: ", interface)

        for address in addresses:
            print("Adresses: ", address.address)

    # Battery Info
    print("\nBattery")

    battery = psutil.sensors_battery()

    if battery:
        print("     Battery Percentage: ", battery.percent)
        if battery.power_plugged:
            print("     Charging/Plugged In")
        else:
            print("     Not Plugged in.")


# PID Section

if selected_program == "2":

    for process in psutil.process_iter(["pid", "name"]):
        print(process.info)
