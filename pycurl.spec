#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycurl
Version  : 7.43.0
Release  : 23
URL      : https://dl.bintray.com/pycurl/pycurl/pycurl-7.43.0.tar.gz
Source0  : https://dl.bintray.com/pycurl/pycurl/pycurl-7.43.0.tar.gz
Summary  : PycURL -- A Python Interface To The cURL library
Group    : Development/Tools
License  : HPND LGPL-2.1
Requires: pycurl-python
Requires: pycurl-doc
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libidn)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev

%description
PycURL -- A Python Interface To The cURL library
================================================

%package doc
Summary: doc components for the pycurl package.
Group: Documentation

%description doc
doc components for the pycurl package.


%package python
Summary: python components for the pycurl package.
Group: Default

%description python
python components for the pycurl package.


%prep
%setup -q -n pycurl-7.43.0

%build
export LANG=C
python2 setup.py build -b py2 --with-ssl
python3 setup.py build -b py3 --with-ssl

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/pycurl/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
