Summary:	Simple Daemon for mks32 for Linux
Summary(pl):	Prosty demon dla mks32 dla Linuksa
Name:		mks_d
Version:	20040410
Release:	4
License:	GPL
Group:		Daemons
Source0:	http://duch.mimuw.edu.pl/~hunter/mks_d/mksd-%{version}.tar.bz2
# Source0-md5:	b5874b1dfaf482570977b63f783b6226
BuildRequires:	sharutils
Requires:	mks
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Daemon for mks32 for Linux. This version of daemon was created
before and independendly of Mks_vir's(R) tool, it differs in license
(GPL) and doesn't require advertising mks_vir on your web (as
comercial one does).

%description -l pl
Prosty demon dla mks32 dla Linuksa. Ta wersja demona powsta³a
niezale¿nie i przed produktem firmy Mks_vir, ró¿ni siê licencj± (GPL)
i nie wymaga reklamowania mks_vir na stronie www (jak w komercyjnym
mksd).

%prep
%setup -q -n mksd

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/spool/virus/mks,/etc/rc.d/init.d,%{_bindir}}

install mks_c mks_d $RPM_BUILD_ROOT%{_bindir}
install rc.d_mks $RPM_BUILD_ROOT/etc/rc.d/init.d/mksd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(640,root,root,750)
%doc JAK_TO_DZIALA Changes *.html README PO-CO TODO
%attr(750,root,root) /var/spool/virus/mks
%attr(754,root,root) /etc/rc.d/init.d/mksd
%attr(755,root,root) %{_bindir}/mks_*
