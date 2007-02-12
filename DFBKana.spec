Summary:	DFBKana - learning Japanese kana
Summary(pl.UTF-8):   DFBKana - program do nauki alfabetu japońskiego kana
Name:		DFBKana
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DFBKana/%{name}-%{version}.tar.gz
# Source0-md5:	7c3b9fb91af1c4ad0e58caa5ca08a052
Patch0:		%{name}-update.patch
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= 0.9.18
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DFBKana is a small DirectFB program to help you learning Japanese kana
(hiragana and katakana).

%description -l pl.UTF-8
DFBKana to mały program dla DirectFB pomagający w nauce japońskiego
alfabetu kana (hiragana i katakana).

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/dfbkana
%{_datadir}/dfbkana
