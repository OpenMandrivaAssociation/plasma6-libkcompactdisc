%define kcompactdisc6_major 5
%define libkcompactdisc6 %mklibname KCompactDisc6 %{kcompactdisc6_major}

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-libkcompactdisc
Version:	24.01.85
Release:	1
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libkcompactdisc-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Phonon4Qt6)
Requires:	%{libkcompactdisc6} = %{EVRD}

%description
KDE library for playing & ripping CDs.

%files -f libkcompactdisc.lang

#------------------------------------------------------------------------------
%package -n %{libkcompactdisc6}
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libkcompactdisc6}
KDE library for playing & ripping CDs.

%files -n %{libkcompactdisc6}
%{_libdir}/libKCompactDisc6.so.%{kcompactdisc6_major}
%{_libdir}/libKCompactDisc6.so.%{kcompactdisc6_major}.*

#------------------------------------------------------------------------------
%define devname %mklibname KCompactDisc6 -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcompactdisc6} = %{EVRD}

%description -n %{devname}
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%files -n %{devname}
%{_libdir}/libKCompactDisc6.so
%{_libdir}/cmake/KCompactDisc6
%{_includedir}/*
%{_libdir}/qt6/mkspecs/modules/qt_KCompactDisc.pri

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n libkcompactdisc-%{version}

%build
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang libkcompactdisc
