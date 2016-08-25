%{!?upstream_version: %global upstream_version %{version}}

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global client python-watcherclient
%global sclient watcherclient

Name:       %{client}
Version:    0.24.0
Release:    1%{?dist}
Summary:    OpenStack Watcher client
License:    ASL 2.0
URL:        http://launchpad.net/%{client}/
Source0:    http://tarballs.openstack.org/%{client}/%{client}-%{upstream_version}.tar.gz

BuildArch:  noarch

%package -n python2-%{sclient}
Summary:    OpenStack Watcher client
%{?python_provide:%python_provide python2-%{sclient}}

BuildRequires:  python-devel
BuildRequires:  git
BuildRequires:  python-mock >= 1.2
BuildRequires:  python-coverage >= 3.6
BuildRequires:  python-hacking >= 0.10.2
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildRequires:  python-oslotest >= 1.10.0
BuildRequires:  python-pbr >= 1.6
BuildRequires:  python-setuptools
BuildRequires:  python-keystoneclient >= 1:1.7.0
BuildRequires:  python-cliff
BuildRequires:  python-openstackclient >= 2.1.0
BuildRequires:  python-subunit >= 0.0.18
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 1.4.0
BuildRequires:  python-sphinx >= 1.2.1

Requires:   python-oslo-config >= 2:3.4.0
Requires:   python-babel >= 2.3.4
Requires:   python-cliff >= 1.15.0
Requires:   python-osc-lib >= 0.4.0
Requires:   python-oslo-i18n >= 2.1.0
Requires:   python-oslo-utils >= 3.16.0
Requires:   python-pbr >= 1.6
Requires:   python-prettytable >= 0.7
Requires:   python-keystoneclient >= 1:1.7.0
Requires:   python-openstackclient >= 2.1.0
Requires:   python-six >= 1.9.0
Requires:   python-setuptools

%description -n python2-%{sclient}
OpenStack Watcher client - Python client library for IAAS optimization service

%package -n python2-%{sclient}-tests
Summary:    OpenStack Watcher client tests
Requires:   python2-%{sclient} = %{version}-%{release}
Requires:   python-devel
Requires:   git
Requires:   python-mock >= 1.2
Requires:   python-coverage >= 3.6
Requires:   python-hacking >= 0.10.2
Requires:   python-oslotest >= 1.10.0
Requires:   python-pbr >= 1.6
Requires:   python-setuptools
Requires:   python-subunit >= 0.0.18
Requires:   python-testrepository >= 0.0.18
Requires:   python-testscenarios >= 0.4
Requires:   python-testtools >= 1.4.0
Requires:   python-devel

%description -n python2-%{sclient}-tests
OpenStack Watcher client tests

This package contains the Watcher client test files.


%package -n python-%{sclient}-doc
Summary:    OpenStack Watcher client documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description -n python-%{sclient}-doc
OpenStack Watcher client documentation

This package contains the documentation.

%if 0%{?with_python3}
%package -n python3-%{sclient}
Summary:    OpenStack Watcher client
%{?python_provide:%python_provide python3-%{sclient}}


# NOTE(danpawlik) Package python3-openstackclient is required for
# BuildRequires but it's not available in RDO repo.
BuildRequires:  python3-devel
BuildRequires:  git
BuildRequires:  python3-mock >= 1.2
BuildRequires:  python3-coverage >= 3.6
BuildRequires:  python3-hacking >= 0.10.2
BuildRequires:  python3-oslo-sphinx >= 2.5.0
BuildRequires:  python3-oslotest >= 1.10.0
BuildRequires:  python3-pbr >= 1.6
BuildRequires:  python3-setuptools
BuildRequires:  python3-keystoneclient >= 1:1.7.0
BuildRequires:  python3-cliff
BuildRequires:  python3-subunit >= 0.0.18
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:  python3-testscenarios >= 0.4
BuildRequires:  python3-testtools >= 1.4.0
BuildRequires:  python3-sphinx >= 1.2.1

Requires:   python3-babel >= 2.3.4
Requires:   python3-cliff >= 1.15.0
Requires:   python3-osc-lib >= 0.4.0
Requires:   python3-oslo-i18n >= 2.1.0
Requires:   python3-oslo-utils >= 3.16.0
Requires:   python3-oslo-config >= 2:3.4.0
Requires:   python3-pbr >= 1.6
Requires:   python3-prettytable >= 0.7
Requires:   python3-keystoneclient >= 1:1.7.0
Requires:   python3-six >= 1.9.0
Requires:   python3-setuptools

%description -n python3-%{sclient}
OpenStack Watcher client - Python client library for IAAS optimization service

%package -n python3-%{sclient}-tests
Summary:    OpenStack Watcher client tests
Requires:   python3-%{sclient} = %{version}-%{release}
Requires:   python3-devel
Requires:   python3-pbr >= 1.6
Requires:   python3-setuptools
Requires:   git
Requires:   python3-mock >= 1.2
Requires:   python3-coverage >= 3.6
Requires:   python3-hacking >= 0.10.2
Requires:   python3-oslotest >= 1.10.0
Requires:   python3-subunit >= 0.0.18
Requires:   python3-testrepository >= 0.0.18
Requires:   python3-testscenarios >= 0.4
Requires:   python3-testtools >= 1.4.0

%description -n python3-%{sclient}-tests
OpenStack Watcher client tests

This package contains the Watcher client test files.

%endif # with_python3


%description
OpenStack Watcher library.


%prep
%autosetup -n %{client}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
export PYTHONPATH=.
sphinx-build -b html doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/watcher %{buildroot}%{_bindir}/watcher-%{python3_version}
ln -s ./watcher-%{python3_version} %{buildroot}%{_bindir}/watcher-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/watcher %{buildroot}%{_bindir}/watcher-%{python2_version}
ln -s ./watcher-%{python2_version} %{buildroot}%{_bindir}/watcher-2

ln -s ./watcher-2 %{buildroot}%{_bindir}/watcher

%check
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test
%endif

%{__python2} setup.py test


%files -n python2-%{sclient}
%{_bindir}/watcher
%{_bindir}/watcher-2
%{_bindir}/watcher-%{python2_version}
%license LICENSE
%{python2_sitelib}/%{sclient}
%{python2_sitelib}/*.egg-info
%exclude %{python2_sitelib}/%{sclient}/tests

%files -n python2-%{sclient}-tests
%license LICENSE
%{python2_sitelib}/%{sclient}/tests

%files -n python-%{sclient}-doc
%license LICENSE
%doc html README.rst

%if 0%{?with_python3}
%files -n python3-%{sclient}
%{_bindir}/watcher-3
%{_bindir}/watcher-%{python3_version}
%license LICENSE
%{python3_sitelib}/%{sclient}
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/%{sclient}/tests

%files -n python3-%{sclient}-tests
%license LICENSE
%{python3_sitelib}/%{sclient}/tests
%endif

%changelog
