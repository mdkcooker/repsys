%define Uname MgaRepo
Name: mgarepo
Version: 1.11.0
Release: %mkrel 3
Summary: Tools for Mageia repository access and management
Group: Development/Other
Source0: http://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/software/%{name}/%{version}/%{name}-%{version}.tar.xz
License: GPLv2+
URL: https://wiki.mageia.org/en/Mgarepo
BuildArch: noarch
BuildRequires:  python3
Requires: openssh-clients
#Requires: python-cheetah
Requires: python3-httplib2
Requires: python3-rpm
Requires: rpm-mageia-setup-build
Requires: subversion
Requires: wget

%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://archive.openmandriva.org/wiki/en/index.php?title=Repsys>

%package ldap
Group: Development/Other
Summary: Mgarepo plug-in to retrieve maintainer information from LDAP
Requires: mgarepo
Requires: python-ldap

%description ldap
A mgarepo plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server. 

See %{name} --help-plugin ldapusers for more information.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 create-srpm %{buildroot}%{_datadir}/%{name}/create-srpm
install -m 0755 %{name}-ssh %{buildroot}%{_bindir}/%{name}-ssh
install -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}

%files
%doc CHANGES %{name}-example.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-ssh
%{_datadir}/%{name}
%{_mandir}/*/*
%{python3_sitelib}/%{Uname}
%exclude %{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%exclude %{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers* 
%{python3_sitelib}/*.egg-info
%{_datadir}/bash-completion/completions/%{name}

%files ldap
%doc README.LDAP
%{python3_sitelib}/%{Uname}/plugins/ldapusers.py*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/__init__*
%{python3_sitelib}/%{Uname}/plugins/__pycache__/ldapusers*

