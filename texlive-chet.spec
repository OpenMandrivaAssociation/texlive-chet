# revision 24432
# category Package
# catalog-ctan /macros/latex/contrib/chet
# catalog-date 2011-10-28 19:36:13 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-chet
Version:	1.3
Release:	1
Summary:	LaTeX class inspired by harvmac
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is designed to streamline the work of typesetting,
and to provide the look and feel of harvmac for readers.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chet/chet.sty
%doc %{_texmfdistdir}/doc/latex/chet/README
%doc %{_texmfdistdir}/doc/latex/chet/chetdoc.pdf
%doc %{_texmfdistdir}/doc/latex/chet/chetdoc.tex
%doc %{_texmfdistdir}/doc/latex/chet/chetmacros.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
