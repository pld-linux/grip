Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(pl):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Name:		grip
Version:	2.96
Release:	1
Epoch		1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.nostatic.org/grip/%{name}-%{version}.tgz
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch0:		%{name}-install.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-libs.patch
URL:		http://www.nostatic.org/grip/
BuildRequires:	gtk+-devel
BuildRequires:	cdparanoia-III-devel
Requires:	bladeenc
Requires:	mp3info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Grip is a gtk-based cd-player and front-end for cd-rippers and MP3
encoders. It allows you to rip entire tracks, or pinpoint a section of
a track to rip. The CDDB protocol is supported for
retreiving/submitting track information from/to disc database servers.

%description -l pl
Grip jest odtwarzaczem kompaktów. Mo¿e byæ u¿ywany jako front-end do
programów ¶ci±gaj±cych ¶cie¿ki CD oraz kompresuj±cych pliki d¼wiêkowe
do formatu MP3. Umo¿liwia ¶ci±ganie tak ca³ych jak i wybranych czê¶ci
utworu. Program ten wspiera protokó³ CDDB w celu ¶ci±gania/wysy³ania
danych o kompakcie z/do umo¿liwiaj±cego tego typu operacje serwera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}" \
	AUXDIR=%{_sysconfdir} INSTALLDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Multimedia}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	AUXDIR=$RPM_BUILD_ROOT%{_sysconfdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf README CREDITS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
