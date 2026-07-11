%global tl_name concmath-otf
%global tl_revision 78172

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.73
Release:	%{tl_revision}.1
Summary:	Concrete based OpenType Math font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/concmath-otf
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an OpenType version of the Concrete Math font
created by Ulrik Vieth in Metafont. "concmath-otf.sty" is a replacement
for the original "concmath.sty" package to be used with LuaTeX or XeTeX
engines.

