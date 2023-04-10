import tkinter as tk
import threading
import pyautogui
import time

class AutoClickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Auto Clicker")

        self.time_label = tk.Label(master, text="Enter time between clicks:")
        self.time_label.pack()

        self.time_frame = tk.Frame(master)
        self.time_frame.pack()

        self.time_entry = tk.Entry(self.time_frame, width=10)
        self.time_entry.pack(side=tk.LEFT)

        self.time_unit = tk.StringVar(value="seconds")
        self.time_menu = tk.OptionMenu(self.time_frame, self.time_unit, "milliseconds", "seconds", "hours")
        self.time_menu.pack(side=tk.LEFT)

        self.start_button = tk.Button(master, text="Start", command=self.start_auto_clicker)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_auto_clicker)
        self.stop_button.pack()

        self.running = False
        self.delay_time = 1.0

    def start_auto_clicker(self):
        time_units = {
            "milliseconds": 0.001,
            "seconds": 1.0,
            "hours": 3600.0,
        }
        self.delay_time = float(self.time_entry.get()) * time_units[self.time_unit.get()]
        self.running = True
        t = threading.Thread(target=self.auto_clicker)
        t.start()

    def stop_auto_clicker(self):
        self.running = False

    def auto_clicker(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.delay_time)

root = tk.Tk()
my_gui = AutoClickerGUI(root)
root.mainloop()
