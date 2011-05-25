%define Uname MgaRepo
Name: mgarepo
Version: 1.9.10
Release: %mkrel 1
Summary: Tools for Mageia repository access and management
Group: Development/Other
Source: http://distrib-coffee.ipsl.jussieu.fr/pub/linux/Mageia/software/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+
URL: http://svn.mageia.org/svn/soft/build_system/mgarepo/
Requires: python-cheetah subversion openssh-clients python-rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://wiki.mandriva.com/en/Development/Packaging/Tools/repsys>

%package ldap
Group: Development/Other
Summary: Mgarepo plug-in to retrieve maintainer information from LDAP
Requires: mgarepo
Requires: python-ldap

%description ldap
A mgarepo plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server. 

See %{name} --help-plugin ldapusers for more information. Also see
http://qa.mandriva.com/show_bug.cgi?id=30549

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot}
# Using compile inline since niemeyer's python macros still not available on mdk rpm macros
find %{buildroot}%{py_puresitedir} -name '*.pyc' -exec rm -f {} \; 
python -c "import sys, os, compileall; br='%{buildroot}'; compileall.compile_dir(sys.argv[1], ddir=br and 
(sys.argv[1][len(os.path.abspath(br)):]+'/') or None)" %{buildroot}%{py_sitedir}

mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 create-srpm %{buildroot}%{_datadir}/%{name}/create-srpm
install -m 0755 %{name}-ssh %{buildroot}%{_bindir}/%{name}-ssh
install -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES %{name}-example.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-ssh
%{_datadir}/%{name}
%{_mandir}/*/*
%{python_sitelib}/%{Uname}
%exclude %{python_sitelib}/%{Uname}/plugins/ldapusers.py*
%{python_sitelib}/*.egg-info

%files ldap
%defattr(-,root,root)
%doc README.LDAP
%{python_sitelib}/%{Uname}/plugins/ldapusers.py*

