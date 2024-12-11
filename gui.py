import tkinter as tk
import psutil
import os


gps = "111.244 23.2387"

humidity = "4%"
temperature = "14 C"
pressure = "13 bars"
weather = "rain oh no"

pry = "pitch, roll, yaw"
magnetic = "True"
acceleration = "west"

time = "5:20"
sun_down_time = "9pm"
sun_up_time = "6am"
date = "01/22/2007"

wifi_usage = "64 kbps"
cpu_use = "2.04 GHz"
memory_usage = "2.8 GB"
cpu_temp = "70 C"


def Weather_SEND():
    print("\n Temperature - " + temperature +"\n air pressure - "+ pressure + "\n humidity - "+ humidity)
def Time_SEND():
    print("\n time - "+ time + "\n sundown - " + sun_down_time +"\n sunup - " + sun_up_time + "\n date - " + date)
def Physics_SEND():
    print("\n acceleration - "+ acceleration + "\n magnetic - " + magnetic +"\n pitch/roll/yaw - " + pry)
def Board_SEND():
    print("\n CPU usage - "+ cpu_use + "\n CPU temp - " + cpu_temp +"\n memory usage - " + memory_usage + "\n wifi - " + wifi_usage)
def SOS_SEND():
    print("\n SOS - EMERGANCY - GPS COORDINATES - \n " + gps)




def main():
    # Create the main window
    root = tk.Tk()
    
    
    # Set the window title
    root.title("wouldn't you like to know weather boy")

    # Get the screen width and height
    screen_width = 1024
    screen_height = 600
    root.geometry("1024x600")
    root.resizable(False, False)

    btn_width = int(screen_width / 6)
    btn_height = int(screen_height / 6)

    # Define section dimensions
    section_width = screen_width // 2
    section_height = screen_height // 3

    # Create sections
    create_section(root, 0, 0, section_width, section_height, "#00A2E8","WEATHER", "temperature - " + temperature,"air pressure - " + pressure, "humidity - " + humidity,"highest chance weather - " + weather)  # weather
    create_section(root, section_width, 0, section_width, section_height,"#FFAEC9", "TIME/SUN INFO", "time - " + time,"sun down - " + sun_down_time, "sun up - " + sun_up_time,"date - " + date)  # time/sun
    create_section(root, 0, section_height, section_width, section_height,"#22B14C", "physics", "pitch, roll, and yaw - " + pry,"magnetic - " + magnetic, "acceleration - " + acceleration,"")  # physics
    create_section(root, section_width, section_height, section_width,section_height,"#FFF200" ,"board info", "CPU - " + cpu_use,"MEMORY - " + memory_usage, "CPU temp - " + cpu_temp,"wifi - " + wifi_usage)  # board info
    send_sect(root, 0, 2 * section_height, screen_width,section_height, "#A349A4", "send information")
    tk.Button(text="WEATHER", width=17, height=10, bg="#00A2E8", fg="#000000", command=Weather_SEND ).place(x=40, y=420)
    tk.Button(text="TIME AND SUN INFO", width=17, height=10, bg="#FFAEC9", fg="#000000", command=(Time_SEND) ).place(x=200, y=420)
    tk.Button(text="PHYSICS", width=17, height=10, bg="#22B14C", fg="#000000", command=(Physics_SEND) ).place(x=360, y=420)
    tk.Button(text="BOARD INFO", width=17, height=10, bg="#FFF200", fg="#000000", command=(Board_SEND) ).place(x=520, y=420)
    tk.Button(text="SOS", width=17, height=10, bg="#ED1C24", fg="#000000", command=(SOS_SEND) ).place(x=680, y=420)
    tk.Button(text="EXIT", width=17, height=10, bg="#FF7F27", fg="#000000").place(x=840, y=420)
    
    # Run the main loop
    root.mainloop()



def create_section(root, x, y, width, height, color, title, text1, text2, text3, text4, button=False):
    section = tk.Frame(root, width=width, height=height, bg=color)
    section.place(x=x, y=y)

    if button:
        make_button(text1, width, height, color).pack(pady=20)
    else:
        label = tk.Label(section, text=title, font=("Helvetica", 42), bg=color, fg="#000000")
        label.place(relx=0.1, rely=0.18, anchor="w")

    label = tk.Label(section, text=text1, font=("Helvetica", 14), bg=color, fg="#000000")
    label.place(relx=0.1, rely=0.4, anchor="w")
    label = tk.Label(section, text=text2, font=("Helvetica", 14), bg=color, fg="#000000")
    label.place(relx=0.1, rely=0.5, anchor="w")
    label = tk.Label(section, text=text3, font=("Helvetica", 14), bg=color, fg="#000000")
    label.place(relx=0.1, rely=0.6, anchor="w")
    label = tk.Label(section, text=text4, font=("Helvetica", 14), bg=color, fg="#000000")
    label.place(relx=0.1, rely=0.7, anchor="w")


def send_sect(root, x, y, width, height, color, title):
    section = tk.Frame(root, width=width, height=height, bg=color)
    section.place(x=x, y=y) 

   
if __name__ == "__main__":
    main()
