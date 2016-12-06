%define Uname	RepSys

Name:		repsys
Version:	1.14.0
Release:	%mkrel 1
Summary:	Tools for Mageia repository access and management
Group:		Development/Other
License:	GPLv2+
URL:		https://wiki.mageia.org/en/Mgarepo
Source0:	https://github.com/DrakXtools/%{name}/archive/%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)

Requires:	openssh-clients
#Requires:	python-cheetah
Requires:	rpm-mageia-setup-build
Requires:	subversion
Requires:	wget

%description
Tools for repository access and management for Mandrake Linux derived distros.

Original wiki page for available at:
http://archive.openmandriva.org/wiki/en/index.php?title=Repsys

%package	ldap
Summary:	%{Uname} plug-in to retrieve maintainer information from LDAP
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	pythonegg(3)(ldap3)

%description	ldap
A repsys plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server.

See %{name} --help-plugin ldapusers for more information.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

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
