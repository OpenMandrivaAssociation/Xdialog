Summary:	A replacement for the cdialog program for X
Name:		Xdialog
Version:	2.3.1
Release:	%mkrel 2
Source0:	%{name}-%{version}.tar.bz2
Patch0:		Xdialog-2.2.1-fix-str-fmt.patch
Group:		Development/Other
License:	GPL
URL:		http://xdialog.dyns.net/
BuildRequires:  bison
BuildRequires:  gtk+2-devel
BuildRequires:  glib2-devel
Provides:	xmsg-dialog
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and the treeview adds an
extra dimension to the way menus can be displayed.

%prep
%setup -q
%patch0 -p0

%build

%configure2_5x --with-gtk2

# don't strip (retarded crap!)
find -type f -name "Makefile" | xargs perl -pi -e "s|^INSTALL_STRIP_PROGRAM.*|INSTALL_STRIP_PROGRAM = \"\\\${SHELL} \\\$\(install_sh\) -c\"|g"
find -type f -name "Makefile" | xargs perl -pi -e "s|INSTALL_STRIP_FLAG=-s|INSTALL_STRIP_FLAG=|g" 
find -type f -name "Makefile" | xargs perl -pi -e "s|-Wall -s|-Wall|g" 

%make

%install
rm -rf %{buildroot}

%makeinstall docdir=%{buildroot}%{_docdir}/%{name}

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING samples
%doc doc/*.html doc/*.png
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.1-2mdv2011.0
+ Revision: 671976
- mass rebuild

* Wed Dec 01 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.3.1-1mdv2011.0
+ Revision: 604385
- New version: 2.3.1
- Remove unneeded X11-devel and autoconf BR

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-6mdv2010.1
+ Revision: 521916
- rebuilt for 2010.1

* Wed Apr 15 2009 Funda Wang <fwang@mandriva.org> 2.2.1-5mdv2010.0
+ Revision: 367267
- fix str fmt

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.2.1-5mdv2009.0
+ Revision: 226029
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-4mdv2008.1
+ Revision: 179998
- fix build
- don't strip the binary
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel


* Tue Dec 05 2006 Pascal Terjan <pterjan@mandriva.org> 2.2.1-2mdv2007.0
+ Revision: 91332
- Use gtk2 and autoconf2.5
- Import Xdialog

* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 2.2.1-1mdk
- 2.2.1

* Fri Jan 13 2006 Eskild Hustvedt <eskild@mandriva.org> 2.1.1-4mdk
- Provides xmsg-dialog
- %%mkrel
- Minor summary change

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.1.1-3mdk
- Rebuild

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1.1-2mdk
- rebuild

