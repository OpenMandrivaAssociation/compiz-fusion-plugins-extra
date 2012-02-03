%define name compiz-fusion-plugins-extra
%define newname compiz-plugins-extra
%define version 0.8.6
%define rel 3

Summary: Compiz Fusion Main Plugin Set for compiz
Name: %{name}
Version: %{version}
Release: %mkrel %rel
Source0: http://releases.compiz-fusion.org/%{version}/%{newname}-%{version}.tar.bz2
Patch0:  compiz-plugins-extra-0.8.6-libnotify0.7.patch
Patch1:  0001-Treat-screenlets-windows-as-widgets.patch
Patch2:  cubereflex-blue.patch
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: dbus-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: compiz-fusion-plugins-main-devel >= %{version}
BuildRequires: compiz-bcop
BuildRequires: libGConf2-devel
BuildRequires: MesaGLU-devel
BuildRequires: jpeg-devel
BuildRequires: pango-devel
BuildRequires: libnotify-devel
Requires: compiz

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities

#----------------------------------------------------------------------------

%package devel
Summary: Development files for Compiz Fusion Extra Plugin Set for compiz
Group: Development/X11

%description devel
Development files for Compiz Fusion Extra Plugin Set for compiz

#----------------------------------------------------------------------------

%prep
%setup -qn %{newname}-%{version}
%patch0 -p0
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;
%find_lang %{newname}

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -f %{newname}.lang
%defattr(-,root,root)
%{_libdir}/compiz/lib*.a
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png


%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Apr 12 2011 Funda Wang <fwang@mandriva.org> 0.8.6-3mdv2011.0
+ Revision: 652761
- build with libnotify 0.7
- rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-2mdv2011.0
+ Revision: 603846
- rebuild

* Sun May 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.8.6-1mdv2010.1
+ Revision: 541655
- New version: 0.8.6

* Sat Mar 13 2010 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-2mdv2010.1
+ Revision: 518616
- Rebuild for new Compiz

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.4-1mdv2010.0
+ Revision: 457734
- New version: 0.8.4
- Harden buildrequires versions

* Wed Sep 09 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.2-3mdv2010.0
+ Revision: 434889
- Rebuild against updated compiz

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 413263
- rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 355372
- New version 0.8.2
- keep the old name for the moment, needs a package renaming

* Sun Feb 08 2009 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-0.20090208.1mdv2009.1
+ Revision: 338488
- 0.8 pre-release snapshot

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.8-1mdv2009.1
+ Revision: 319175
- rediff and rename widget-screenlets-match.patch
- 0.7.8 final

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.8-0.20080912.1mdv2009.0
+ Revision: 284302
- New snapshot
- Add -devel subpackage for new upstream files

* Sun Jul 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.7-0.20080713.1mdv2009.0
+ Revision: 234354
- New snapshot
- New version: 0.7.6

* Fri May 23 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.5-0.20080522.1mdv2009.0
+ Revision: 210162
- Update to git snapshot
- Disable the cubereflex patch (need to investigate what happened to it :)

* Tue Apr 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.4-1mdv2009.0
+ Revision: 192373
- New version 0.7.4

* Fri Mar 07 2008 Colin Guthrie <cguthrie@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 181124
- New version 0.7.2

* Wed Mar 05 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080218.2mdv2008.1
+ Revision: 179390
- Add BR on libnotify-devel for the notification plugin

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.99-0.20080218.1mdv2008.1
+ Revision: 172301
- Update to git master for new compiz

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 100720
- New upstream release: 0.6.0

* Fri Oct 19 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20071018.1mdv2008.1
+ Revision: 100100
- Update snapshot from 0.6.0 branch for compiz 0.6.2

* Mon Sep 17 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-4mdv2008.0
+ Revision: 88950
- Make reflections colours fit in better with default Mandriva theme.

* Sun Sep 16 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-3mdv2008.0
+ Revision: 88521
- Add window match for widget plugin for Screenlets

* Tue Sep 04 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-2mdv2008.0
+ Revision: 79533
- Rebuild for latest compiz (patch removal caused ABI change)

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62615
- Official Release: 0.5.3

* Sun Aug 12 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070811.1mdv2008.0
+ Revision: 62122
- Update snapshot

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070801.1mdv2008.0
+ Revision: 57839
- Updated snapshot

* Wed Jul 25 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070724.1mdv2008.0
+ Revision: 55253
- Update Snapshot

* Sat Jul 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070714.2mdv2008.0
+ Revision: 52142
- Update snapshot

* Sun Jul 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.20070707.1mdv2008.0
+ Revision: 49610
- Require compiz
- Update Snapshot to 20070707
- Import compiz-fusion-extra

