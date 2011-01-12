#
# please keep this file backportable on the system running on kenobi
#
%define my_py_ver %(echo %py_ver | tr -d -c '[:digit:]')
%if "%my_py_ver" == ""
# Assume 2.6 if we don't have python at src.rpm creation time
%define my_py_ver 26
%endif

Name: mgarepo
Version: 1.9.5
Release: %mkrel 1
Summary: Tools for Mageia repository access and management
Group: Development/Other
Source: %{name}-%{version}.tar.bz2
License: GPL
URL: http://svn.mageia.org/svn/soft/build_system/mgarepo/
Requires: python-cheetah subversion openssh-clients python-rpm
%py_requires -d
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

%description
Tools for Mageia repository access and management.

It is a fork of repsys :
<http://wiki.mandriva.com/en/Development/Packaging/Tools/repsys>


%package ldap
Group: Development/Other
Summary: mgarepo plugin to retrieve maintainer information from LDAP
Requires: mgarepo >= 1.6.16 python-ldap

%description ldap
A mgarepo plugin that allows retrieving maintainer information shown in
changelogs from a LDAP server. 

See repsys --help-plugin ldapusers for more information. Also see
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
mkdir -p %{buildroot}%{_datadir}/repsys/
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 create-srpm %{buildroot}%{_datadir}/repsys/create-srpm
install -m 0755 repsys-ssh %{buildroot}%{_bindir}/repsys-ssh
install -m 0644 repsys.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES repsys-example.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/repsys.conf
%{_bindir}/repsys
%{_bindir}/repsys-ssh
%{_datadir}/repsys
%{_mandir}/*/*
%{py_puresitedir}/RepSys
%exclude %{py_puresitedir}/RepSys/plugins/ldapusers.py*
%if %my_py_ver >= 25
%{py_puresitedir}/*.egg-info
%endif

%files ldap
%doc README.LDAP
%{py_puresitedir}/RepSys/plugins/ldapusers.py*

