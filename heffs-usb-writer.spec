Name:           heffs-usb-writer
Version:        1.0.8
Release:        1%{?dist}
Summary:        Create bootable USB for Linux Distributions
License: GPLv3+
URL: https://github.com/BradHeff/Horizon-Bulkuser-Importer-Canvas
Source0: %{name}-%{version}.tar.gz

BuildRequires: python3
Requires:      python3, python3-tkinter, python3-pillow, python3-pillow-tk, ttkbootstrap


%description
Create bootable USB for Linux Distributions

%install
mkdir -p %{buildroot}/usr/local/bin/
mkdir -p %{buildroot}/usr/lib/Heffs_USB_Writer/
mkdir -p %{buildroot}/usr/share/pixmaps/
mkdir -p %{buildroot}/usr/share/polkit-1/actions/
mkdir -p %{buildroot}/usr/share/applications/



cp %{_topdir}/BUILD/heffs-usb-writer/heffs-usb-writer %{buildroot}/usr/local/bin/heffs-usb-writer
cp %{_topdir}/BUILD/heffs-usb-writer/heffs-usb-writer.desktop %{buildroot}/usr/share/applications/heffs-usb-writer.desktop
cp %{_topdir}/BUILD/heffs-usb-writer/heffna.png %{buildroot}/usr/share/pixmaps/heffna.png
cp %{_topdir}/BUILD/heffs-usb-writer/org.heffsusb.writer.policy %{buildroot}/usr/share/polkit-1/actions/org.heffsusb.writer.policy
cp %{_topdir}/BUILD/heffs-usb-writer/USBWriter.py %{buildroot}/usr/lib/Heffs_USB_Writer/USBWriter.py
cp %{_topdir}/BUILD/heffs-usb-writer/Gui.py %{buildroot}/usr/lib/Heffs_USB_Writer/Gui.py



%post
chmod +x /usr/local/bin/heffs-usb-writer

%files

/usr/local/bin/heffs-usb-writer
/usr/share/applications/heffs-usb-writer.desktop
/usr/share/polkit-1/actions/org.heffsusb.writer.policy
/usr/lib/Heffs_USB_Writer/Gui.py
/usr/lib/Heffs_USB_Writer/USBWriter.py
/usr/share/pixmaps/heffna.png


%changelog
* Mon Nov 25 2024 Brad Heffernan <brad.heffernan83@outlook.com>
- 
