Name:		texlive-concmath-otf
Version:	70294
Release:	1
Summary:	Concrete based OpenType Math font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/concmath-otf
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concmath-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an OpenType version of the Concrete Math
font created by Ulrik Vieth in Metafont. "concmath-otf.sty" is
a replacement for the original "concmath.sty" package to be
used with LuaTeX or XeTeX engines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/concmath-otf
%{_texmfdistdir}/fonts/opentype/public/concmath-otf
%doc %{_texmfdistdir}/doc/fonts/concmath-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
