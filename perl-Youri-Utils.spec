%define module	Youri-Utils

Name:		perl-%{module}
Version:	0.2.1
Release:	7
Summary:	Youri shared functions
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{module}-v%{version}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl-devel
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(version)
Requires:	perl(version)
BuildArch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This package provides basic utility functions used by other youri programs.

%prep
%setup -q -n %{module}-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc ChangeLog README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-5mdv2010.0
+ Revision: 430677
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-4mdv2009.0
+ Revision: 268889
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-3mdv2009.0
+ Revision: 210951
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-2mdv2008.0
+ Revision: 17191
- force dependency on perl-version

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 17030
- new version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2007.1
+ Revision: 138939
- fix build dependencies _correctly_
- fix build dependencies
- Imported perl-Youri-Utils-0.1.1-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2007.1
- first mdv release

