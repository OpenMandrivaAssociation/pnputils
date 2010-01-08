%define name pnputils
%define version 0.1

Summary: Dump resource information for PnP devices
Name: %{name}
Version: %{version}
Release: %mkrel 6
Source0: %{name}-%{version}.tar.bz2
Patch0: pnputils-0.1-destdir.patch
License: GPL
Group: System/Kernel and hardware
Url: ftp://ftp.kernel.org/pub/linux/kernel/people/helgaas/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ldetect-lst >= 0.1.282


%description
A utility for dumping resource information for PnP devices.

%prep
%setup -q
%patch0 -p1 -b .destdir

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#packaged as part of ldetect-lst
rm -f $RPM_BUILD_ROOT%{_datadir}/misc/pnp.ids

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
/sbin/lspnp
/sbin/setpnp
%{_mandir}/man8/*.8*
