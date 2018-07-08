#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Hash-Flatten
Version  : 1.19
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-1.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BB/BBC/Hash-Flatten-1.19.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhash-flatten-perl/libhash-flatten-perl_1.19-2.debian.tar.xz
Summary  : flatten/unflatten complex data hashes
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Hash-Flatten-license
Requires: perl-Hash-Flatten-man
Requires: perl(Log::Trace)
Requires: perl(Test::Assertions)
BuildRequires : perl(Log::Trace)
BuildRequires : perl(Test::Assertions)

%description
Hash::Flatten v1.19
(c) BBC 2004. This program is free software; you can redistribute it and/or
modify it under the GNU GPL.

%package license
Summary: license components for the perl-Hash-Flatten package.
Group: Default

%description license
license components for the perl-Hash-Flatten package.


%package man
Summary: man components for the perl-Hash-Flatten package.
Group: Default

%description man
man components for the perl-Hash-Flatten package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Hash-Flatten-1.19
mkdir -p %{_topdir}/BUILD/Hash-Flatten-1.19/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Hash-Flatten-1.19/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Hash-Flatten
cp COPYING %{buildroot}/usr/share/doc/perl-Hash-Flatten/COPYING
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Hash-Flatten/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Hash/Flatten.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Hash-Flatten/COPYING
/usr/share/doc/perl-Hash-Flatten/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Hash::Flatten.3
