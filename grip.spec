Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(pl):	rip, odtwarzacz kompaktów umo¿liwiaj±cy ¶ci±ganie ¶cie¿ek CD i/lub kompresowanie ich w formacie MP3.
Name:		grip
Version:	2.5
Release:	1
Copyright:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.ling.ed.ac.uk/~oliphant/grip/%{name}-%{version}.tgz
Source1:	http://www.mit.edu/afs/sipb/user/xiphmont/cdparanoia/download/cdparanoia-III-alpha9.5.src.tgz
Patch0:		grip-install.patch
Patch1:		grip-opt.patch
Patch2:		cdparanoia-III.patch
URL:		http://www.ling.ed.ac.uk/~oliphant/grip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	bladeenc, cdparanoia, mp3info

%define		_prefix	/usr/X11R6
%define		_mandir /usr/X11R6/man

%description
Grip is a gtk-based cd-player and front-end for cd-rippers and MP3
encoders. It allows you to rip entire tracks, or pinpoint a section of a
track to rip. The CDDB protocol is supported for retreiving/submitting track
information from/to disc database servers.

%description -l pl
Grip jest odtwarzaczem kompaktów. Mo¿e byæ u¿ywany jako front-end do programów
¶ci±gaj±cych ¶cie¿ki CD oraz kompresuj±cych pliki d¼wiêkowe do formatu MP3.
Umo¿liwia ¶ci±ganie tak ca³ych jak i wybranych czê¶ci utworu. Program ten
wspiera protokó³ CDDB w celu ¶ci±gania/wysy³ania danych o kompakcie 
z/do umo¿liwiaj±cego tego typu operacje serwera.

%prep
%setup -q
%setup -q -a 1
%patch0 -p1
%patch1 -p1
cd cdparanoia-III-alpha9.5
%patch2 -p1

%build
mv cdparanoia-III-alpha9.5 cdparanoia
cd cdparanoia
RPM_OPT=$RPM_OPT_FLAGS
export RPM_OPT
%configure
make
cd ..
make AUXDIR=/etc INSTALLDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

make PREFIX=$RPM_BUILD_ROOT%{_prefix} AUXDIR=$RPM_BUILD_ROOT/etc install
install gripicon.tif $RPM_BUILD_ROOT%{_datadir}/pixmaps/gripicon.tiff

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf README CREDITS LICENSE TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CREDITS,LICENSE,TODO}.gz
%attr(755,root,root) %{_bindir}/grip
%{_datadir}/pixmaps/gripicon.tiff
%config /etc/grip.rc
