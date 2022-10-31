Name     : xdg-desktop-portal-wlr
Version  : 0.6.0
Release  : 1
URL      : https://github.com/emersion/xdg-desktop-portal-wlr
Source0  : https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v%{version}/%{name}-%{version}.tar.gz
Summary  : xdg portal backend for wlroots
Group    : Development/Tools
License  : MIT
Requires: pipewire
Requires: dbus
Requires: xdg-desktop-portal
BuildRequires : meson cmake
BuildRequires : dbus-bin
BuildRequires : gettext
BuildRequires : gsettings-desktop-schemas
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libportal)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(inih)


%description
This project seeks to add support for the screenshot, screencast, and possibly
remote-desktop xdg-desktop-portal interfaces for wlroots based compositors.


%prep
%setup -q -n xdg-desktop-portal-wlr-%{version}

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -mprefer-vector-width=256  "
meson \
     --libdir=lib64 --prefix=/usr \
     --buildtype=plain -Dman-pages=disabled builddir
ninja -v -C builddir


%install
DESTDIR=%{buildroot} ninja -C builddir install


%files
%defattr(-,root,root,-)
/usr/libexec/xdg-desktop-portal-wlr
/usr/share/xdg-desktop-portal/portals/wlr.portal
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.wlr.service
/usr/lib/systemd/user/xdg-desktop-portal-wlr.service
