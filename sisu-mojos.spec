%_javapackages_macros
Name:           sisu-mojos
Version:        0.1.0
Release:        2%{?dist}
Summary:        Sisu plugin for Apache Maven
License:        EPL
URL:            http://www.eclipse.org/sisu
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/sisu/org.eclipse.sisu.mojos.git/snapshot/releases/%{version}.tar.bz2#/%{name}-%{version}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.sonatype.oss:oss-parent)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice)

Obsoletes:      sisu-maven-plugin < 1:0.1

%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -c
mv releases/%{version}/* .
# Animal Sniffer is not useful in Fedora
%pom_remove_plugin :animal-sniffer-maven-plugin
%mvn_alias : org.sonatype.plugins:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt
