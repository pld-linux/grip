Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(pl):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Summary(zh_CN):	Grip是一个 CD 播放器, 抓轨器和 MP3 编码器前端程序.
Name:		grip
Version:	3.0.0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.nostatic.org/grip/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://www.nostatic.org/grip/
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	cdparanoia-III-devel
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
Grip jest odtwarzaczem kompakt體. Mo縠 by� u縴wany jako front-end do
program體 禼i眊aj眂ych 禼ie縦i CD oraz kompresuj眂ych pliki d紈i阫owe
do formatu MP3. Umo縧iwia 禼i眊anie tak ca硑ch jak i wybranych cz甓ci
utworu. Program ten wspiera protok蟪 CDDB w celu 禼i眊ania/wysy砤nia
danych o kompakcie z/do umo縧iwiaj眂ego tego typu operacje serwera.

%description -l zh_CN
Grip 是一个可以在Gnome桌面环境下运行的CD音乐播放器和抓轨器, 它可以使用
内置的 cdparanoia 程序抓轨器(将音轨存储为文件),也可以使用外部的抓轨器
(例如: cdda2wav).同时提供自动的MP3编码前端,
还可以自动地从internet上的光 盘数据库中查询光盘曲目.
如果协同DigitalDJ程序一起工作, 您可以创建自己的 "计算机化"的音乐库.

%prep
%setup -q

%build
%configure2_13 \
	--disable-id3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Multimedia}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
