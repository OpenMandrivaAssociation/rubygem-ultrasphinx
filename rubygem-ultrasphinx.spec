# Generated from ultrasphinx-1.11.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	ultrasphinx

Summary:	Ruby on Rails configurator and client to the Sphinx fulltext search engine
Name:		rubygem-%{rbname}
Version:	1.11
Release:	4
Group:		Development/Ruby
License:	Academic Free License (AFL) v. 3.0
URL:		http://blog.evanweaver.com/files/doc/fauna/ultrasphinx/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		ultrasphinx-1.11-prefix.patch
BuildRequires:	rubygems >= 1.2
BuildArch:	noarch
Requires:	sphinx

%description
Ruby on Rails configurator and client to the Sphinx fulltext search engine.

%package        doc
Summary:        Documentation for %{name}
Group:          Books/Computer
Requires:       %{name} = %{EVRD}
BuildArch:      noarch

%description    doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .prefix~

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
