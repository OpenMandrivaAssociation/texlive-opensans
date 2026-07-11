%global tl_name opensans
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	The Open Sans font family, and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/opensans
License:	apache2 lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/opensans.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Open Sans is a humanist sans serif typeface designed by Steve Matteson;
the font is available from the Google Font Directory as TrueType files
licensed under the Apache License version 2.0. The package provides
support for this font family in LaTeX. It includes the original TrueType
fonts, as well as Type 1 versions, converted for this package using
FontForge for full support with dvips

