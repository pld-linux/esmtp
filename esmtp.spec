Summary:	esmtp - relay-only Mail Transfer Agent
Summary(pl.UTF-8):   esmtp - MTA obsługujący tylko przekazywanie poczty do serwera (E)SMTP
Name:		esmtp
Version:	0.5.1
Release:	0.3
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/esmtp/%{name}-%{version}.tar.bz2
# Source0-md5:	9f0b809e891a548910f099efc4315b02
URL:		http://esmtp.sourceforge.net/
BuildRequires:	libesmtp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
esmtp is a user configurable relay-only Mail Transfer Agent (MTA) with
a sendmail compatible syntax. It's based on libESMTP supporting the
AUTH (including the CRAM-MD5 and NTLM SASL mechanisms) and the
StartTLS SMTP extensions.

%description -l pl.UTF-8
esmtp to konfigurowalny przez użytkownika MTA (Mail Transfer Agent) o
składni kompatybilnej z sendmailem, obsługujący wyłącznie
przekazywanie poczty do serwera (E)SMTP. Jest oparty na libESMTP,
obsługuje AUTH (włącznie z mechanizmami SASL CRAM-MD5 i NTLM) oraz
rozszerzenia SMTP StartTLS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install sample.esmtprc	$RPM_BUILD_ROOT%{_sysconfdir}/esmtprc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/esmtp.1*
%{_mandir}/man5/esmtprc.5*
