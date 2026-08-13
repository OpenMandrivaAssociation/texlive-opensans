%global tl_name opensans
%global tl_revision 77682
%global tl_version 2.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The Open Sans font family, and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/opensans
License:	apache2 lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Open Sans is a humanist sans serif typeface designed by Steve Matteson;
the font is available from the Google Font Directory as TrueType files
licensed under the Apache License version 2.0. The package provides
support for this font family in LaTeX. It includes the original TrueType
fonts, as well as Type 1 versions, converted for this package using
FontForge for full support with dvips


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from opensans:
Map opensans.map
TL_DROPIN_EOF
