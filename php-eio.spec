#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-eio
Version  : 2.0.4
Release  : 11
URL      : https://pecl.php.net//get/eio-2.0.4.tgz
Source0  : https://pecl.php.net//get/eio-2.0.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
BuildRequires : buildreq-php

%description
Eio - PECL Extension
====================
DESCRIPTION
-----------
This is a PHP extension wrapping functions of the libeio library written by Marc
Lehmann <libeio@schmorp.de>(see <http://software.schmorp.de/pkg/libeio.html>).

%prep
%setup -q -n eio-2.0.4
cd %{_builddir}/eio-2.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
