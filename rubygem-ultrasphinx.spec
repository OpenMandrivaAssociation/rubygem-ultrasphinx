# Generated from ultrasphinx-1.11.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	ultrasphinx

Summary:	Ruby on Rails configurator and client to the Sphinx fulltext search engine
Name:		rubygem-%{rbname}
Version:	1.11
Release:	5
Group:		Development/Ruby
License:	Academic Free License (AFL) v. 3.0
URL:		http://blog.evanweaver.com/files/doc/fauna/ultrasphinx/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		ultrasphinx-1.11-prefix.patch
Patch1:		ultrasphinx-1.11-test-dispatch-env-shebang.patch
BuildRequires:	rubygems >= 1.2
BuildArch:	noarch
Requires:	sphinx

%description
Ruby on Rails configurator and client to the Sphinx fulltext search engine.

%package        doc
Summary:        Documentation for %{name}
Group:          Books/Computer books
Requires:       %{name} = %{EVRD}
BuildArch:      noarch

%description    doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .prefix~
%patch1 -p1 -b .shebang~

%build
%gem_build -f '(.*.rb|Rakefile|tasks|vendor)'

%install
rm -rf %{buildroot}

%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/Rakefile
%{ruby_gemdir}/gems/%{rbname}-%{version}/init.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/vendor
%{ruby_gemdir}/gems/%{rbname}-%{version}/vendor/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/DEPLOYMENT_NOTES
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/RAKE_TASKS
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/TODO
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11-4
+ Revision: 643273
- use absolute path to /usr/sbin/sphinx-searchd
- ship docs in a separate subpackage
- use gem2rpm5 layout..

* Sun Sep 19 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11-3mdv2011.0
+ Revision: 579883
- fix path to indexer & searchd
- add dependency on sphinx

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11-2mdv2011.0
+ Revision: 579744
- fix license
- rebuild for new auto requires/provides
- don't ship gem archive

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11-1mdv2010.1
+ Revision: 500501
- fix summary-ended-with-dot
- import rubygem-ultrasphinx


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11-1
- initial release
