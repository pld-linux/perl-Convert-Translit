#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Translit
%define		__find_requires %{_builddir}/Convert-Translit-%{version}/find-perl-requires
%define		__find_provides %{_builddir}/Convert-Translit-%{version}/find-perl-provides
Summary:	Convert::Translit - Perl module for string conversion among numerous character sets
Summary(pl):	Convert::Translit - modu³ Perla do konwersji tekstów pomiêdzy ró¿nymi zestawami znaków
Name:		perl-Convert-Translit
Version:	1.03
Release:	10
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcf7e8811f2ee1bbf5ca1f547d1b02dc
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Translit Perl module provides the function "transliterate"
for transliterating strings between any 8-bit character sets defined
in RFC 1345 (about 128 character sets).  The RFC document is included
so you can look up character set names and aliases (and it's also read
by the module when creating transliteration maps).

%description -l pl
Modu³ Perla Convert::Translit udostêpnia funkcjê "transliterate" do
konwersji tekstów pomiêdzy dowolnymi 8-bitowymi zestawami znaków
zdefiniowanymi w RFC 1345 (oko³o 128 zestawów znaków). Dokument RFC
jest do³±czony do pakietu, co umo¿liwia poszukiwanie nazw zestawów
znaków i ich aliasów (i jest on równie¿ czytany przez modu³ podczas
tworzenia odwzorowañ konwersji).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

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
install example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
