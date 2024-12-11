import tkinter as tk  # Import the Tkinter library
from sense_hat import SenseHat
import time
import sys
import requests
import psutil
import requests  # For weather API
import json  # For processing weather API response
from gpiozero import CPUTemperature  # For CPU temperature
import meshtastic


def get_weather(temperature, humidity, pressure):
    if humidity > 80 and temperature < 32:
        return "Snowing"
    elif humidity > 80 and temperature >= 32:
        return "Raining"
    elif humidity <= 80 and pressure < 1000:
        return "Raining"
    else:
        return "Clear"
    

def Weather_SEND(temperature, pressure, humidity):
    data = {
        "type": "weather",
        "temperature": temperature,
        "pressure": pressure,
        "humidity": humidity
    }
    send_data(data)

def Time_SEND(current_time, sun_down_time, sun_up_time, date):
    data = {
        "type": "time",
        "current_time": current_time,
        "sun_down_time": sun_down_time,
        "sun_up_time": sun_up_time,
        "date": date
    }
    send_data(data)

def Physics_SEND(acceleration, magnetic, pry):
    data = {
        "type": "physics",
        "acceleration": acceleration,
        "magnetic": magnetic,
        "pry": pry
    }
    send_data(data)

def Board_SEND(cpu_use, cpu_temp, memory_usage, wifi_usage):
    data = {
        "type": "board",
        "cpu_use": cpu_use,
        "cpu_temp": cpu_temp,
        "memory_usage": memory_usage,
        "wifi_usage": wifi_usage
    }
    send_data(data)

def SOS_SEND(gps):
    data = {
        "type": "sos",
        "gps": gps
    }
    send_data(data)

def send_data(data):
    try:
        response = requests.post(lora_t_beam_endpoint, json=data)
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {str(e)}")

def main():
    sense = SenseHat()
    
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    fahrenheit = (1.8 * temperature) + 32
    STANDARD_PRESSURE = 1013.25
    LAPSE_RATE = 0.0065
    altitude = (STANDARD_PRESSURE - pressure) / LAPSE_RATE
    magnetic = sense.get_compass_raw()['x']  # Use the appropriate method for your magnetic data

    acceleration = sense.get_accelerometer_raw()
    acceleration_x = acceleration['x']
    acceleration_y = acceleration['y']
    acceleration_z = acceleration['z']

    current_time = time.ctime()

    # WiFi Usage - Example using psutil to get total bytes sent and received
    net_io = psutil.net_io_counters()
    wifi_usage = f"Sent: {net_io.bytes_sent}, Received: {net_io.bytes_recv}"

    cpu_use = psutil.cpu_percent(interval=1)

    # CPU Temperature - Using gpiozero for Raspberry Pi 3B+
    cpu_temp_sensor = CPUTemperature()
    cpu_temp = f"{cpu_temp_sensor.temperature} C"

    weather = get_weather(temperature, humidity, pressure)

    orientation = sense.get_orientation()
    p = orientation["pitch"]
    r = orientation["roll"]
    y = orientation["yaw"]
    pry = p, r, y

    modification_time = time.time()
    local_time = time.ctime(modification_time)
    gps = "input the coordinates of your station" #REQUIRES INPUT
    root.mainloop()  # I moved this line to the end of the main function as it was not properly indented in the original code

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
    # Create the main window
    root = tk.Tk()

    # Set the window title
    root.title("Wouldn't you like to know weather boy")

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
    create_section(root, 0, 0, section_width, section_height, "#00A2E8", "WEATHER", "temperature - " + str(temperature), "air pressure - " + str(pressure), "humidity - " + str(humidity), "highest chance weather - " + str(weather))  # weather
    create_section(root, section_width, 0, section_width, section_height, "#FFAEC9", "TIME/SUN INFO", "time - " + time, "sun down - " + sun_down
