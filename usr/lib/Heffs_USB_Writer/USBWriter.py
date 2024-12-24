import ttkbootstrap as ttk
from Gui import USBWriterGUI
import subprocess
import re
import os
import psutil


class USBWriter:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.gui = USBWriterGUI(self.root)
        self.setup_callbacks()

    def setup_callbacks(self):
        self.gui.refresh_button.config(command=self.refresh_usb_list)
        self.gui.write_button.config(command=self.write_to_usb)

    def refresh_usb_list(self):
        self.gui.update_status("Refreshing USB devices...")
        self.gui.update_progress(0)

        usb_devices = []
        for partition in psutil.disk_partitions(all=True):
            if "removable" in partition.opts or "usb" in partition.opts.lower():
                device_name = f"{partition.device} ({partition.mountpoint})"
                usb_devices.append(device_name)

        if not usb_devices:
            self.gui.update_status("No USB devices found")
        else:
            self.gui.update_status(f"Found {len(usb_devices)} USB device(s)")

        self.gui.usb_combobox["values"] = usb_devices
        self.gui.update_progress(100)

    def write_to_usb(self):
        iso_file = self.gui.iso_entry.get()
        usb_drive = self.gui.usb_combobox.get()

        if not iso_file or not usb_drive:
            self.gui.update_status("Please select both ISO file and USB drive")
            return

        # Extract the device name from the combobox value
        device = usb_drive.split()[0]

        # Check if the user has necessary permissions
        if os.geteuid() != 0:
            self.gui.update_status(
                "Error: Root privileges required. Please run as sudo."
            )
            return

        self.gui.update_status(f"Writing {iso_file} to {device}...")

        # Get the total size of the ISO file
        total_size = os.path.getsize(iso_file)

        try:
            # Use dd command to write ISO to USB
            cmd = f"dd if={iso_file} of={device} bs=4M status=progress"
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

            # Read the output of dd command
            for line in process.stdout:
                if "bytes" in line:
                    # Extract the number of bytes written
                    match = re.search(r"(\d+)\s+bytes", line)
                    if match:
                        bytes_written = int(match.group(1))
                        progress = int((bytes_written / total_size) * 100)
                        self.gui.update_progress(progress)
                        self.gui.update_status(f"Writing... {progress}% complete")

            # Wait for the process to complete
            process.wait()

            if process.returncode == 0:
                self.gui.update_status("Write complete!")
                self.gui.update_progress(100)
            else:
                self.gui.update_status("Error occurred during writing.")

        except Exception as e:
            self.gui.update_status(f"Error: {str(e)}")

    def run(self):
        self.gui.window()
        self.gui.icon()
        self.root.mainloop()


if __name__ == "__main__":
    app = USBWriter()
    app.run()
