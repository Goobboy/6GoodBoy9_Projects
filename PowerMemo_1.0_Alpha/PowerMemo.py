import os
import platform
import psutil
import subprocess
import threading
import socket
import time
import wmi
from tkinter import *
from winotify import Notification, audio

# imp variables
counter = 0
indication = 0
running = False
pause_resume_event = threading.Event()


# imp functions

def more_than_sixty(seconds):
    minute = int(seconds / 60)
    second = int(seconds % 60)

    return f"{minute} min(s) and {second} sec(s)"


# just look at the name of the function:
def main_prog():
    global average_timer_drop, average_timer_gain
    global indication

    battery_check = psutil.sensors_battery().percent
    charge_check = None

    time_counter_drop = 0
    time_counter_gain = 0
    average_counter_for_decreasing = 0
    average_counter_for_increasing = 0
    average_timer_drop = f"Average Time Per Drop(0%): [evaluating]"
    average_timer_gain = f"Average Time Per Drop(0%): [evaluating]"
    drop_time_count = 0  # adds up total time of each percentage of battery draining
    gain_time_count = 0  # add up total time of each percentage of battery gaining
    indication = 0
    flag = True

    def for_performace_window():
        nonlocal flag
        global indication

        while True:
            if flag:
                try:
                    label_unplugged_time.config(text=" Unplugged Duration: - ")
                    label_plugged_time.config(text=" Plugged Duration: - ")
                    label_average_increase.config(text=" Average Time Per Drop: - ")
                    label_average_decrease.config(text=" Average Time Per Rise: - ")
                    flag = False
                    indication = 1
                    pause_resume_event.set()
                    print("try breaking")
                    break
                except:
                    print("except")
                    time.sleep(2)

    once = 0
    while True:

        if not running:
            print("breaking")
            break

        if once == 0:
            threading.Thread(target=for_performace_window, daemon=True).start()
            once = 1

        charged = psutil.sensors_battery().power_plugged
        battery_percent = psutil.sensors_battery().percent

        if charge_check != charged:
            with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                f.write(f"\n\n\nTime: {time.ctime(time.time())}")
                f.write(f"\nCharging: {charged}")
                f.write(f"\nBattery percentage: {battery_percent}%")

            charge_check = charged

            if charged:
                global timer_after_unplugging, timer_after_plugging
                timer_after_plugging = time.time()
                try:
                    how_long_unplugged = round((time.time() - timer_after_unplugging), 2)

                    if how_long_unplugged > 59:
                        in_minute = (more_than_sixty(how_long_unplugged))
                        with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                            f.write(f"\nUnplugged duration: {in_minute}")
                    else:
                        with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                            f.write(f"\nUnplugged duration: {how_long_unplugged} second(s)")

                except:
                    pass

                with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                    f.write(f"\nCurrent status: Plugged! ")

            else:
                timer_after_unplugging = time.time()

                try:
                    how_long_plugged = round((time.time() - timer_after_plugging), 2)

                    if how_long_plugged > 59:
                        in_minute = (more_than_sixty(how_long_plugged))
                        with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                            f.write(f"\nPlugged duration: {in_minute}")
                    else:
                        with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                            f.write(f"\nPlugged duration: {how_long_plugged} second(s)")

                except:
                    pass
                with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                    f.write(f"\nCurrent status: Un-plugged! ")

        if battery_percent != battery_check:
            with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                f.write(f"\n\n\nTime: {time.ctime(time.time())}")
                f.write(f"\nCharging: {charged}")
                f.write(f"\nBattery percentage: {battery_percent}%")

            if battery_percent < battery_check:  # when battery % drops

                average_counter_for_decreasing = average_counter_for_decreasing + (battery_check - battery_percent)
                if average_counter_for_decreasing != 1:
                    drop_time_count = drop_time_count + (time.time() - time_counter_drop)

                    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                        f.write(f"\ntotal drop time:{round(drop_time_count, 2)} seconds")

                time_counter_drop = time.time()
                if (average_counter_for_decreasing - 1) > 0:
                    if drop_time_count / (average_counter_for_decreasing - 1) < 60:
                        average_timer_drop = f"Average Time Per Drop({(average_counter_for_decreasing - 1)}%): {round((drop_time_count / (average_counter_for_decreasing - 1)), 2)} second(s)"

                    else:
                        average_timer_drop = f"Average Time Per Drop({(average_counter_for_decreasing - 1)}%): {more_than_sixty(drop_time_count / (average_counter_for_decreasing - 1))}"

                    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                        f.write(f"\n{average_timer_drop}")

                with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                    f.write(f"\n| Charge dropped by {battery_check - battery_percent}% |")

            elif battery_percent > battery_check:  # when battery % increases

                average_counter_for_increasing = average_counter_for_increasing + (battery_percent - battery_check)
                if average_counter_for_increasing != 1:
                    gain_time_count = gain_time_count + (time.time() - time_counter_gain)
                    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                        f.write(f"\ntotal rise time:{round(gain_time_count, 2)} seconds")

                time_counter_gain = time.time()
                if (average_counter_for_increasing - 1) > 0:
                    if gain_time_count / (average_counter_for_increasing - 1) < 60:
                        average_timer_gain = f"Average Time Per Rise({(average_counter_for_increasing - 1)}%): {round((gain_time_count / (average_counter_for_increasing - 1)), 2)} second(s)"
                    else:
                        average_timer_gain = f"Average Time Per Rise({(average_counter_for_increasing - 1)}%): {more_than_sixty(gain_time_count / (average_counter_for_increasing - 1))}"

                    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                        f.write(f"\n{average_timer_gain}")

                with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
                    f.write(f"\n| Charge increased by {battery_percent - battery_check}% |")

            battery_check = battery_percent


