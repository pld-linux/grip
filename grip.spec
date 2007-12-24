Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(ca.UTF-8):	Reproductor/extractor de CD d'audio
Summary(es.UTF-8):	Grip, interfaz para reproducir CDs y generar MP3s
Summary(fr.UTF-8):	Grip, un lecteur de CD, extracteur, et IHM pour encodeur MP3
Summary(ja.UTF-8):	CD プレーヤー/リッパ/MP3エンコーダ フロントエンド
Summary(pl.UTF-8):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Summary(pt_BR.UTF-8):	Grip, interface para reproduzir CDs e gerar MP3s
Summary(zh_CN.UTF-8):	Grip 是一个 CD 播放器、抓轨器和 MP3 编码器前端程序。
Summary(zh_HK.UTF-8):	Grip 是一個 CD 播放器、抓軌器和 MP3 編碼器前端程式。
Summary(zh_TW.UTF-8):	Grip 是一個 CD 播放器、抓軌器和 MP3 編碼器前端程式。
Name:		grip
Version:	3.3.1
Release:	4
Epoch:		1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/grip/%{name}-%{version}.tar.gz
# Source0-md5:	4b4233999b9f2bc85c711092553ea9aa
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-configure_in.patch
Patch2:		%{name}-po.patch
URL:		http://www.nostatic.org/grip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	curl-devel
BuildRequires:	id3lib-devel >= 3.7.13
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
Suggests:	bladeenc
Suggests:	cdparanoia-III
Suggests:	flac
Suggests:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grip is a GTK+-based cd-player and front-end for cd-rippers and MP3
encoders. It allows you to rip entire tracks, or pinpoint a section of
a track to rip. The CDDB protocol is supported for
retreiving/submitting track information from/to disc database servers.

%description -l fr.UTF-8
Grip est un lecteur-extracteur de CD pour le Bureau GNome. Il a des
capacités d'extraction du type cdparanoia incluses, mais il peut
utiliser un extracteur externe (comme cdda2wav). Il fournis également
une IHM pour les encodeurs MP3, permettant simplement de prendre un
disque et de le transformer en MP3. La récupération des noms sur
Internet permet également d'avoir les informations sur les pistes
auprès des serveurs CDDB. Grip fonctionne également avec DigitalDJ
pour fournir une version unifiée informatique de votre discothèque.

%description -l es.UTF-8
Grip es una interfaz GTK+ para programas que copian bandas de CD como
cdparanoia y cdda2wav. Permite copiar bandas enteras, o solamente
algunas partes. También le permite llamar su codificador MP3 favorito.
Y también sirve como interfaz para tocar CDs.

%description -l pl.UTF-8
Grip jest odtwarzaczem kompaktów. Może być używany jako front-end do
programów ściągających ścieżki CD oraz kompresujących pliki dźwiękowe
do formatu MP3. Umożliwia ściąganie tak całych jak i wybranych części
utworu. Program ten wspiera protokół CDDB w celu ściągania/wysyłania
danych o kompakcie z/do umożliwiającego tego typu operacje serwera.

%description -l pt_BR.UTF-8
Grip é uma interface GTK+ para programas que copiam faixas de CD como o
cdparanoia e cdda2wav. Ele permite que você copie faixas inteiras, ou
apenas pedaços. Também permite que você chame seu codificador MP3
favorito. Finalmente, ele também serve como interface para tocar CDs.

%description -l zh_CN.UTF-8
Grip 是一个可以在 GNOME 桌面环境下运行的 CD
音乐播放器和抓轨器。它可以使用 内置的 cdparanoia 程序抓轨器
(将音轨存储为文件)，也可以使用外部的抓轨器 (例如:
cdda2wav)。同时提供自动的 MP3 编码前端，还可以自动地从 Internet 上的
光盘数据库中查询光盘曲目。如果协同 DigitalDJ
程序一起工作，您可以创建自己的 “计算机化”的音乐库。

%description -l zh_HK.UTF-8
Grip 是一個可以在 GNOME 桌面環境下執行的 CD
音樂播放器和抓軌器。它可以使 用內置的 cdparanoia 程式抓軌器
(將音軌存為檔案)，也可以使用外部的抓軌器 (例如
cdda2wav)。同時提供自動的 MP3 編碼前端，還可以自動地從 Internet 上
的光碟資料庫中查詢光碟曲目。如果協同 DigitalDJ
程式一起工作，您可以建立 自己的「電腦化」的音樂庫。

%description -l zh_TW.UTF-8
Grip 是一個可以在 GNOME 桌面環境下執行的 CD
音樂播放器和抓軌器。它可以使 用內置的 cdparanoia 程式抓軌器
(將音軌存為檔案)，也可以使用外部的抓軌器 (例如
cdda2wav)。同時提供自動的 MP3 編碼前端，還可以自動地從 Internet 上
的光碟資料庫中查詢光碟曲目。如果協同 DigitalDJ
程式一起工作，您可以建立 自己的「電腦化」的音樂庫。

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pl{_PL,}

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README CREDITS TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
