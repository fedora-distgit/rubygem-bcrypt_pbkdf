# Generated from bcrypt_pbkdf-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bcrypt_pbkdf

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: OpenBSD's bcrypt_pdkfd (a variant of PBKDF2 with bcrypt-based PRF)
# BSD license in files:
#   bcrypt_pbkdf-1.0.0/ext/mri/hash_sha512.c
#   bcrypt_pbkdf-1.0.0/ext/mri/blf.h
#   bcrypt_pbkdf-1.0.0/ext/mri/blowfish.c
# ISC License in file:
#   bcrypt_pbkdf-1.0.0/ext/mri/bcrypt_pbkdf.c
License: MIT and BSD and ISC
URL: https://github.com/net-ssh/bcrypt_pbkdf-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rake-compiler) >= 0.9.7
BuildRequires: rubygem(minitest) >= 5

%description
This gem implements bcrypt_pdkfd (a variant of PBKDF2 with bcrypt-based
PRF).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -Itest:$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/bcrypt_pbkdf.gemspec
%{gem_instdir}/test

%changelog
* Tue Jul 14 2020 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Initial package
