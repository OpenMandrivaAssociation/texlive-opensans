Name:		texlive-opensans
Version:	54512
Release:	2
Summary:	The Open Sans font family, and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/opensans
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Open Sans is a humanist sans serif typeface designed by Steve
Matteson; the font is available from the Google Font Directory
as TrueType files licensed under the Apache License version
2.0. The package provides support for this font family in
LaTeX. It includes the original TrueType fonts, as well as Type
1 versions, converted for this package using FontForge for full
support with dvips.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/opensans
%{_texmfdistdir}/fonts/map/dvips/opensans
%{_texmfdistdir}/fonts/tfm/ascender/opensans
%{_texmfdistdir}/fonts/truetype/ascender/opensans
%{_texmfdistdir}/fonts/type1/ascender/opensans
%{_texmfdistdir}/fonts/vf/ascender/opensans
%{_texmfdistdir}/tex/latex/opensans
%doc %{_texmfdistdir}/doc/fonts/opensans

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
