Name: fzy
Summary: 🔍 A better fuzzy finder
Version: 0.9
Release: 1%{?dist}
License: MIT
URL: https://github.com/jhawthorn/fzy
Source0: %{version}.tar.gz

%description
fzy is a fast, simple fuzzy text selector for the terminal with an advanced
scoring algorithm.

%prep
%setup -q

%build
%make_build

%check
make test

%install
%make_install

%files
/usr/local/bin/fzy
/usr/local/share/man/man1/fzy.1

%changelog
* Sun Oct 29 2017 Alex Blackie <alexblackie@fedoraproject.org> - 0.9-1
- Initial addition of RPM spec.
