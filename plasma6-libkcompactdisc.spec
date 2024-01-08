%define kf6compactdisc_major 6
%define libkf6compactdisc %mklibname kf6compactdisc %{kf6compactdisc_major}

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-libkcompactdisc
Version:	24.01.85
Release:	1
Epoch:		3
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
Requires:	%{libkf6compactdisc} = %{EVRD}

%description
KDE library for playing & ripping CDs.

%files -f libkcompactdisc.lang

#------------------------------------------------------------------------------
%package -n %{libkf6compactdisc}
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libkf6compactdisc}
KDE library for playing & ripping CDs.

%files -n %{libkf6compactdisc}
%{_libdir}/libKF6CompactDisc.so.%{kf6compactdisc_major}
%{_libdir}/libKF6CompactDisc.so.%{kf6compactdisc_major}.*

#------------------------------------------------------------------------------
%define devname %mklibname kf6compactdisc -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkf6compactdisc} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.96

%description -n %{devname}
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%files -n %{devname}
%{_libdir}/libKF6CompactDisc.so
%{_libdir}/cmake/KF6CompactDisc
%{_includedir}/*
%{_libdir}/qt6/mkspecs/modules/qt_KCompactDisc.pri

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%autopatch -p1

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang libkcompactdisc
