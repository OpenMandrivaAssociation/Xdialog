Summary:	A replacement for the cdialog program for X
Name:		Xdialog
Version:	2.3.1
Release:	10
Group:		Development/Other
License:	GPLv2
Url:		http://xdialog.dyns.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		Xdialog-2.2.1-fix-str-fmt.patch
BuildRequires:	bison
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
Provides:	xmsg-dialog

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
%makeinstall docdir=%{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING samples
%doc doc/*.html doc/*.png
%{_bindir}/*
%{_mandir}/man1/*

