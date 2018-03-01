Name:		k4dirstat
Summary:	Ggraphical disk usage utility
Version:	3.1.3
Release:	1
License:	GPLv2
Group:		File tools
URL:		https://bitbucket.org/jeromerobert/k4dirstat/wiki/Home
Source0:	https://bitbucket.org/jeromerobert/k4dirstat/get/k4dirstat-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Gui) cmake(Qt5Core) cmake(Qt5Widgets)
BuildRequires:	cmake(KF5CoreAddons) cmake(KF5I18n) cmake(KF5DocTools) cmake(KF5XmlGui) cmake(KF5KIO) cmake(KF5JobWidgets) cmake(KF5IconThemes)

%description
KDirStat is a graphical disk usage utility, very much like the Unix "du"
command. In addition to that, it comes with some cleanup facilities to reclaim
disk space. 

%prep
%setup -qn jeromerobert-k4dirstat-fcf698417d42

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
