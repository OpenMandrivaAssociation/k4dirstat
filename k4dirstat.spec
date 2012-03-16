%define snapshot 20101010

Name:		k4dirstat
Summary:	Ggraphical disk usage utility
Version:	0.1
Release:	%{?snapshot:0.%{snapshot}.}1
License:	GPLv2
Group:		File tools
URL:		http://grumpypenguin.org/
Source0:	kdirstat-%{snapshot}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel

%description
KDirStat is a graphical disk usage utility, very much like the Unix "du"
command. In addition to that, it comes with some cleanup facilities to reclaim
disk space. 

%prep
%setup -q -n kdirstat-%{snapshot}

%build
%cmake
%make

%install
pushd build
%makeinstall_std
popd

%files
%{_bindir}/k4dirstat
%{_kde_applicationsdir}/k4dirstat.desktop
%{_kde_appsdir}/k4dirstat/
%{_kde_datadir}/config.kcfg/k4dirstat.kcfg
%{_kde_docdir}/HTML/en/k4dirstat/
%{_kde_iconsdir}/hicolor/*/apps/k4dirstat.*
