Summary:	Construct and optionally mail MIME messages
Name:		mime-construct
Version:	1.9
Release:	%mkrel 1
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


