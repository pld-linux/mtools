Summary:	Programs to access DOS disks w/o mounting them
Summary(de):	Programme für den Zugriff auf DOS-Disks, ohne sie zu montieren 
Summary(fr):	Programmes pour accéder aux disques DOS sans avoir à les monter
Summary(pl):	Dostêp do dysków DOSa bez montowania
Summary(tr):	Baðlama (mount) yapmadan DOS disklerine eriþim saðlar
Name:		mtools
Version:	3.9.8
Release:	2
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.tux.org/pub/tux/knaff/mtools/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-no_libnsl_and_libbsd.patch
URL:		http://www.tux.org/pub/tux/knaff/mtools/
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Mtools is a collection of utilities to access MS-DOS disks from Unix
without mounting them. It supports Win'95 style long file names, OS/2
Xdf disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high
density 3 1/2 disk).

%description -l de
Mtools ist eine Dienstprogrammsammlung zum Zugriff auf
MS-DOS-Disketten, ohne daß diese montiert werden müssen. Es
unterstützt Win'95-Dateinamen (lang), OS/2-Xdf-, ZIP/JAZ- und
2m-Disketten (speichern bis zu 1992 KB auf einer HD 3 1/2-Diskette).

%description -l fr
Mtools est un ensemble d'utilitaires pour accéder aux disques MS-DOS
depuis UNIX sans les monter. Il supporte les noms longs Windows 95,
les diques Xdf OS/2, les disques ZIP et JAZ et les disques 2m
(stockant 1992k sur une disquette 3,5\").

%description -l pl
Mtools to zbiór narzêdzi udostêpniaj±cych Unixowi DOSowe dyski bez ich
montowania. Obs³uguje d³ugie nazwy Win95, dyski Xdf z OS/2, dyski
ZIP/JAZ i dyski 2m (mieszcz±ce na 3.5-calowej dyskietce do 1992k).

%description -l tr
mtools, MS-DOS disklerine baðlanmadan (mount edilmeden) UNIX
sistemlerinden eriþilebilmesini saðlar. Win'95 tarzý uzun dosya
isimlerini, OS/2 Xdf disklerini, ZIP/JAZ disklerini ve 2m disklerini
destekler.

%package floppyd
Summary:	floppyd
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Group:		Applications/System
Requires:	%{name} = %{version}

%description floppyd


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
%configure

%{__make} MYCFLAGS="%{rpmcflags} -Wall"

(makeinfo --force mtools.texi; touch mtools.*)
strip mtools mkmanifest

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

mv -f $RPM_BUILD_ROOT%{_bindir}/floppyd* $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

gzip -9nf Changelog README Release.notes

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mtools.conf
%{_mandir}/man[15]/m*
%{_infodir}/*info*

%files floppyd
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%{_mandir}/man[15]/f*
