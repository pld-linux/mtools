Summary:	Programs to access DOS disks w/o mounting them
Summary(de):	Programme für den Zugriff auf DOS-Disks, ohne sie zu montieren 
Summary(fr):	Programmes pour accéder aux disques DOS sans avoir à les monter
Summary(pl):	Dostêp do dysków DOSa bez montowania
Summary(tr):	Baðlama (mount) yapmadan DOS disklerine eriþim saðlar
Name:		mtools
Version:	3.9.6
Release:	5
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	http://www.tux.org/pub/tux/knaff/mtools/%{name}-%{version}.tar.gz 
Source1:	mtools.conf
Patch0:		mtools-info.patch
Patch1:		mtools-mzip.patch
Patch2:		mtools-DESTDIR.patch
Patch3:		mtools-paths.patch
URL:		http://www.tux.org/pub/tux/knaff/mtools/
BuildRequires:	texinfo
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Mtools is a collection of utilities to access MS-DOS disks from Unix without
mounting them. It supports Win'95 style long file names, OS/2 Xdf disks,
ZIP/JAZ disks and 2m disks (store up to 1992k on a high density 3 1/2 disk).

%description -l de
Mtools ist eine Dienstprogrammsammlung zum Zugriff auf MS-DOS-Disketten,
ohne daß diese montiert werden müssen. Es unterstützt Win'95-Dateinamen
(lang), OS/2-Xdf-, ZIP/JAZ- und 2m-Disketten (speichern bis zu 1992 KB auf
einer HD 3 1/2-Diskette).

%description -l fr
Mtools est un ensemble d'utilitaires pour accéder aux disques MS-DOS depuis
UNIX sans les monter. Il supporte les noms longs Windows 95, les diques Xdf
OS/2, les disques ZIP et JAZ et les disques 2m (stockant 1992k sur une
disquette 3,5\").

%description -l pl
Mtools to zbiór narzêdzi udostêpniaj±cych Unixowi DOSowe dyski bez ich
montowania. Obs³uguje d³ugie nazwy Win95, dyski Xdf z OS/2, dyski
ZIP/JAZ i dyski 2m (mieszcz±ce na 3.5-calowej dyskietce do 1992k).

%description -l tr
mtools, MS-DOS disklerine baðlanmadan (mount edilmeden) UNIX sistemlerinden
eriþilebilmesini saðlar. Win'95 tarzý uzun dosya isimlerini, OS/2 Xdf
disklerini, ZIP/JAZ disklerini ve 2m disklerini destekler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

make MYCFLAGS="$RPM_OPT_FLAGS -Wall"

(makeinfo --force mtools.texi; touch mtools.*)
strip mtools mkmanifest

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_sysconfdir}}

make install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man{1,5}/*} \
	Changelog README Release.notes TODO

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changelog,README,Release.notes,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[15]/*
%{_infodir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mtools.conf
