Summary: NethServer configuration for LemonLDAP::NG
%define name nethserver-lemonldap-ng
%define version 0.2.3
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://github.com/danb35/nethserver-lemonldap-ng

BuildRequires: nethserver-devtools
Requires: lemonldap-ng-2.0.11-1.el7 lasso lasso-perl
Requires: nethserver-release = 7
#AutoReq: no

%description
NethServer configuration for LemonLDAP::NG
(https://lemonldap-ng.org/welcome/)

%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} $RPM_BUILD_ROOT > default.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files -f default.lst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Aug  4 2021 Dan Brown <dan@familybrown.org> 0.2.3-1.ns7
- Allow IP-based access restriction on manager

* Wed Jul 28 2021 Dan Brown <dan@familybrown.org> 0.2.2-3.ns7
- Moved cfgDate check

* Tue Jul 27 2021 Dan Brown <dan@familybrown.org> 0.2.2-2.ns7
- Fix exported vars for local OpenLDAP

* Tue Jul 27 2021 Dan Brown <dan@familybrown.org> 0.2.2-1.ns7
- Warn on re-running lemon_config.sh

* Mon Jul 26 2021 Dan Brown <dan@familybrown.org> 0.2.1-1.ns7
- Workaround for https://gitlab.ow2.org/lemonldap-ng/lemonldap-ng/-/issues/2566

* Sat Jul 10 2021 Dan Brown <dan@familybrown.org> 0.2.0-6.ns7
- Properly set exported vars

* Wed Jun 30 2021 Dan Brown <dan@familybrown.org> 0.2.0-5.ns7
- Remove Register button
- Really shrink Nethserver logo

* Tue Jun 29 2021 Dan Brown <dan@familybrown.org> 0.2.0-4.ns7
- Configure some uniform exported LDAP variables
- Shrink login page logo

* Mon Jun 28 2021 Dan Brown <dan@familybrown.org> 0.2.0-3.ns7
- Fix background for logo

* Mon Jun 28 2021 Dan Brown <dan@familybrown.org> 0.2.0-2.ns7
- Add support for remote LDAP authentication

* Sun Jun 27 2021 Dan Brown <dan@familybrown.org> 0.2.0-1.ns7
- Include Nethserver branding
- Support for Active Directory authentication

* Sat Jun 26 2021 Dan Brown <dan@familybrown.org> 0.1.0-8.ns7
- Fix virtual host redirect for ACME HTTP validation

* Thu Jun 17 2021 Dan Brown <dan@familybrown.org> 0.1.0-7.ns7
- Fix templates for z-lemonldap-ng-api.conf and z-lemonldap-ng-handler.conf

* Thu Jun 17 2021 Dan Brown <dan@familybrown.org> 0.1.0-6.ns7
- Expand templates for z-lemonldap-ng-api.conf and z-lemonldap-ng-handler.conf

* Thu Jun 17 2021 Dan Brown <dan@familybrown.org> 0.1.0-5.ns7
- Template z-lemonldap-ng-api.conf and z-lemonldap-ng-handler.conf

* Sun Apr  4 2021 Dan Brown <dan@familybrown.org> 0.1.0-4.ns7
- Correct template expansion
- Reload httpd on completion of lemon_config.sh

* Tue Mar 23 2021 Dan Brown <dan@familybrown.org> 0.1.0-3.ns7
- Correct TLS certificate path when no config property present

* Thu Mar 18 2021 Dan Brown <dan@familybrown.org> 0.1.0-2.ns7
- Fixed error in createlinks

* Thu Mar 18 2021 Dan Brown <dan@familybrown.org> 0.1.0-1.ns7
- Initial Release
