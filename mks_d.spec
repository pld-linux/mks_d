# $Id: mks_d.spec,v 1.5 2003-08-21 18:55:34 hunter Exp $
Summary:	Simple Daemon for mks32 for Linux
Summary(pl):	Prosty demon dla mks32 dla Linuksa
Name:		mks_d
Version:	20030821
Release:	1
License:	GPL
Group:		Applications/Deamons
Source0:	http://duch.mimuw.edu.pl/~hunter/mks_d/mksd-%{version}.tar.bz2
#Source0-md5: 847f408e9f072c0274dc4f0f6b131bdf
Requires:	mks
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
install -d $RPM_BUILD_ROOT{/var/spool/virus/mks,%{_sysconfdir}/rc.d/init.d,\
%{_bindir}}

install mks_c mks_d $RPM_BUILD_ROOT%{_bindir}
install rc.d_mks $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/mksd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(640,root,root,750)
%doc JAK_TO_DZIALA Changes *.html 
%attr(750,root,root) /var/spool/virus/mks
%{_sysconfdir}/rc.d/init.d/mksd
%{_bindir}/mks_*
