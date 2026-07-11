%global tl_name chet
%global tl_revision 78825

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3a
Release:	%{tl_revision}.1
Summary:	LaTeX layout inspired by harvmac
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chet
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package aims to streamline the work of typesetting, and to provide
the look and feel of harvmac for readers. The package name stands for
"Class for High Energy Theory", as the majority of individuals using
harvmac for their papers were primarily working in high energy theory, a
subfield of theoretical physics.

