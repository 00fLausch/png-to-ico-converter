import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, StringVar, IntVar, Frame
from PIL import Image

def select_input_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder.set(folder)
        label_input.config(text=f"Eingabeordner: {folder}")

def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder.set(folder)
        label_output.config(text=f"Ausgabeordner: {folder}")

def convert_images():
    input_dir = input_folder.get()
    output_dir = output_folder.get()
    if not input_dir or not output_dir:
        label_status.config(text="Bitte wähle beide Ordner aus!")
        return

    png_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]
    total = len(png_files)
    if total == 0:
        label_status.config(text="Keine PNG-Dateien im ausgewählten Eingabeordner gefunden.")
        return

    progress_bar.config(maximum=total)
    progress_bar.config(value=0)

    # Festlegen der Icon-Größen anhand der Checkboxen
    sizes = []
    if var16.get():
        sizes.append((16, 16))
    if var32.get():
        sizes.append((32, 32))
    if var48.get():
        sizes.append((48, 48))
    if var64.get():
        sizes.append((64, 64))
    if var128.get():
        sizes.append((128, 128))
    if var256.get():
        sizes.append((256, 256))
    if not sizes:
        sizes = [(32, 32)]  # Fallback falls nichts ausgewählt wurde

    for count, file in enumerate(png_files, start=1):
        input_path = os.path.join(input_dir, file)
        output_filename = os.path.splitext(file)[0] + ".ico"
        output_path = os.path.join(output_dir, output_filename)
        try:
            img = Image.open(input_path)
            if img.mode != "RGBA":
                img = img.convert("RGBA")
            img.save(output_path, format="ICO", sizes=sizes)
        except Exception as e:
            print(f"Fehler bei {file}: {e}")
        progress_bar.config(value=count)
        window.update_idletasks()

    label_status.config(text="Konvertierung abgeschlossen!")

# Hauptfenster mit dunklem Theme
window = ttk.Window(themename="darkly")
window.title("PNG zu ICO Converter")

input_folder = StringVar()
output_folder = StringVar()

# Eingabeordner auswählen
ttk.Button(window, text="Eingabeordner auswählen", command=select_input_folder).pack(pady=5)
label_input = ttk.Label(window, text="Kein Eingabeordner ausgewählt")
label_input.pack()

# Ausgabeordner auswählen
ttk.Button(window, text="Ausgabeordner auswählen", command=select_output_folder).pack(pady=5)
label_output = ttk.Label(window, text="Kein Ausgabeordner ausgewählt")
label_output.pack()

# Optionen: Icon-Größen
size_frame = Frame(window)
size_frame.pack(pady=10)
ttk.Label(size_frame, text="Icon-Größen auswählen:").pack(anchor="w")

var16 = IntVar(value=1)
ttk.Checkbutton(size_frame, text="16x16", variable=var16).pack(anchor="w")
var32 = IntVar(value=1)
ttk.Checkbutton(size_frame, text="32x32", variable=var32).pack(anchor="w")
var48 = IntVar(value=1)
ttk.Checkbutton(size_frame, text="48x48", variable=var48).pack(anchor="w")
var64 = IntVar(value=0)
ttk.Checkbutton(size_frame, text="64x64", variable=var64).pack(anchor="w")
var128 = IntVar(value=0)
ttk.Checkbutton(size_frame, text="128x128", variable=var128).pack(anchor="w")
var256 = IntVar(value=0)
ttk.Checkbutton(size_frame, text="256x256", variable=var256).pack(anchor="w")

# Fortschrittsanzeige
progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Statusanzeige
label_status = ttk.Label(window, text="")
label_status.pack()

# Konvertierungs-Button
ttk.Button(window, text="Konvertieren", command=convert_images).pack(pady=10)

window.mainloop()
