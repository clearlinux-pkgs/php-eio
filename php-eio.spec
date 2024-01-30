#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-eio
Version  : 3.1.0
Release  : 54
URL      : https://github.com/rosmanov/pecl-eio/archive/3.1.0/pecl-eio-3.1.0.tar.gz
Source0  : https://github.com/rosmanov/pecl-eio/archive/3.1.0/pecl-eio-3.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-eio-lib = %{version}-%{release}
Requires: php-eio-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Eio PECL Extension
[![Build Status](https://travis-ci.com/rosmanov/pecl-eio.svg?branch=master)](https://travis-ci.com/rosmanov/pecl-eio)

%package lib
Summary: lib components for the php-eio package.
Group: Libraries
Requires: php-eio-license = %{version}-%{release}

%description lib
lib components for the php-eio package.


%package license
Summary: license components for the php-eio package.
Group: Default

%description license
license components for the php-eio package.


%prep
%setup -q -n pecl-eio-3.1.0
cd %{_builddir}/pecl-eio-3.1.0
pushd ..
cp -a pecl-eio-3.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-eio
cp %{_builddir}/pecl-eio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-eio/27b46923d7341b6bb717d06db4850b1180d565b2 || :
cp %{_builddir}/pecl-eio-%{version}/libeio/LICENSE %{buildroot}/usr/share/package-licenses/php-eio/fea251a93b840fb5da2ba0ea287c76507fd99303 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/eio.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-eio/27b46923d7341b6bb717d06db4850b1180d565b2
/usr/share/package-licenses/php-eio/fea251a93b840fb5da2ba0ea287c76507fd99303
