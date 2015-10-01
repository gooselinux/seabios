%define githead 669c991

# there are no binaries for -debuginfo in this package
%define debug_package %{nil}

Name:           seabios
Version:        0.5.1
%define pkgrelease 3
Release:        %{pkgrelease}%{?dist}
Summary:        Open-source legacy BIOS implementation

Group:          Applications/Emulators
License:        LGPLv3
URL:            http://www.coreboot.org/SeaBIOS
# Source0:        http://linuxtogo.org/~kevin/SeaBIOS/%{name}-%{version}.tar.gz
# The source for this package was pulled from upstream's git.  Use the
# following commands to generate the tarball:
# git archive --format=tar --prefix=seabios-0.5.1/ 669c991 | gzip > seabios-0.5.1-669c991.tar.gz
Source0:        %{name}-%{version}-%{githead}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python
BuildRequires: iasl
ExclusiveArch: x86_64

Patch0: seabios-Go-back-to-using-0xf0000000.patch
# For bz#571553 - Backport 0.5.1-stable seabios.git fixes
Patch1: seabios-Fix-PkgLength-calculation-for-the-SSDT.patch
# For bz#567910 - Make seabios configuration parameter CONFIG_S3_RESUME_VGA_INIT default to 1
Patch2: seabios-Set-CONFIG_S3_RESUME_VGA_INIT-to-1.patch
# For bz#561290 - `dmidecode' shows wrong memory which is assigned to VM.
Patch3: seabios-smbios-avoid-counting-io-hole-as-ram.patch
# For bz#578752 - Need to show "hard disk" menu item when pressing F12 during POST
Patch4: seabios-Support-for-booting-from-virtio-disks.patch
# For bz#578752 - Need to show "hard disk" menu item when pressing F12 during POST
# For bz#596881 - Unable to install RHEL virtual machines
Patch5: seabios-Revert-Support-for-booting-from-virtio-disks.patch
# For bz#578752 - Need to show "hard disk" menu item when pressing F12 during POST
Patch6: seabios-Support-for-booting-from-virtio-disks-reapply.patch
# For bz#578752 - Need to show "hard disk" menu item when pressing F12 during POST
# For bz#596881 - Unable to install RHEL virtual machines
Patch7: seabios-zero-memory-before-use.patch
# For bz#602177 - Failed to install rhel3.9-64 guest
Patch8: seabios-do-not-advertise-hpet-to-a-guest-OS.patch
# For bz#593317 - seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0
Patch9: seabios-smbios-allow-vendor-manufacturer-version-product-nam.patch
# For bz#593317 - seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0
Patch10: seabios-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch
# For bz#593317 - seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0
Patch11: seabios-smbios-set-system-manufacturer-product-name-to-Red-H.patch
# For bz#593317 - seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0
Patch12: seabios-smbios-set-Type-3-chassis-manufacturer-information-t.patch
# For bz#603677 - Windows7 hangs during resume from S3 when using QXL device
Patch13: seabios-fix-resume-from-S3-with-QXL-device.patch
# For bz#603677 - Windows7 hangs during resume from S3 when using QXL device
Patch14: seabios-remove-acpi-dsdt.hex-file-from-source-tree.patch
# For bz#606411 - Update version info to match upstream 0.5.1
Patch15: seabios-Update-version-to-0.5.1.patch
# For bz#561324 - USB keyboard misbehaves with BIOS driver
Patch16: seabios-Support-USB-keyboard-auto-repeat.patch
# For bz#561324 - USB keyboard misbehaves with BIOS driver
Patch17: seabios-Support-USB-interrupt-schedules-on-OHCI-and-UHCI.patch
# For bz#607500 - An unexpected error occurs during winxp installation with virtio disk.
Patch18: seabios-add-write-support-to-virtio-blk.patch

%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1


%build
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seabios
install -m 0644 out/bios.bin $RPM_BUILD_ROOT%{_datadir}/seabios


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/seabios/
%doc COPYING COPYING.LESSER README TODO
%{_datadir}/seabios/bios.bin



