#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Convert
%define		pnam	Translit
%include	/usr/lib/rpm/macros.perl
Summary:	Convert::Translit - Perl module for string conversion among numerous character sets
Summary(pl.UTF-8):	Convert::Translit - moduł Perla do konwersji tekstów pomiędzy różnymi zestawami znaków
Name:		perl-Convert-Translit
Version:	1.03
Release:	11
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcf7e8811f2ee1bbf5ca1f547d1b02dc
Patch0:		%{name}-dep.patch
URL:		http://search.cpan.org/dist/Convert-Translit/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__find_requires %{_builddir}/Convert-Translit-%{version}/find-perl-requires
%define		__find_provides %{_builddir}/Convert-Translit-%{version}/find-perl-provides

%description
Convert::Translit Perl module provides the function "transliterate"
for transliterating strings between any 8-bit character sets defined
in RFC 1345 (about 128 character sets). The RFC document is included
so you can look up character set names and aliases (and it's also read
by the module when creating transliteration maps).

%description -l pl.UTF-8
Moduł Perla Convert::Translit udostępnia funkcję "transliterate" do
konwersji tekstów pomiędzy dowolnymi 8-bitowymi zestawami znaków
zdefiniowanymi w RFC 1345 (około 128 zestawów znaków). Dokument RFC
jest dołączony do pakietu, co umożliwia poszukiwanie nazw zestawów
znaków i ich aliasów (i jest on również czytany przez moduł podczas
tworzenia odwzorowań konwersji).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

chmod +x find-perl-*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Convert/Translit.pm
%{perl_vendorlib}/Convert/rfc1345
%{perl_vendorlib}/Convert/substitutes
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/example.pl
