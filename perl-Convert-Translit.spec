%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Convert-Translit perl module
Summary(pl):	Modu³ perla Convert-Translit
Name:		perl-Convert-Translit
Version:	1.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-Translit-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Convert-Translit - module for string conversion among numerous character sets.

%description -l pl
Convert-Translit - modu³ do konwersji ³añcuchów pomiêdzy ró¿nymi zestawami
znaków.

%prep
%setup -q -n Convert-Translit-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/Translit
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitelib}/Convert/Translit.pm
%{perl_sitelib}/Convert/example.pl
%{perl_sitelib}/Convert/rfc1345
%{perl_sitelib}/Convert/substitutes
%{perl_sitearch}/auto/Convert/Translit

%{_mandir}/man3/*
