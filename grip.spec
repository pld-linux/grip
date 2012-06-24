Summary:	Grip, a CD player and ripper/MP3-encoder front-end
Summary(ca):	Reproductor/extractor de CD d'audio
Summary(es):	Grip, interfaz para reproducir CDs y generar MP3s
Summary(fr):	Grip, un lecteur de CD, extracteur, et IHM pour encodeur MP3
Summary(ja):	CD �ץ졼�䡼/��å�/MP3���󥳡��� �ե��ȥ����
Summary(pl):	Grip, odtwarzacz CD z frontendem do ripowania i kodowania MP3
Summary(pt_BR):	Grip, interface para reproduzir CDs e gerar MP3s
Summary(zh_CN):	Grip ��һ�� CD ��������ץ������ MP3 ������ǰ�˳���
Summary(zh_HK):	Grip �O�@�� CD ���񾹡B��y���M MP3 �s�X���e�ݵ{���C
Summary(zh_TW):	Grip �O�@�� CD ���񾹡B��y���M MP3 �s�X���e�ݵ{���C
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
capacit�s d'extraction du type cdparanoia incluses, mais il peut
utiliser un extracteur externe (comme cdda2wav). Il fournis �galement
une IHM pour les encodeurs MP3, permettant simplement de prendre un
disque et de le transformer en MP3. La r�cup�ration des noms sur
Internet permet �galement d'avoir les informations sur les pistes
aupr�s des serveurs CDDB. Grip fonctionne �galement avec DigitalDJ
pour fournir une version unifi�e informatique de votre discoth�que.

%description -l es
Grip es una interfaz GTK para programas que copian bandas de CD como
cdparanoia y cdda2wav. Permite copiar bandas enteras, o solamente
algunas partes. Tambi�n le permite llamar su codificador MP3 favorito.
Y tambi�n sirve como interfaz para tocar CDs.

%description -l pl
Grip jest odtwarzaczem kompakt�w. Mo�e by� u�ywany jako front-end do
program�w �ci�gaj�cych �cie�ki CD oraz kompresuj�cych pliki d�wi�kowe
do formatu MP3. Umo�liwia �ci�ganie tak ca�ych jak i wybranych cz�ci
utworu. Program ten wspiera protok� CDDB w celu �ci�gania/wysy�ania
danych o kompakcie z/do umo�liwiaj�cego tego typu operacje serwera.

%description -l pt_BR
Grip � uma interface GTK para programas que copiam faixas de CD como o
cdparanoia e cdda2wav. Ele permite que voc� copie faixas inteiras, ou
apenas peda�os. Tamb�m permite que voc� chame seu codificador MP3
favorito. Finalmente, ele tamb�m serve como interface para tocar CDs.

%description -l zh_CN
Grip ��һ�������� GNOME ���滷�������е� CD
���ֲ�������ץ������������ʹ�� ���õ� cdparanoia ����ץ����
(������洢Ϊ�ļ�)��Ҳ����ʹ���ⲿ��ץ���� (����:
cdda2wav)��ͬʱ�ṩ�Զ��� MP3 ����ǰ�ˣ��������Զ��ش� Internet �ϵ�
�������ݿ��в�ѯ������Ŀ�����Эͬ DigitalDJ
����һ�����������Դ����Լ��� ����������������ֿ⡣

%description -l zh_HK
Grip �O�@�ӥi�H�b GNOME �ୱ���ҤU���檺 CD
���ּ��񾹩M��y���C���i�H�� �Τ��m�� cdparanoia �{����y��
(�N���y�s���ɮ�)�A�]�i�H�ϥΥ~������y�� (�Ҧp
cdda2wav)�C�P�ɴ��Ѧ۰ʪ� MP3 �s�X�e�ݡA�٥i�H�۰ʦa�q Internet �W
�����и�Ʈw���d�ߥ��Ц��ءC�p�G��P DigitalDJ
�{���@�_�u�@�A�z�i�H�إ� �ۤv���u�q���ơv�����֮w�C

%description -l zh_TW
Grip �O�@�ӥi�H�b GNOME �ୱ���ҤU���檺 CD
���ּ��񾹩M��y���C���i�H�� �Τ��m�� cdparanoia �{����y��
(�N���y�s���ɮ�)�A�]�i�H�ϥΥ~������y�� (�Ҧp
cdda2wav)�C�P�ɴ��Ѧ۰ʪ� MP3 �s�X�e�ݡA�٥i�H�۰ʦa�q Internet �W
�����и�Ʈw���d�ߥ��Ц��ءC�p�G��P DigitalDJ
�{���@�_�u�@�A�z�i�H�إ� �ۤv���u�q���ơv�����֮w�C

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
