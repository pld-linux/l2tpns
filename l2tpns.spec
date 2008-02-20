# TODO
# - detects HAVE_EPOLL from uname -r
Summary:	High-speed clustered L2TP LNS
Name:		l2tpns
Version:	2.1.21
Release:	1
License:	GPL
Group:		Networking/Daemons
URL:		http://sourceforge.net/projects/l2tpns/
Source0:	http://dl.sourceforge.net/l2tpns/%{name}-%{version}.tar.gz
# Source0-md5:	385c58055723ebc6c38062acd2db9c2c
Source1:	%{name}.init
Source2:	%{name}.logrotate
BuildRequires:	libcli-devel >= 1.8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
l2tpns is a layer 2 tunneling protocol network server (LNS). It
supports up to 65535 concurrent sessions per server/cluster plus ISP
features such as rate limiting, walled garden, usage accounting, and
more.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTIM="%{rpmcflags}" \
	libdir=%{_libdir}/l2tpns

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d}

%{__make} install \
	INSTALL="install -c -D" \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}/l2tpns

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/l2tpns
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/l2tpns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL INTERNALS THANKS Docs/*.html
%attr(754,root,root) /etc/rc.d/init.d/l2tpns
%attr(640,root,root) /etc/logrotate.d/l2tpns
%config(noreplace) %{_sysconfdir}/l2tpns
%dir %{_libdir}/l2tpns
%attr(755,root,root) %{_libdir}/l2tpns/*.so
%attr(755,root,root) %{_sbindir}/l2tpns
%attr(755,root,root) %{_sbindir}/nsctl
%{_mandir}/man5/startup-config.5*
%{_mandir}/man8/l2tpns.8*
%{_mandir}/man8/nsctl.8*
