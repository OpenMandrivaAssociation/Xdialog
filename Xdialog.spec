Summary:	A replacement for the cdialog program for X
Name:		Xdialog
Version:	2.2.1
Release:	%mkrel 5
Source0:	%{name}-%{version}.tar.bz2
Patch0:		Xdialog-2.2.1-fix-str-fmt.patch
Group:		Development/Other
License:	GPL
URL:		http://xdialog.dyns.net/
Buildrequires:	bison X11-devel gtk+2-devel glib2-devel autoconf2.5
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
