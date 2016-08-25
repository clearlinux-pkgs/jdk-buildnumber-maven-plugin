#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-buildnumber-maven-plugin
Version  : 1.3
Release  : 1
URL      : http://central.maven.org/maven2/org/codehaus/mojo/buildnumber-maven-plugin/1.3/buildnumber-maven-plugin-1.3-source-release.zip
Source0  : http://central.maven.org/maven2/org/codehaus/mojo/buildnumber-maven-plugin/1.3/buildnumber-maven-plugin-1.3-source-release.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: jdk-buildnumber-maven-plugin-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jna
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-jtidy
BuildRequires : jdk-junit4
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-scm
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-mojo-parent
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-qdox
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%package data
Summary: data components for the jdk-buildnumber-maven-plugin package.
Group: Data

%description data
data components for the jdk-buildnumber-maven-plugin package.


%prep
%setup -q -n buildnumber-maven-plugin-1.3

python3 /usr/share/java-utils/pom_editor.py pom_remove_dep com.google.code.maven-scm-provider-svnjava:maven-scm-provider-svnjava
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep org.tmatesoft.svnkit:svnkit
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-enforcer-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-invoker-plugin
python3 /usr/share/java-utils/pom_editor.py pom_add_dep        junit:junit::test

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n buildnumber-maven-plugin-1.3 -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/buildnumber-maven-plugin-1.3/buildnumber-maven-plugin.jar
/usr/share/maven-metadata/buildnumber-maven-plugin-1.3.xml
/usr/share/maven-poms/buildnumber-maven-plugin-1.3/buildnumber-maven-plugin.pom
