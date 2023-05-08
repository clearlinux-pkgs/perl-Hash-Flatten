#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Hash-Flatten
Version  : 1.19
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-1.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-1.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhash-flatten-perl/libhash-flatten-perl_1.19-2.debian.tar.xz
Summary  : flatten/unflatten complex data hashes
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Hash-Flatten-license = %{version}-%{release}
Requires: perl-Hash-Flatten-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Log::Trace)
BuildRequires : perl(Test::Assertions)

%description
Hash::Flatten v1.19
(c) BBC 2004. This program is free software; you can redistribute it and/or
modify it under the GNU GPL.

%package dev
Summary: dev components for the perl-Hash-Flatten package.
Group: Development
Provides: perl-Hash-Flatten-devel = %{version}-%{release}
Requires: perl-Hash-Flatten = %{version}-%{release}

%description dev
dev components for the perl-Hash-Flatten package.


%package license
Summary: license components for the perl-Hash-Flatten package.
Group: Default

%description license
license components for the perl-Hash-Flatten package.


%package perl
Summary: perl components for the perl-Hash-Flatten package.
Group: Default
Requires: perl-Hash-Flatten = %{version}-%{release}

%description perl
perl components for the perl-Hash-Flatten package.


%prep
%setup -q -n Hash-Flatten-1.19
cd %{_builddir}
tar xf %{_sourcedir}/libhash-flatten-perl_1.19-2.debian.tar.xz
cd %{_builddir}/Hash-Flatten-1.19
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Hash-Flatten-1.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Hash-Flatten
cp %{_builddir}/Hash-Flatten-1.19/COPYING %{buildroot}/usr/share/package-licenses/perl-Hash-Flatten/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Hash-Flatten/be1c60dc95faf7d9af7a6f9a7bddea5f5a8f68c9
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Hash::Flatten.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Hash-Flatten/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/perl-Hash-Flatten/be1c60dc95faf7d9af7a6f9a7bddea5f5a8f68c9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
