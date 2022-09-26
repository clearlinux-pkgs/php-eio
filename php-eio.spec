#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-eio
Version  : 3.0.0rc4
Release  : 21
URL      : https://github.com/rosmanov/pecl-eio/archive/refs/tags/3.0.0RC4.tar.gz
Source0  : https://github.com/rosmanov/pecl-eio/archive/refs/tags/3.0.0RC4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
BuildRequires : buildreq-php

%description
# Eio PECL Extension
[![Build Status](https://travis-ci.com/rosmanov/pecl-eio.svg?branch=master)](https://travis-ci.com/rosmanov/pecl-eio)


%package lib
Summary: lib components for the  php-eio package.
Group: Libraries
Requires:  php-eio-license = %{version}-%{release}

%description lib
lib components for the php-eio package.


%package license
Summary: license components for the znc package.
Group: Default

%description license
license components for the php-eio package.


%prep
%setup -q -n pecl-eio-3.0.0RC4
cd %{_builddir}/pecl-eio-3.0.0RC4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-eio
cp %{_builddir}/pecl-eio-3.0.0RC4/LICENSE %{buildroot}/usr/share/package-licenses/php-eio/27b46923d7341b6bb717d06db4850b1180d565b2
cp %{_builddir}/pecl-eio-3.0.0RC4/libeio/LICENSE %{buildroot}/usr/share/package-licenses/php-eio/fea251a93b840fb5da2ba0ea287c76507fd99303
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/eio.so

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/php-eio/27b46923d7341b6bb717d06db4850b1180d565b2
/usr/share/package-licenses/php-eio/fea251a93b840fb5da2ba0ea287c76507fd99303
