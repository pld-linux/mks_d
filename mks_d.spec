# $Id: mks_d.spec,v 1.2 2003-08-18 08:08:20 gotar Exp $
Summary:	Simple Daemon for mks32 for Linux
Summary(pl):	Prosty demon dla mks32 dla linuksa
Name:		mksd
Version:	20030815
Release:	1
License:	GPL
Group:		Applications/Deamons
Group(pl):	Aplikacje/Demony
Source0:	http://www.raszyn.pl/~hunter/pliki/%{name}-%{version}.tar.gz
Requires:	mks32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Daemon for mks32 for Linux. This version of daemon was created before
and independendly of Mks_vir's(R) tool, it differs in GPL license and doesn't
require advertising mks_vir on your web (as comercial one does).

%description -l pl
Prosty demon dla mks32 dla Linuksa. Ta wersja demona powsta³a nie zale¿nie
i przed produktem firmy Mks_vir, ró¿ni siê licencj± GPL i nie wymaga
reklamowania mks_vir na stronie www (ja w komercyjnym mksd).

%prep
%setup -q -n %{name}

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/spool/virus/mks/
install mks_c mks_d $RPM_BUILD_ROOT/var/spool/virus/mks/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/
install rc.d_mks $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/mksd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc JAK_TO_DZIALA Changes *.txt
%defattr(640,root,root,750)
%attr(750,root,root) /var/spool/virus/mks
%{_sysconfdir}/rc.d/init.d/mksd
%doc *.gz
