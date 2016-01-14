%global pkg_name ws-commons-util
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0.1
Release:        29.12%{?dist}
Summary:        Common utilities from the Apache Web Services Project

License:        ASL 2.0
URL:            http://apache.osuosl.org/ws/commons/util/
Source0:        http://apache.osuosl.org/ws/commons/util/sources/ws-commons-util-1.0.1-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-source-plugin
BuildRequires:  %{?scl_prefix_maven}maven-assembly-plugin
BuildRequires:  %{?scl_prefix_maven}maven-resources-plugin

%description
This is version 1.0.1 of the common utilities from the Apache Web
Services Project.

%package        javadoc
Summary:        Javadoc for %{pkg_name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x

# add OSGI manifest
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . '
       <configuration>
           <archive>
               <manifestEntries>
                   <Bundle-ManifestVersion>2</Bundle-ManifestVersion>
                   <Bundle-Name>%Bundle-Name</Bundle-Name>
                   <Bundle-Localization>plugin</Bundle-Localization>
                   <Bundle-SymbolicName>org.apache.ws.commons.util</Bundle-SymbolicName>
                   <Bundle-Version>1.0.1</Bundle-Version>
                   <Export-Package>org.apache.ws.commons.serialize;version="1.0.1", org.apache.ws.commons.util;version="1.0.1"</Export-Package>
                   <Import-Package>javax.xml, javax.xml.namespace, org.w3c.dom, org.xml.sax, org.xml.sax.ext, org.xml.sax.helpers</Import-Package>
                   <Bundle-RequiredExecutionEnvironment>J2SE-1.4, CDC-1.0/Foundation-1.0, J2SE-1.3</Bundle-RequiredExecutionEnvironment>
               </manifestEntries>
           </archive>
       </configuration>
'

# Remove maven-eclipse-plugin from build dependencies to simplify the
# dependency chain.
%pom_remove_plugin :maven-eclipse-plugin

%mvn_file : %{pkg_name}
%mvn_alias : org.apache.ws.commons.util:%{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-29.12
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.0.1-29.11
- Rebuild to regenerate requires

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1.0.1-29.10
- Mass rebuild 2015-01-09

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.9
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.8
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.7
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0.1-29.3
- SCL-ize BR/R
- Remove BR on java-javadoc

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-29.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-29
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> 1.0.1-28
- Migrate away from mvn-rpmbuild (#997459)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-27
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Sun Mar 03 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0.1-26
- Remove superfluous BRs rhbz #915622.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-24
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-22
- Patch pom.xml to remove maven-eclipse-plugin
- Add missing java and jpackage-utils requires

* Tue Apr 17 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-21
- Fix OSGi manifest.
- Adapt to current guidelines.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Andrew Overholt <overholt@redhat.com> 1.0.1-19
- Build with Maven 3.
- Clean up unnecessary lines.
- Remove building with ant.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.1-17
- Versionless jars and javadocs
- Add jpackage-utils Requires to javadoc subpackage
- Add alternative depmap groupId

* Fri Sep 10 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-16
- Use default file attr.
- Use newer maven plugins' names.

* Tue Aug 24 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.1-15
- Install maven depmaps and pom.xml files

* Wed Jan 13 2010 Andrew Overholt <overholt@redhat.com> 1.0.1-14
- Add missing maven-doxia{,-sitetools} BRs.

* Wed Jan 13 2010 Andrew Overholt <overholt@redhat.com> 1.0.1-13
- Add missing maven-surefire-provider-junit BR.
- Remove gcj support
- Add ability to build with ant and not maven

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Andrew Overholt <overholt@redhat.com> 1.0.1-10
- Bump so I can chain-build with xmlrpc3.

* Fri Sep 12 2008 Andrew Overholt <overholt@redhat.com> 1.0.1-9
- Add ppc64.

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-7
- Autorebuild for GCC 4.3

* Thu Sep 13 2007 Andrew Overholt <overholt@redhat.com> 1.0.1-6
- Add BR on maven surefire resources, eclipse, and install plugins.

* Thu Sep 13 2007 Andrew Overholt <overholt@redhat.com> 1.0.1-5
- ExcludeArch ppc64 until maven is built on ppc64.

* Thu Sep 13 2007 Andrew Overholt <overholt@redhat.com> 1.0.1-4
- Bump again.

* Thu Sep 13 2007 Andrew Overholt <overholt@redhat.com> 1.0.1-3
- Bump release.

* Thu Sep 06 2007 Andrew Overholt <overholt@redhat.com> 1.0.1-2
- maven-ify.
- Add OSGi MANIFEST information.

* Fri Mar 16 2007 Anthony Green <green@redhat.com> - 1.0.1-1
- Created.
