%define	pdir	Convert
%define	pnam	Translit
%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/Convert-Translit-%{version}/find-perl-requires
%define		__find_provides %{_builddir}/Convert-Translit-%{version}/find-perl-provides
Summary:	Convert-Translit perl module
Summary(pl):	Modu� perla Convert-Translit
Name:		perl-Convert-Translit
Version:	1.03
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Translit - module for string conversion among numerous
character sets.

%description -l pl
Convert-Translit - modu� do konwersji �a�cuch�w pomi�dzy r�nymi
zestawami znak�w.

%prep
%setup -q -n Convert-Translit-%{version}
%patch -p1

chmod +x find-perl-*

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example.pl
%{perl_sitelib}/Convert/Translit.pm
%{perl_sitelib}/Convert/rfc1345
%{perl_sitelib}/Convert/substitutes
%{_mandir}/man3/*
