%include	/usr/lib/rpm/macros.perl
%define		__find_requires %{_builddir}/Convert-Translit-%{version}/find-perl-requires
%define		__find_provides %{_builddir}/Convert-Translit-%{version}/find-perl-provides
Summary:	Convert-Translit perl module
Summary(pl):	Modu³ perla Convert-Translit
Name:		perl-Convert-Translit
Version:	1.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-Translit-%{version}.tar.gz
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Translit - module for string conversion among numerous
character sets.

%description -l pl
Convert-Translit - modu³ do konwersji ³añcuchów pomiêdzy ró¿nymi
zestawami znaków.

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
