Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(ca):	Reproductor/extractor de CD d'audio
Summary(es):	Grip, interfaz para reproducir CDs y generar MP3s
Summary(fr):	Grip, un lecteur de CD, extracteur, et IHM pour encodeur MP3
Summary(ja):	CD ¥×¥ì¡¼¥ä¡¼/¥ê¥Ã¥Ñ/MP3¥¨¥ó¥³¡¼¥À ¥Õ¥í¥ó¥È¥¨¥ó¥É
Summary(pl):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Summary(pt_BR):	Grip, interface para reproduzir CDs e gerar MP3s
Summary(zh_CN):	Grip ÊÇÒ»¸ö CD ²¥·ÅÆ÷¡¢×¥¹ìÆ÷ºÍ MP3 ±àÂëÆ÷Ç°¶Ë³ÌÐò¡£
Summary(zh_HK):	Grip ¬O¤@­Ó CD ¼½©ñ¾¹¡B§ì­y¾¹©M MP3 ½s½X¾¹«eºÝµ{¦¡¡C
Summary(zh_TW):	Grip ¬O¤@­Ó CD ¼½©ñ¾¹¡B§ì­y¾¹©M MP3 ½s½X¾¹«eºÝµ{¦¡¡C
Name:		grip
Version:	3.0.7
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.nostatic.org/grip/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
URL:		http://www.nostatic.org/grip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libghttp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grip is a gtk-based cd-player and front-end for cd-rippers and MP3
encoders. It allows you to rip entire tracks, or pinpoint a section of
a track to rip. The CDDB protocol is supported for
retreiving/submitting track information from/to disc database servers.

%description -l fr
Grip est un lecteur-extracteur de CD pour le Bureau GNome. Il a des
capacités d'extraction du type cdparanoia incluses, mais il peut
utiliser un extracteur externe (comme cdda2wav). Il fournis également
une IHM pour les encodeurs MP3, permettant simplement de prendre un
disque et de le transformer en MP3. La récupération des noms sur
Internet permet également d'avoir les informations sur les pistes
auprès des serveurs CDDB. Grip fonctionne également avec DigitalDJ
pour fournir une version unifiée informatique de votre discothèque.

%description -l es
Grip es una interfaz GTK para programas que copian bandas de CD como
cdparanoia y cdda2wav. Permite copiar bandas enteras, o solamente
algunas partes. También le permite llamar su codificador MP3 favorito.
Y también sirve como interfaz para tocar CDs.

%description -l pl
Grip jest odtwarzaczem kompaktów. Mo¿e byæ u¿ywany jako front-end do
programów ¶ci±gaj±cych ¶cie¿ki CD oraz kompresuj±cych pliki d¼wiêkowe
do formatu MP3. Umo¿liwia ¶ci±ganie tak ca³ych jak i wybranych czê¶ci
utworu. Program ten wspiera protokó³ CDDB w celu ¶ci±gania/wysy³ania
danych o kompakcie z/do umo¿liwiaj±cego tego typu operacje serwera.

%description -l pt_BR
Grip é uma interface GTK para programas que copiam faixas de CD como o
cdparanoia e cdda2wav. Ele permite que você copie faixas inteiras, ou
apenas pedaços. Também permite que você chame seu codificador MP3
favorito. Finalmente, ele também serve como interface para tocar CDs.

%description -l zh_CN
Grip ÊÇÒ»¸ö¿ÉÒÔÔÚ GNOME ×ÀÃæ»·¾³ÏÂÔËÐÐµÄ CD
ÒôÀÖ²¥·ÅÆ÷ºÍ×¥¹ìÆ÷¡£Ëü¿ÉÒÔÊ¹ÓÃ ÄÚÖÃµÄ cdparanoia ³ÌÐò×¥¹ìÆ÷
(½«Òô¹ì´æ´¢ÎªÎÄ¼þ)£¬Ò²¿ÉÒÔÊ¹ÓÃÍâ²¿µÄ×¥¹ìÆ÷ (ÀýÈç:
cdda2wav)¡£Í¬Ê±Ìá¹©×Ô¶¯µÄ MP3 ±àÂëÇ°¶Ë£¬»¹¿ÉÒÔ×Ô¶¯µØ´Ó Internet ÉÏµÄ
¹âÅÌÊý¾Ý¿âÖÐ²éÑ¯¹âÅÌÇúÄ¿¡£Èç¹ûÐ­Í¬ DigitalDJ
³ÌÐòÒ»Æð¹¤×÷£¬Äú¿ÉÒÔ´´½¨×Ô¼ºµÄ ¡°¼ÆËã»ú»¯¡±µÄÒôÀÖ¿â¡£

%description -l zh_HK
Grip ¬O¤@­Ó¥i¥H¦b GNOME ®à­±Àô¹Ò¤U°õ¦æªº CD
­µ¼Ö¼½©ñ¾¹©M§ì­y¾¹¡C¥¦¥i¥H¨Ï ¥Î¤º¸mªº cdparanoia µ{¦¡§ì­y¾¹
(±N­µ­y¦s¬°ÀÉ®×)¡A¤]¥i¥H¨Ï¥Î¥~³¡ªº§ì­y¾¹ (¨Ò¦p
cdda2wav)¡C¦P®É´£¨Ñ¦Û°Êªº MP3 ½s½X«eºÝ¡AÁÙ¥i¥H¦Û°Ê¦a±q Internet ¤W
ªº¥úºÐ¸ê®Æ®w¤¤¬d¸ß¥úºÐ¦±¥Ø¡C¦pªG¨ó¦P DigitalDJ
µ{¦¡¤@°_¤u§@¡A±z¥i¥H«Ø¥ß ¦Û¤vªº¡u¹q¸£¤Æ¡vªº­µ¼Ö®w¡C

%description -l zh_TW
Grip ¬O¤@­Ó¥i¥H¦b GNOME ®à­±Àô¹Ò¤U°õ¦æªº CD
­µ¼Ö¼½©ñ¾¹©M§ì­y¾¹¡C¥¦¥i¥H¨Ï ¥Î¤º¸mªº cdparanoia µ{¦¡§ì­y¾¹
(±N­µ­y¦s¬°ÀÉ®×)¡A¤]¥i¥H¨Ï¥Î¥~³¡ªº§ì­y¾¹ (¨Ò¦p
cdda2wav)¡C¦P®É´£¨Ñ¦Û°Êªº MP3 ½s½X«eºÝ¡AÁÙ¥i¥H¦Û°Ê¦a±q Internet ¤W
ªº¥úºÐ¸ê®Æ®w¤¤¬d¸ß¥úºÐ¦±¥Ø¡C¦pªG¨ó¦P DigitalDJ
µ{¦¡¤@°_¤u§@¡A±z¥i¥H«Ø¥ß ¦Û¤vªº¡u¹q¸£¤Æ¡vªº­µ¼Ö®w¡C

%prep
%setup  -q
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README CREDITS TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