def start_button_clicked():
    global running, status, counter
    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
        f.write(f"\n Program Started!!!")
        f.write(f"\n_______________________________________________________________________________________________")
    running = True
    print("You pressed start")

    if counter < 1:
        threading.Thread(target=main_prog, daemon=True).start()
        counter += 1
        status_label.config(text="Online", foreground="spring green2")
    else:
        print(" !!!main_prog is already in use !!!\n")


def stop_button_clicked():
    global running, status, counter
    print("you pressed stop")
    status = "Offline"
    running = False
    threading.Thread(target=main_prog, daemon=True).start()
    counter = 0
    print("\ncounter changed to 0!!!")
    status_label.config(text="Offline", foreground="firebrick1")

    with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "a") as f:
        f.write(f"\n\n_______________________________________________________________________________________________")
        f.write(f"\n Program Stopped!!!")
        f.write(f"\n_______________________________________________________________________________________________")


def open_running_file():
    os.startfile(rf'c:/PowerMemo/{local_day_date}/{txt_file_time}.txt')


def open_folder():
    os.startfile(r'c:/PowerMemo')


def this_pc_specs():
    if os.path.exists("ecosystems.txt"):
        os.remove("ecosystems.txt")
        print("$$$ txt file deleted $$$")
    else:
        print("The file does not exist")

    # traverse the info
    id_ = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in id_:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        r = (i[2:-2])
        with open("ecosystems.txt", "a") as f:
            f.write("\n" + r)

    os.startfile(r"ecosystems.txt")


def hundred_twenty_notify(battery_fully_notify=None):
    while True:
        time.sleep(3)
        if battery_fully_notify != 1:
            if psutil.sensors_battery().percent == 100:
                toast = Notification(app_id="PowerMemo",
                                     title="Battery Full!",
                                     msg="Battery fully charged!",
                                     duration="short",
                                     icon=fr"{os.getcwd()}\the_logo.png")

                toast.set_audio(audio.IM, loop=False)

                toast.show()
                battery_fully_notify = 1

            elif psutil.sensors_battery().percent <= 20:
                toast = Notification(app_id="PowerMemo",
                                     title="Battery Low!",
                                     msg="Running out of battery, recharge required.",
                                     duration="short",
                                     icon=fr"{os.getcwd()}\the_logo.png")

                toast.set_audio(audio.IM, loop=False)
                toast.show()
                battery_fully_notify = 1
        if battery_fully_notify == 1:
            print("notify break")
            break
        time.sleep(5)