%changelog
* Wed Aug 18 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-3.el6
- seabios-add-write-support-to-virtio-blk.patch [bz#607500]
- Resolves: bz#607500
  (An unexpected error occurs during winxp installation with virtio disk.)

* Tue Jun 29 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-2.el6
- seabios-Support-USB-keyboard-auto-repeat.patch [bz#561324]
- seabios-Support-USB-interrupt-schedules-on-OHCI-and-UHCI.patch [bz#561324]
- Resolves: bz#561324
  (USB keyboard misbehaves with BIOS driver)

* Mon Jun 28 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-1.el6
- seabios-Update-version-to-0.5.1.patch [bz#606411]
- Resolves: bz#606411
  (Update version info to match upstream 0.5.1)

* Wed Jun 23 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.15.20100108git669c991.el6
- seabios-remove-acpi-dsdt.hex-file-from-source-tree.patch [bz#603677]
- Add BuildRequires: iasl
- Resolves: bz#603677
  (Windows7 hangs during resume from S3 when using QXL device)

* Mon Jun 21 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.14.20100108git669c991.el6
- seabios-fix-resume-from-S3-with-QXL-device.patch [bz#603677]
- Resolves: bz#603677
  (Windows7 hangs during resume from S3 when using QXL device)

* Mon Jun 21 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.13.20100108git669c991.el6
- seabios-smbios-allow-vendor-manufacturer-version-product-nam.patch [bz#593317]
- seabios-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch [bz#593317]
- seabios-smbios-set-system-manufacturer-product-name-to-Red-H.patch [bz#593317]
- seabios-smbios-set-Type-3-chassis-manufacturer-information-t.patch [bz#593317]
- Resolves: bz#593317
  (seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0)

* Wed Jun 16 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.12.20100108git669c991.el6
- seabios-do-not-advertise-hpet-to-a-guest-OS.patch [bz#602177]
- Resolves: bz#602177
  (Failed to install rhel3.9-64 guest)

* Wed Jun 09 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.11.20100108git669c991.el6
- seabios-Support-for-booting-from-virtio-disks-reapply.patch [bz#578752]
- seabios-zero-memory-before-use.patch [bz#578752 bz#596881]
- Resolves: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)
- Related: bz#596881
  (Unable to install RHEL virtual machines)

* Wed Jun 02 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.10.20100108git669c991.el6
- seabios-Revert-Support-for-booting-from-virtio-disks.patch [bz#578752 bz#596881]
- Resolves: bz#596881
  (Unable to install RHEL virtual machines)
- Related: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)

* Wed May 19 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.9.20100108git669c991.el6
- seabios-Support-for-booting-from-virtio-disks.patch [bz#578752]
- Resolves: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)

* Mon May 17 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.8.20100108git669c991.el6
- seabios-smbios-avoid-counting-io-hole-as-ram.patch [bz#561290]
- Resolves: bz#561290
  (`dmidecode' shows wrong memory which is assigned to VM.)

* Thu Apr 29 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.7.20100108git669c991.el6
- Disable -debuginfo package generation
- Related: bz#564482
  (empty debuginfo packages)

* Thu Apr 22 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.6.20100108git669c991.el6
- seabios-Set-CONFIG_S3_RESUME_VGA_INIT-to-1.patch [bz#567910]
- Resolves: bz#567910
  (Make seabios configuration parameter CONFIG_S3_RESUME_VGA_INIT default to 1)

* Tue Mar 16 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.5.20100108git669c991.el6
- seabios-Fix-PkgLength-calculation-for-the-SSDT.patch [bz#571553]
- Resolves: bz#571553
  (Backport 0.5.1-stable seabios.git fixes)

* Tue Mar 9 2010 Glauber Costa <glommer@redhat.com> - seabios-0.5.1-0.4.20100108git669c991.el6
- Go back to using 0xf0000000 for PCI memory start
- Resolves: bz#571553
  (Backport 0.5.1-stable seabios.git fixes)

* Wed Jan 13 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.3.20100108git669c991.el6
- Build only on x86_64
- Resolves: bz#554866
  (seabios should not be shipped on i686/ppc64/s390x, only x86_64)

* Tue Jan 12 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.2.20100108git669c991.el6
- Regenerate tarball from git (it contained an extra .pyc file that doesn't belong there)

* Thu Jan 07 2010 Justin M. Forbes <jforbes@redhat.com> 0.5.1-0.1.20100108git669c991
- Created initial package
