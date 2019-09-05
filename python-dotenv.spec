%global srcname dotenv
%global pkgname python-dotenv
%global sum Get and set values in your .env file in local and production servers using Python. 

# Hack %{?dist} on CentOS build hosts
%if 0%{?rhel} == 6
  %define dist .el6
%endif
%if 0%{?rhel} == 7
  %define dist .el7
%endif

Summary: %{sum}
Name: python%{python3_pkgversion}-%{srcname}
Version: 0.10.3 
Release: 1%{?dist}
Source0: %{pkgname}-%{version}.tar.gz
Group: System Environment/Base
License: Apache-2.0
URL: https://github.com/theskumar/python-dotenv 
Vendor: theskumar
BuildArch: noarch
BuildRequires: python%{python3_pkgversion}-devel 
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
# Hopefully, we can use this in the future
%{?python_disable_dependency_generator}

%description
%{sum}

%prep
%autosetup -n %{pkgname}-%{version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf %{buildroot}

%files
%{python3_sitelib}/python_%{srcname}*egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/dotenv

%changelog
* Wed Sep 4 2019 Chris Brundage <chris.brundage@atmosphere.tv> 0.10.3-1
- First rpm build

