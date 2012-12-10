Summary:	Construct and optionally mail MIME messages
Name:		mime-construct
Version:	1.9
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~rosch/mime-construct/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%{name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mime-construct constructs and (by default) mails MIME messages. It
is entirely driven from the command line, it is designed to be
used by other programs, or people who act like programs.

%prep

%setup -q -n %{name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/mime-construct
%{_mandir}/*/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-5mdv2011.0
+ Revision: 620340
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.9-4mdv2010.0
+ Revision: 430043
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.9-3mdv2009.0
+ Revision: 252497
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.9-1mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.9-1mdv2007.0
+ Revision: 131193
- Import mime-construct

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.9-1mdk
- initial Mandriva package

