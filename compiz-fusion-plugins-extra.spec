%define _disable_ld_no_undefined 1

%define __noautoprov 'pkgconfig(.*)'
%define __noautoreq 'pkgconfig\\(compiz\\)'

%define oname compiz-plugins-extra

Summary:	Compiz Fusion Main Plugin Set for compiz
Name:		compiz-fusion-plugins-extra
Version:	0.8.8
Release:	1
License:	GPLv2
Group:		System/X11
URL:		http://www.compiz.org/
Source0:	http://releases.compiz.org/components/plugins-extra/%{oname}-%{version}.tar.bz2
Patch0:		compiz-plugins-extra-0.8.8-libnotify0.7.patch
BuildRequires:	intltool
BuildRequires:	compiz0.8-bcop
BuildRequires:	compiz0.8-devel
BuildRequires:	compiz-fusion-plugins-main-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(pango)
Requires:	compiz0.8

%description
This is the main plugin set from the Compiz Fusion community.

This is a combination of the Compiz Extras and Beryl communities.

%files -f %{oname}.lang
%{_libdir}/compiz/lib*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Compiz Fusion Extra Plugin Set for compiz
Group:		Development/X11
Conflicts:	compiz-devel > 0.9
Requires:	compiz0.8-devel

%description devel
Development files for Compiz Fusion Extra Plugin Set for compiz.

%files devel
%{_includedir}/compiz/*.h
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{oname}

