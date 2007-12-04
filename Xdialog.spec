%define name Xdialog
%define version 2.2.1
%define rel	2
%define release %mkrel %rel

Name:		%{name}
Summary:	A replacement for the cdialog program for X
Version:	%{version}
Release:	%{release}

Source:		%name-%version.tar.bz2

Group:		Development/Other
URL:		http://xdialog.dyns.net/
Buildrequires:	bison X11-devel gtk+2-devel glib2-devel autoconf2.5
BuildRoot:	%_tmppath/%name-buildroot
License:	GPL
Provides:	xmsg-dialog

%description
Xdialog is designed to be a drop in replacement for the cdialog program.
It converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and the treeview adds an
extra dimension to the way menus can be displayed.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q


%build

%configure2_5x --with-gtk2

%make

%install

%makeinstall

%{find_lang} %{name}

%clean
rm -fr %buildroot

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING samples
%doc doc/*.html doc/*.png
%_mandir/man1/*
%_bindir/*


