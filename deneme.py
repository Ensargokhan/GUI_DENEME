import cv2 as cv
import tkinter as Tk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
#Kamera seçimi yapılıyor
#yorum eklendi.
cap = cv.VideoCapture(0)

class LIHAIHAYerIstasyonu:
    def __init__(self, root):
        self.root = root
        self.root.title("LİHA İHA YER İSTASYONU")
        self.root.geometry("1920x1080")
        self.root.state("zoomed")
        self.root.configure(background="#2C2C2C")
        
        self.create_widgets()
        self.update_frame()
        
    def create_widgets(self):
        self.create_title_frame()
        self.create_camera_frame()
        self.create_map_frame()
        self.create_server_frame()
        self.create_raspberry_frame()
        self.create_connection_frame()
        self.create_drop_cargo_frame()
        self.create_date_time_frame()
        self.create_connection_time_frame()
        self.create_speed_altitude_frame()
        self.create_latitude_longitude_frame()
        self.create_info_box_frame()

    def create_title_frame(self):
        self.title_frame = Tk.Frame(self.root, width=720, height=100,  bg=self.root.cget('bg'), borderwidth=10, relief="sunken")
        self.title_frame.place(x=600, y=10)

        self.title_label = Tk.Label(self.title_frame, text="LİVA İHA YER İSTASYONU", font="Times 20 bold", bg="#2C2C2C", height=2, width=40)
        self.title_label.pack()

    def create_camera_frame(self):
        self.camera_frame = Tk.Frame(self.root, width=688, height=527, bg="#2C2C2C", borderwidth=20, relief="sunken")
        self.camera_frame.place(x=1040, y=254)

        self.camera_label = Tk.Label(self.camera_frame, width=640, height=480, bg="#2C2C2C")
        self.camera_label.pack()

    def create_map_frame(self):
        self.map_frame = Tk.Frame(self.root, width=705, height=530, bg="#2C2C2C", borderwidth=20, relief="sunken")
        self.map_frame.place(x=310, y=252)

        self.map_label = Tk.Label(self.map_frame, width=655, height=480, bg="#2C2C2C")
        self.map_label.pack()

    def create_server_frame(self):
        self.server_frame = Tk.Frame(self.root, width=290, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
        self.server_frame.place(x=340, y=130)

        self.server_ip_label = Tk.Label(self.server_frame, text="Server IP:", font="Times 14 bold", padx=10, pady=10, bg="#2C2C2C", fg="white")
        self.server_ip_label.grid(row=0, column=0)
        self.server_ip = Tk.Label(self.server_frame, text="ip adresi", font="Times 14 bold", bg="white", fg="black")
        self.server_ip.grid(row=0, column=1)
        self.server_port_label = Tk.Label(self.server_frame, text="PORT:", font="Times 14 bold", padx=10, pady=10, bg="#2C2C2C", fg="white")
        self.server_port_label.grid(row=1, column=0)
        self.ports = ["com1", "com2", "com3", "com4", "com5"]
        self.port_combo = Combobox(self.server_frame, values=self.ports, height=3, background="#2C2C2C")
        self.port_combo.grid(row=1, column=1)

    # Diğer frame'lerin oluşturulması fonksiyonları benzer şekilde devam eder.

    def update_frame(self):
        success, frame = cap.read()

        if success:
            rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgtk = ImageTk.PhotoImage(image=img)

            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)

        self.camera_label.after(10, self.update_frame)

if __name__ == "__main__":
    root = Tk.Tk()
    app = LIHAIHAYerIstasyonu(root)
    root.mainloop()