def about_app_window():
    windows_for_features = Toplevel()
    windows_for_features.geometry('970x700')
    windows_for_features.configure(background="gray11")

    list_of_questions = ("1. Navigation Menu:",
                         "2. Battery Notifications:",
                         "3. Documenting and System Information:",
                         "4. Performance window:",
                         "1. What does this app do?",
                         "2. Platform Support:",
                         "3. Future Plans:")

    list_of_answers = ("""-> Access "File" to document information, "Folder" for file storage,
                            "Performance" for real time info and "Specs" for system details.""",

                       "-> Get alerts for low battery (below 20%) and full charge status.",

                       """->  The app currently documents battery draining and gaining times in Notepad.
                         Additionally, it offers functionality to check your computer's specs.""",

                       "-> Real-time CPU, RAM, network usage and exclusive battery insights.",

                       """-> Conveniently track battery use, access specs, receive battery notifications,
                        and monitor performance in real-time.""",

                       """-> The app, built with Python, is compatible with Windows, Linux, and MacOS,
                        although only the Windows version will be released.""",

                       """-> App will evolve with UI enhancements, performance optimization, toggle-able features,
                        and potential Windows optimization feature.""",)

    Label(windows_for_features, text="Features:", background="gray11", foreground="brown3",
          font=("Comic Sans MS", 10)).pack()

    for i in range(len(list_of_questions)):
        Label(windows_for_features, text=list_of_questions[i], background="gray11", foreground="aquamarine3",
              font=("Comic Sans MS", 11)).pack()
        Label(windows_for_features, text=list_of_answers[i], background="gray11", foreground="white",
              font=("Comic Sans MS", 12)).pack()

        if i == 3:
            Label(windows_for_features, text="Questions you may have:", background="gray11", foreground="brown3",
                  font=("Comic Sans MS", 10)).pack()

    Label(windows_for_features, text="""Feel free to suggest additional features you'd like to see in the app,
         or propose ideas for entirely different applications. Constructive criticism is appreciated; however,
          specific feedback will be more valuable in improving the app.""",
          background="gray11",
          foreground="darkorchid3", font=("Comic Sans MS", 13)).pack()
    Label(windows_for_features, text="idea credit(more like requested): xqwalli🎗 #8005 (xqwalli)", background="gray11",
          foreground="grey", font=("Comic Sans MS", 10)).pack()


