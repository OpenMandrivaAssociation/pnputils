%define debug_package %{nil}

Summary:	Dump resource information for PnP devices
Name:		pnputils
Version:	0.1
Release:	19
License:	GPLv2
Group:		System/Kernel and hardware
Url:		ftp://ftp.kernel.org/pub/linux/kernel/people/helgaas/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		pnputils-0.1-destdir.patch
Requires:	ldetect-lst >= 0.1.282

%description
A utility for dumping resource information for PnP devices.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
%make

%install
%makeinstall_std

#packaged as part of ldetect-lst
rm -f %{buildroot}%{_datadir}/misc/pnp.ids

%files
%doc ChangeLog
/sbin/lspnp
/sbin/setpnp
%{_mandir}/man8/*.8*

