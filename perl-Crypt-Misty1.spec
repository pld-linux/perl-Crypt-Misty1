#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Misty1
Summary:	Crypt::Misty1 - Crypt::CBC-compliant block cipher
Summary(pl):	Crypt::Misty1 - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Misty1
Version:	1.1.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ca9e4ad4db7b249751731a35cae5f9bc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Misty1 is a 64-bit symmetric block cipher with a 128-bit key. It was
developed by Mitsuru Matsui, and is described in the paper "New Block
Encryption Algorithm MISTY" and in RFC 2994. In January of 2000, the
3GPP consortium selected a variant of Misty1, dubbed as KASUMI (the
Japanese word for "misty"), as the mandatory cipher in W-CDMA. This
module supports the Crypt::CBC interface.

%description -l pl
Misty1 to 64-bitowy symetryczny szyfr blokowy ze 128-bitowym kluczem.
Zosta³ opracowany przez Mitsuru Matsui i opisany w dokumencie "New
Block Encryption Algorithm MISTY" oraz w RFC 2994. W styczniu 2000
konsorcjum 3GPP wybra³o wariant Misty1 pod nazw± KASUMI (japoñski
odpowiednik s³owa "misty") jako obowi±zkowy szyfr w W-CDMA. Ten
modu³ obs³uguje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Misty1.pm
%dir %{perl_vendorarch}/auto/Crypt/Misty1
%{perl_vendorarch}/auto/Crypt/Misty1/Misty1.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Misty1/Misty1.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
