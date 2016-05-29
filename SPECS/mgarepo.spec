%define Uname	MgaRepo

Name:		mgarepo
Version:	1.12.2
Release:	%mkrel 1
Summary:	Tools for Mageia repository access and management
Group:		Development/Other
License:	GPLv2+
URL:		https://wiki.mageia.org/en/Mgarepo
# tarball needs to be created manually if new version has not been tagged yet
# git clone git://git.mageia.org/software/build-system/mgarepo; cd mgarepo && make dist
Source0:	http://gitweb.mageia.org/software/build-system/mgarepo/snapshot/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)

Requires:	openssh-clients
#Requires:	python-cheetah
Requires:	pythonegg(3)(httplib2)
Requires:	pythonegg(3)(rpm-python)
Requires:	rpm-mageia-setup-build
Requires:	subversion
Requires:	wget

%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://archive.openmandriva.org/wiki/en/index.php?title=Repsys>

%package	ldap
Summary:	Mgarepo plug-in to retrieve maintainer information from LDAP
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	pythonegg(3)(ldap3)

%description	ldap
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
