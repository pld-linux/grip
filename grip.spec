Summary:     Grip, a CD player and ripper/MP3-encoder front-end
Name:        grip
Version:     2.1
Release:     1
Copyright:   GPL
Group:       Applications/Sound
Source:      http://www.ling.ed.ac.uk/~oliphant/grip/grip-2.1.tgz
Patch0:      grip-%{version}.install.patch
URL:         http://www.ling.ed.ac.uk/~oliphant/grip
Buildroot:   /tmp/%{name}-root
Buildprereq: glib => 1.2, gtk+ => 1.2

%description
Grip is a gtk-based cd-player and front-end for cd-rippers and MP3
encoders. It allows you to rip entire tracks, or pinpoint a section of a
track to rip. The CDDB protocol is supported for retreiving/submitting track
information from/to disc database servers.

%description -l pl
Grip jest 

%prep
%setup -q
%patch0 -p1

%build
make AUXDIR=/etc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make PREFIX=$RPM_BUILD_ROOT/usr AUXDIR=$RPM_BUILD_ROOT/etc install
gzip -9nf README CREDITS LICENSE TODO
install -d $RPM_BUILD_ROOT/usr/share/pixmaps
install gripicon.tif $RPM_BUILD_ROOT/usr/share/pixmaps/gripicon.tiff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CREDITS,LICENSE,TODO}.gz
%attr(755,root,root) /usr/bin/grip
%attr(644,root,root) /usr/share/pixmaps/gripicon.tiff
%attr(644,root,root) /etc/grip.rc
