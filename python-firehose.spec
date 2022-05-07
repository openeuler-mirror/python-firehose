Name:           python-firehose
Version:        0.5
Release:        2
Summary:        Library for working with output from static code analyzers

License:        LGPLv2+
URL:            https://github.com/fedora-static-analysis/firehose
Source0:        %{name}-%{version}.tar.gz
# https://github.com/fedora-static-analysis/firehose/pull/42
Patch0:         0001-Remove-calls-to-deprecated-plistlib-function.patch
BuildArch:      noarch

BuildRequires:  libxml2
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-mock

%global _description\
"firehose" is a Python package intended for managing the results from\
code analysis tools (e.g. compiler warnings, static analysis, linters,\
etc).\

%description %_description

%package -n python3-firehose
Summary:        Library for working with output from static code analyzers
Requires:  python3-six
%{?python_provide:%python_provide python3-firehose}

%description -n python3-firehose %_description


%prep
%setup -q -n firehose-%{version}
%patch0 -p1

%build
%py3_build

%install
%py3_install
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/cppcheck.py
chmod +x %{buildroot}/%{python3_sitelib}/firehose/parsers/gcc.py


%check
%{__python3} -m unittest discover -v


%files -n python3-firehose
%doc README.rst lgpl-2.1.txt examples firehose.rng
%{python3_sitelib}/firehose/
%{python3_sitelib}/firehose-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 17 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.5-2
- Remove calls to deprecated plistlib function

* Mon Jul 05 2021 Lianguo Wang <wanglianguo@kylinos.cn> - 0.5
- Initial package for openEuler, version 0.5
