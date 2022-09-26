Name:		k4dirstat
Summary:	Ggraphical disk usage utility
Version:	3.4.2
Release:	1
License:	GPLv2
Group:		File tools
URL:		https://bitbucket.org/jeromerobert/k4dirstat/wiki/Home
Source0:	https://github.com/jeromerobert/k4dirstat/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Gui) 
BuildRequires:	cmake(Qt5Core) 
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5CoreAddons) 
BuildRequires:	cmake(KF5I18n) 
BuildRequires:	cmake(KF5DocTools) 
BuildRequires:	cmake(KF5XmlGui) 
BuildRequires:	cmake(KF5KIO) 
BuildRequires:	cmake(KF5JobWidgets) 
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	pkgconfig(zlib)

%description
KDirStat is a graphical disk usage utility, very much like the Unix "du"
command. In addition to that, it comes with some cleanup facilities to reclaim
disk space. 

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/k4dirstat
%{_kde5_applicationsdir}/k4dirstat.desktop
%{_kde5_datadir}/config.kcfg/k4dirstat.kcfg
%{_kde5_docdir}/HTML/en/k4dirstat/
%{_kde5_iconsdir}/hicolor/*/apps/k4dirstat.*
%{_mandir}/man1/%{name}.1*