def get_gb_value(value):
    return round(value // 1024 ** 3, 3)


def get_mb_value(value):
    return round(value // 1024 ** 2, 3)


def performance_window():
    window_for_performance = Toplevel()
    window_for_performance.geometry('450x700')
    window_for_performance.configure(background="gray11")
    window_for_performance.maxsize(450, root_powermemo.winfo_screenheight())
    ############################################################################################################
    # cpu

    Label(window_for_performance, text=f'CPU Info', foreground="aquamarine3", font=15, background="gray15").pack(fill=X)
    Cpu_info_frame = Frame(window_for_performance, background="gray12")

    label_physical_cores = Label(Cpu_info_frame, text=f" Physical cores: {psutil.cpu_count(logical=False)}",
                                 foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_physical_cores.grid(row=1, column=0, sticky='w', pady=0)
    label_total_cores = Label(Cpu_info_frame, text=f" Total cores: {psutil.cpu_count(logical=True)}",
                              font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_total_cores.grid(row=2, column=0, sticky='w')
    label_max_freq = Label(Cpu_info_frame, text=f" Max Frequency: {psutil.cpu_freq().max:.2f}Mhz", foreground="white",
                           font=("Comic Sans MS", 11), background="gray12")
    label_max_freq.grid(row=3, column=0, sticky='w')
    label_current_freq = Label(Cpu_info_frame, text=f" Current Frequency: {psutil.cpu_freq().current:.2f}Mhz",
                               foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_current_freq.grid(row=4, column=0, sticky='w')

    # # threading.Thread(target=core_config, daemon=True).start()

    label_cpu_use = Label(Cpu_info_frame, text=f" Total CPU Usage: {psutil.cpu_percent()}%", foreground="white",
                          font=("Comic Sans MS", 11), background="gray12")
    label_cpu_use.grid(sticky='w')

    Cpu_info_frame.pack(side=TOP, fill=X)

    threading.Thread(target=cpu_real_time, args=(label_cpu_use,), daemon=True).start()
    ###################################################################################################################
    # ram

    Label(window_for_performance, text=f'RAM Info', foreground="aquamarine3", font=15, background="gray15").pack(fill=X)

    ram_info_frame = Frame(window_for_performance, background="gray12")
    label_ram = Label(ram_info_frame, text=f" RAM: {round(psutil.virtual_memory().total / 1024 ** 3, 2)}GB",
                      foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_ram.grid(sticky='w', pady=0)
    label_ram_using = Label(ram_info_frame, text=f" RAM using: {psutil.virtual_memory().percent}%",
                            font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_ram_using.grid(sticky='w')
    label_ram_free = Label(ram_info_frame, text=f" Ram free: {round(100 - psutil.virtual_memory().percent, 1)}%",
                           foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_ram_free.grid(sticky='w')
    ram_info_frame.pack(side=TOP, fill=X)

    threading.Thread(target=ram_real_time, args=(label_ram_using, label_ram_free), daemon=True).start()

    ############################################################################################################
    # disk

    Label(window_for_performance, text=f'Disk Info', foreground="aquamarine3", font=15, background="gray15").pack(
        fill=X)

    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can happen due to the disk that isn't ready
            continue

        used_space = round((partition_usage.percent / 100) * get_gb_value(partition_usage.total), 2)

    disk_info_frame = Frame(window_for_performance, background="gray12")
    label_disk_file_system_type = Label(disk_info_frame, text=f" File system type: {partition.fstype}",
                                        foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_disk_file_system_type.pack(side=TOP, anchor="w")
    label_disk_size = Label(disk_info_frame, text=f" Total Size: {get_gb_value(partition_usage.total)} GB",
                            foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_disk_size.pack(side=TOP, anchor="w")
    label_disk_used = Label(disk_info_frame, text=f" Used: {used_space} GB  ({partition_usage.percent}%)",
                            font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_disk_used.pack(side=TOP, anchor="w")
    label_disk_free = Label(disk_info_frame,
                            text=f" Free: {round(get_gb_value(partition_usage.total) - used_space, 2)} GB",
                            foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_disk_free.pack(side=TOP, anchor="w")
    disk_info_frame.pack(side=TOP, fill=X)

    ############################################################################################################
    # network

    Label(window_for_performance, text=f'Network Info', foreground="aquamarine3", font=15, background="gray15").pack(
        fill=X)

    network_info_frame = Frame(window_for_performance, background="gray12")
    label_IP = Label(network_info_frame, text=f" IP: {socket.gethostbyname(socket.gethostname())}", foreground="white",
                     font=("Comic Sans MS", 11), background="gray12")
    label_IP.grid(sticky='w', pady=0)
    label_bytes_sent = Label(network_info_frame,
                             text=f" Total Bytes Sent: {get_mb_value(psutil.net_io_counters().bytes_sent)} MB",
                             font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_bytes_sent.grid(sticky='w')
    label_bytes_recived = Label(network_info_frame,
                                text=f" Total Bytes Received: {get_mb_value(psutil.net_io_counters().bytes_recv)} MB",
                                foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_bytes_recived.grid(sticky='w')
    network_info_frame.pack(side=TOP, fill=X)

    threading.Thread(target=network_real_time, args=(label_bytes_sent, label_bytes_recived), daemon=True).start()

    ############################################################################################################
    # Battery

    global label_plugged_time, label_unplugged_time, label_average_increase, label_average_decrease

    Label(window_for_performance, text=f'Battery Info  [Documenting]', foreground="aquamarine3", font=15,
          background="gray15").pack(fill=X)

    battery_info_frame = Frame(window_for_performance, background="gray12")

    if psutil.sensors_battery().power_plugged:
        battery_remain_text = "[Charging]"
    else:
        battery_remain_text = more_than_sixty(psutil.sensors_battery().secsleft)

    label_battery_remain = Label(battery_info_frame,
                                 text=f" (Approx.)Battery time remaining: {battery_remain_text}  [start for updates]",
                                 foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_battery_remain.grid(sticky='w', pady=0)
    label_average_decrease = Label(battery_info_frame, text=f" Average Time Per Drop:  [start the program] ",
                                   font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_average_decrease.grid(sticky='w')
    label_average_increase = Label(battery_info_frame, text=f" Average Time Per Rise:  [start the program] ",
                                   foreground="white", font=("Comic Sans MS", 11), background="gray12")
    label_average_increase.grid(sticky='w')
    label_plugged_time = Label(battery_info_frame, text=f" Plugged Duration:  [start the program] ",
                               font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_plugged_time.grid(sticky='w')
    label_unplugged_time = Label(battery_info_frame, text=f" Unplugged Duration:  [start the program] ",
                                 font=("Comic Sans MS", 11), background="gray12", foreground="white")
    label_unplugged_time.grid(sticky='w')
    battery_info_frame.pack(side=TOP, fill=X)

    threading.Thread(target=battery_real_time,
                     args=(label_battery_remain, label_average_decrease, label_average_increase), daemon=True).start()
    threading.Thread(target=plug_unplug_real_time, args=(label_plugged_time, label_unplugged_time), daemon=True).start()


def cpu_real_time(label_cpu_use):
    while True:
        try:
            time.sleep(2)
            label_cpu_use.config(text=f" Total CPU Usage: {psutil.cpu_percent()}%")
        except Exception as e:
            print("\nError:", e, "\t window closed-cpu")
            break


def ram_real_time(label_ram_using, label_ram_free):
    while True:
        try:
            time.sleep(2)
            total_ram = round(psutil.virtual_memory().total / 1024 ** 3, 2)
            using_percent = psutil.virtual_memory().percent
            free_percent = round(100 - using_percent, 1)
            label_ram_using.config(
                text=f" RAM using: {using_percent}%  ({round((using_percent / 100) * total_ram, 2)}GB)")
            label_ram_free.config(
                text=f" Ram free: {free_percent}%  ({round(total_ram - ((using_percent / 100) * total_ram), 2)}GB)")
        except Exception as e:
            print("Error:", e, "\t window closed-ram")
            break


def network_real_time(label_bytes_sent, label_bytes_recived):
    global after_window_closed
    while True:
        try:
            after_window_closed = 0
            time.sleep(3)
            label_bytes_sent.config(text=f" Total Bytes Sent: {get_mb_value(psutil.net_io_counters().bytes_sent)} MB")
            label_bytes_recived.config(
                text=f" Total Bytes Received: {get_mb_value(psutil.net_io_counters().bytes_recv)} MB")


        except Exception as e:
            print("\nError:", e, "\t window closed-network")
            after_window_closed = 1
            break


def battery_real_time(label_battery_remain, label_average_decrease, label_average_increase):
    time.sleep(1)

    if indication == 0:
        pause_resume_event.wait()
        pause_resume_event.clear()
    else:
        pass

    while True:
        time.sleep(1)
        try:
            label_average_increase.config(text=average_timer_gain)
            label_average_decrease.config(text=average_timer_drop)

            battery_time_remaning = psutil.sensors_battery().secsleft

            if not psutil.sensors_battery().power_plugged:
                if battery_time_remaning < 57600:  # all best time for a laptop battery is 16 hours(57600 sec)
                    label_battery_remain.config(
                        text=f" (Approx.)Battery time remaining: {more_than_sixty(battery_time_remaning)}")
                else:
                    label_battery_remain.config(text=" (Approx.)Battery time remaining: [Calculating]")
            else:
                label_battery_remain.config(text=" (Approx.)Battery time remaining: [Charging]")
                pass
            time.sleep(5)
        except Exception as e:
            print("Error:", e, "\t window closed")
            break


def plug_unplug_real_time(label_plugged_time, label_unplugged_time):
    time.sleep(1)

    if indication == 0:
        pause_resume_event.wait()
        pause_resume_event.clear()
    else:
        pass

    while True:
        time.sleep(1)
        try:
            if psutil.sensors_battery().power_plugged:
                label_plugged_time.config(
                    text=f" Plugged Duration: {more_than_sixty(time.time() - timer_after_plugging)}")
            else:
                label_unplugged_time.config(
                    text=f" Unplugged Duration: {more_than_sixty(time.time() - timer_after_unplugging)} ")
        except Exception as e:
            print("\nError:", e, "\t window closed-plug")
            break


root_powermemo = Tk()
root_powermemo.geometry("444x222")

win_width = 444
win_height = 222
root_powermemo.title("PowerMemo")
root_powermemo.configure(bg="gray11")

root_powermemo.eval('tk::PlaceWindow . Center')
root_powermemo.iconbitmap("the_logo.ico")

final_width = (root_powermemo.winfo_screenwidth() // 2) - win_width // 2
final_height = (root_powermemo.winfo_screenheight() // 2) - win_height // 2
root_powermemo.geometry(f"{win_width}x{win_height}+{final_width}+{final_height}")
root_powermemo.maxsize(555, 333)

# custom menu
menu_frame = Frame(root_powermemo, bg="gray14", borderwidth=0, relief=SUNKEN)

file_button = Button(menu_frame, text="Open file", foreground='white', bg="gray14", borderwidth=0,
                     command=open_running_file)
file_button.pack(side=LEFT, pady=1, padx=2)
folder_button = Button(menu_frame, text="Open folder", foreground='white', bg="gray14", borderwidth=0,
                       command=open_folder)
folder_button.pack(side=LEFT, pady=1, padx=2)
Spec_button = Button(menu_frame, text="Specs", foreground='white', bg="gray14", borderwidth=0, command=this_pc_specs)
Spec_button.pack(side=LEFT, pady=1, padx=2)
Performance_window_button = Button(menu_frame, text="Performance", foreground='white', bg="gray14", borderwidth=0,
                                   command=performance_window)
Performance_window_button.pack(side=LEFT, pady=1, padx=2)
About_app_button = Button(menu_frame, text="About app", foreground='white', bg="gray14", borderwidth=0,
                          command=about_app_window)
About_app_button.pack(side=LEFT, pady=1, padx=2)

menu_frame.pack(side=TOP, fill=X)

# the main heading
the_title_img = PhotoImage(file="Powermemo.png")
heading_label = Label(root_powermemo, image=the_title_img, border=0)
heading_label.pack(pady=10)

# Label for Start and Stop
frame_start_stop = Frame(root_powermemo)
frame_start_stop.configure(bg="gray11")
frame_start_stop.pack(side=LEFT, fill=BOTH, expand=True, padx=50)

# start button
Start_button = Button(frame_start_stop, text="Start", activebackground="gainsboro", font=("Comic Sans MS", 15),
                      bg="gray11", foreground="White", border=0, command=start_button_clicked)
Start_button.pack(side=LEFT, padx=30, ipadx=10)

# stop button
Stop_button = Button(frame_start_stop, text="Stop ", activebackground="gainsboro", font=("Comic Sans MS", 15),
                     bg="gray11", foreground="White", border=0, command=stop_button_clicked)
Stop_button.pack(side=RIGHT, padx=30, ipadx=10)

# the_label_before_config
status_label = Label(frame_start_stop, text="Offline", font=("Segoe Print", 11), bg="grey11", foreground="firebrick1",
                     border=0)
status_label.pack(side=BOTTOM)

# for setting up the folder
time_object = time.localtime()
local_day_date = time.strftime("%B-%d-%Y-%A-__PowerMemo Report__", time_object)
txt_file_time = f"launchTime - {time.strftime('%I.%M PM _ %B-%d-%Y-%A-%S')}"

path = f"c:/PowerMemo/{local_day_date}"

if not os.path.exists(path):
    os.makedirs(path)
else:
    print(f"Folder exists: {path}")

with open(f"c:/PowerMemo/{local_day_date}/{txt_file_time}.txt", "x") as f:
    f.write("System Info: ")
    f.write(f"\n\nPlatform: {platform.system()} {platform.uname().release} {platform.win32_edition()}")
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    f.write(f"\nDevice: {my_system.Manufacturer} {my_system.Model} {my_system.SystemType}")
    f.write(f"\nProcessor: {platform.processor()}")
    f.write(f"\nRam: {round(psutil.virtual_memory().total / 1024 ** 3, 2)}GB")
    f.write(f"\n_______________________________________________________________________________________________")

    threading.Thread(target=hundred_twenty_notify, daemon=True).start()

if __name__ == '__main__':
    root_powermemo.mainloop()

# idea credit(more like requested): xqwalli🎗 #8005 (xqwalli)
