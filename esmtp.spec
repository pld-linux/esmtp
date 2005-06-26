Summary:	esmtp - relay-only Mail Transfer Agent
Summary(pl):	esmtp - MTA obs�uguj�cy tylko przekazywanie poczty do serwera (E)SMTP
Name:		esmtp
Version:	0.5.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/esmtp/%{name}-%{version}.tar.bz2
# Source0-md5:	9f0b809e891a548910f099efc4315b02
URL:		http://esmtp.sourceforge.net/
BuildRequires:	libesmtp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description	
esmtp is a user configurable relay-only Mail Transfer
Agent (MTA) with a sendmail compatible syntax. It's based on libESMTP
supporting the AUTH (including the CRAM-MD5 and NTLM SASL mechanisms)
and the StartTLS SMTP extensions.

%description -l pl
esmtp to konfigurowalny przez u�ytkownika MTA (Mail Transfer Agent) o
sk�adni kompatybilnej z sendmailem, obs�uguj�cy wy��cznie
przekazywanie poczty do serwera (E)SMTP. Jest oparty na libESMTP,
obs�uguje AUTH (w��cznie z mechanizmami SASL CRAM-MD5 i NTLM) oraz
rozszerzenia SMTP StartTLS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/esmtp.1*
%{_mandir}/man5/esmtprc.5*
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}