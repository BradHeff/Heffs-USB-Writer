import ttkbootstrap as ttk
from tkinter import filedialog
import os


# constants for window size and positioning
WIDTH, HEIGHT = 700, 350
X, Y = 0, 0
VERSION = "1.0.9"


class USBWriterGUI:
    def __init__(self, master):
        self.master = master
        self.style = ttk.Style(theme="darkly")

        self.create_widgets()
        self.setup_widgets()
        self.setup_bindings()
        self.setup_menu()
        self.setup_statusbar()

    def calculate_position(self, width, height):
        x = int((self.master.winfo_screenwidth() - width) / 2)
        y = int((self.master.winfo_screenheight() - height) / 2)
        return f"{width}x{height}+{x}+{y}"

    def window(self):
        self.master.title("Heff's USB Writer")
        self.master.geometry(self.calculate_position(WIDTH, HEIGHT))
        self.master.resizable(False, False)

    def icon(self):
        icon_path = "/usr/share/pixmaps/horizon.png"
        if os.path.exists(icon_path):
            self.master.iconphoto(False, ttk.PhotoImage(file=icon_path))

    def create_widgets(self):
        self.frame = ttk.Frame(self.master, padding="20")
        self.frame.pack(fill=ttk.BOTH, expand=ttk.YES)

        self.lbl_title = ttk.Label(
            self.frame,
            text="Write ISO to USB to create a bootable USB for any Linux distribution",
            font=("TkDefaultFont", 10),
            anchor=ttk.CENTER,
            justify=ttk.CENTER,
            wraplength=400,
        )

        self.iso_label = ttk.Label(
            self.frame, text="ISO File:", font=("TkDefaultFont", 12)
        )
        self.iso_entry = ttk.Entry(self.frame, width=30, font=("TkDefaultFont", 12))
        self.iso_button = ttk.Button(
            self.frame, text="Browse", command=self.browse_iso, style="info.TButton"
        )

        self.usb_label = ttk.Label(
            self.frame, text="USB Drive: ", font=("TkDefaultFont", 12)
        )
        self.usb_combobox = ttk.Combobox(
            self.frame, width=30, font=("TkDefaultFont", 12)
        )
        self.refresh_button = ttk.Button(
            self.frame, text="Refresh", style="info.Outline.TButton"
        )

        self.write_button = ttk.Button(
            self.frame, text="Write to USB", style="success.TButton"
        )

        self.progress = ttk.Progressbar(
            self.master,
            length=600,
            mode="determinate",
            style="success.Horizontal.TProgressbar",
        )

    def setup_widgets(self):
        self.lbl_title.grid(row=0, column=0, columnspan=3, pady=3)

        self.iso_label.grid(row=1, column=0, sticky=ttk.W, pady=10, padx=10)
        self.iso_entry.grid(row=1, column=1, pady=10, padx=(0, 10))
        self.iso_button.grid(row=1, column=2, pady=10)

        self.usb_label.grid(row=2, column=0, sticky=ttk.W, pady=10, padx=10)
        self.usb_combobox.grid(row=2, column=1, pady=10, padx=(0, 10))
        self.refresh_button.grid(row=2, column=2, pady=10)

        self.write_button.grid(row=3, column=2, pady=20)

        self.progress.pack(side=ttk.BOTTOM, fill=ttk.X)

    def setup_bindings(self):
        self.master.bind("<Escape>", lambda e: self.master.quit())

    def setup_menu(self):
        menubar = ttk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = ttk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.quit)

        help_menu = ttk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def setup_statusbar(self):
        self.statusbar = ttk.Label(
            self.master,
            text="Ready",
            relief=ttk.SUNKEN,
            anchor=ttk.W,
            font=("TkDefaultFont", 10),
        )
        self.statusbar.pack(side=ttk.BOTTOM, fill=ttk.X)

    def browse_iso(self):
        filename = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
        if filename:
            self.iso_entry.delete(0, ttk.END)
            self.iso_entry.insert(0, filename)

    def show_about(self):
        about_window = ttk.Toplevel(self.master)
        about_window.resizable(False, False)
        about_window.title("About Heff's USB Writer")
        about_label = ttk.Label(
            about_window,
            text="Heff's USB Writer\nVersion 1.0\n\nCreated by Brad Heffernan",
            font=("TkDefaultFont", 12),
            justify=ttk.CENTER,
        )
        about_label.pack(padx=20, pady=20)

    def update_progress(self, value):
        self.progress["value"] = value
        self.master.update_idletasks()

    def update_status(self, text):
        self.statusbar.config(text=text)
