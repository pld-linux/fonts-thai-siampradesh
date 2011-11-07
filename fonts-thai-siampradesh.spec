Summary:	Thai SiamPradesh scalable fonts
Summary(pl.UTF-8):	Tajskie fonty skalowalne SiamPradesh
Name:		fonts-thai-siampradesh
Version:	0.2.2
Release:	1
License:	Font Computer Program License (see COPYING)
Group:		Fonts
Source0:	http://linux.thai.net/pub/thailinux/software/thaifonts-siampradesh/thaifonts-siampradesh-%{version}.tar.gz
# Source0-md5:	682791e7abc47f4dd35d2bb2e598b154
URL:		http://linux.thai.net/projects/thaifonts-siampradesh
BuildRequires:	fontforge >= 20080110
BuildRequires:	xorg-app-mkfontscale
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is an attempt to adjust fonts from DIP & SIPA contested
fonts for use in GNU/Linux desktops. All fonts are renamed as required
by the license.

%description -l pl.UTF-8
Ten projekt jest próbą dostosowania fontów DIP i SIPA do użytku w
środowiskach graficznych systemów GNU/Linux. Wszystkie fonty mają
nazwy zmienione zgodnie z wymogiem licencji.

%package -n fonts-TTF-thai-siampradesh
Summary:	TrueType Thai SiamPradesh fonts
Summary(pl.UTF-8):	Tajskie fonty SiamPradesh w formacie TrueType
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-TTF-thai-siampradesh
This project is an attempt to adjust fonts from DIP & SIPA contested
fonts for use in GNU/Linux desktops. All fonts are renamed as required
by the license.

This package contains fonts in TrueType format.

%description -n fonts-TTF-thai-siampradesh -l pl.UTF-8
Ten projekt jest próbą dostosowania fontów DIP i SIPA do użytku w
środowiskach graficznych systemów GNU/Linux. Wszystkie fonty mają
nazwy zmienione zgodnie z wymogiem licencji.

Ten pakiet zawiera fonty w formacie TrueType.

%package -n fonts-Type1-thai-siampradesh
Summary:	Type1 Thai SiamPradesh fonts
Summary(pl.UTF-8):	Tajskie fonty SiamPradesh w formacie Type1
Group:		Fonts
Requires(post,postun):	fontpostinst

%description -n fonts-Type1-thai-siampradesh
This project is an attempt to adjust fonts from DIP & SIPA contested
fonts for use in GNU/Linux desktops. All fonts are renamed as required
by the license.

This package contains fonts in Type1 format.

%description -n fonts-Type1-thai-siampradesh -l pl.UTF-8
Ten projekt jest próbą dostosowania fontów DIP i SIPA do użytku w
środowiskach graficznych systemów GNU/Linux. Wszystkie fonty mają
nazwy zmienione zgodnie z wymogiem licencji.

Ten pakiet zawiera fonty w formacie Type1.

%prep
%setup -q -n thaifonts-siampradesh-%{version}

%build
%configure \
	--enable-pfb \
	--with-ttfdir=%{_fontsdir}/TTF \
	--with-type1dir=%{_fontsdir}/Type1
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mv $RPM_BUILD_ROOT%{_fontsdir}/Type1/*.afm $RPM_BUILD_ROOT%{_fontsdir}/Type1/afm
mkfontscale -o $RPM_BUILD_ROOT%{_fontsdir}/Type1/fonts.scale.thai-siampradesh $RPM_BUILD_ROOT%{_fontsdir}/Type1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n fonts-TTF-thai-siampradesh
fontpostinst TTF

%postun	-n fonts-TTF-thai-siampradesh
fontpostinst TTF

%post	-n fonts-Type1-thai-siampradesh
fontpostinst Type1

%postun	-n fonts-Type1-thai-siampradesh
fontpostinst Type1

%files -n fonts-TTF-thai-siampradesh
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/TTF/SPAphaimanee*.ttf
%{_fontsdir}/TTF/SPHanuman*.ttf
%{_fontsdir}/TTF/SPLaksaman*.ttf
%{_fontsdir}/TTF/SPLaweng*.ttf
%{_fontsdir}/TTF/SPRama*.ttf
%{_fontsdir}/TTF/SPSida*.ttf
%{_fontsdir}/TTF/SPSinsamut*.ttf
%{_fontsdir}/TTF/SPSutsakhorn*.ttf
%{_fontsdir}/TTF/SPThotsakan*.ttf
/etc/fonts/conf.avail/64-ttf-thai-siampradesh.conf
/etc/fonts/conf.avail/89-ttf-thai-siampradesh-synthetic.conf

%files -n fonts-Type1-thai-siampradesh
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_fontsdir}/Type1/SPAphaimanee*.pfb
%{_fontsdir}/Type1/SPHanuman*.pfb
%{_fontsdir}/Type1/SPLaksaman*.pfb
%{_fontsdir}/Type1/SPLaweng*.pfb
%{_fontsdir}/Type1/SPRama*.pfb
%{_fontsdir}/Type1/SPSida*.pfb
%{_fontsdir}/Type1/SPSinsamut*.pfb
%{_fontsdir}/Type1/SPSutsakhorn*.pfb
%{_fontsdir}/Type1/SPThotsakan*.pfb
%{_fontsdir}/Type1/fonts.scale.thai-siampradesh
%{_fontsdir}/Type1/afm/SPAphaimanee*.afm
%{_fontsdir}/Type1/afm/SPHanuman*.afm
%{_fontsdir}/Type1/afm/SPLaksaman*.afm
%{_fontsdir}/Type1/afm/SPLaweng*.afm
%{_fontsdir}/Type1/afm/SPRama*.afm
%{_fontsdir}/Type1/afm/SPSida*.afm
%{_fontsdir}/Type1/afm/SPSinsamut*.afm
%{_fontsdir}/Type1/afm/SPSutsakhorn*.afm
%{_fontsdir}/Type1/afm/SPThotsakan*.afm
