Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(pl):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Summary(zh_CN):	GripÊÇÒ»¸ö CD ²¥·ÅÆ÷, ×¥¹ìÆ÷ºÍ MP3 ±àÂëÆ÷Ç°¶Ë³ÌĞò.
Name:		grip
Version:	3.0.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.nostatic.org/grip/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://www.nostatic.org/grip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libghttp-devel
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

%description -l zh_CN
Grip ÊÇÒ»¸ö¿ÉÒÔÔÚGnome×ÀÃæ»·¾³ÏÂÔËĞĞµÄCDÒôÀÖ²¥·ÅÆ÷ºÍ×¥¹ìÆ÷, Ëü¿ÉÒÔÊ¹ÓÃ
ÄÚÖÃµÄ cdparanoia ³ÌĞò×¥¹ìÆ÷(½«Òô¹ì´æ´¢ÎªÎÄ¼ş),Ò²¿ÉÒÔÊ¹ÓÃÍâ²¿µÄ×¥¹ìÆ÷
(ÀıÈç: cdda2wav).Í¬Ê±Ìá¹©×Ô¶¯µÄMP3±àÂëÇ°¶Ë,
»¹¿ÉÒÔ×Ô¶¯µØ´ÓinternetÉÏµÄ¹â ÅÌÊı¾İ¿âÖĞ²éÑ¯¹âÅÌÇúÄ¿.
Èç¹ûĞ­Í¬DigitalDJ³ÌĞòÒ»Æğ¹¤×÷, Äú¿ÉÒÔ´´½¨×Ô¼ºµÄ "¼ÆËã»ú»¯"µÄÒôÀÖ¿â.

%prep
%setup -q

%build
rm -f missing
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--disable-id3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Multimedia}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CREDITS TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
