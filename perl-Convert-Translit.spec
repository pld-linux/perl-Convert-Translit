%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Translit
%define		__find_requires %{_builddir}/Convert-Translit-%{version}/find-perl-requires
%define		__find_provides %{_builddir}/Convert-Translit-%{version}/find-perl-provides
Summary:	Convert::Translit perl module
Summary(pl):	Modu³ perla Convert::Translit
Name:		perl-Convert-Translit
Version:	1.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcf7e8811f2ee1bbf5ca1f547d1b02dc
Patch0:		%{name}-dep.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Translit - module for string conversion among numerous
character sets.

%description -l pl
Convert::Translit - modu³ do konwersji ³añcuchów pomiêdzy ró¿nymi
zestawami znaków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

chmod +x find-perl-*

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
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
