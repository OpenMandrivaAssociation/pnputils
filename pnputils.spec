%define name pnputils
%define version 0.1

Summary: Dump resource information for PnP devices
Name: %{name}
Version: %{version}
Release: %mkrel 8
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 667795
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2011.0
+ Revision: 607187
- rebuild

* Fri Jan 08 2010 Frederic Crozat <fcrozat@mandriva.com> 0.1-6mdv2010.1
+ Revision: 487689
- uncompress patch
- remove pnp.ids, moved to ldetect-lst

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-5mdv2010.0
+ Revision: 426735
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 225020
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2008.1
+ Revision: 179248
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdv2008.1
+ Revision: 179240
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2008.0
+ Revision: 74791
- Import pnputils



* Mon Jul 10 2006 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.0
- initial Mandriva release
