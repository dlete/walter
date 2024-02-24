### activiti-app
* username/password: admin/test


### activiti-admin
* username/password: admin/admin


### activiti-rest
* [Activiti User Guide, REST API](https://www.activiti.org/userguide/#_rest_api)
* Make resquests
** Chrome, to see apps installed: `chrome://apps` in Chrome browser 
** Install Postman or Advanced REST Client
** username/password: kermit/kermit
** http://192.168.56.101:8080/activiti-rest/service/repository/deployments

### Get Help
* https://community.alfresco.com/

### Glossary
* Process. End to end.
* Business Process Construct. The minimum unit of reference by which a Process is built on. 


# Tomcat
### How to install in Ubuntu
https://help.ubuntu.com/lts/serverguide/tomcat.html
* edit `/etc/tomcat8/tomcat-users.xml` to include the admin user

### How to deploy an app, a .war file
* Go to http://<server>:8080/manager
* To deploy file `activiti-app.war` in `/workspace/bpm/software/activiti-6.0.0/wars/`
* In "Context Path (required)", fill with `/activiti-app`
* In "WAR or Directory URL:", fill with `/workspace/bpm/software/activiti-6.0.0/wars/activiti-app.war`

### How to log to activity-app
* Default username/password is admin/test

### How to log to activiti-admin
* Default username/password is: admin/admin
* Reference, 6.5 in: http://docs.alfresco.com/activiti/docs/admin-guide/1.4.0/



root@laurel:/home/heanet# apt-get install tomcat8
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  authbind ca-certificates-java default-jre-headless fontconfig-config fonts-dejavu-core java-common libavahi-client3
  libavahi-common-data libavahi-common3 libcommons-collections3-java libcommons-dbcp-java libcommons-pool-java libcups2
  libecj-java libfontconfig1 libjpeg-turbo8 libjpeg8 liblcms2-2 libnspr4 libnss3 libnss3-nssdb libpcsclite1 libtomcat8-java
  libxi6 libxrender1 libxtst6 openjdk-8-jre-headless tomcat8-common x11-common
Suggested packages:
  default-jre libcommons-collections3-java-doc libcommons-dbcp-java-doc libgeronimo-jta-1.1-spec-java cups-common ecj  ant
  libecj-java-gcj liblcms2-utils pcscd openjdk-8-jre-jamvm libnss-mdns fonts-dejavu-extra fonts-ipafont-gothic
  fonts-ipafont-mincho fonts-wqy-microhei fonts-wqy-zenhei fonts-indic libtcnative-1 tomcat8-admin tomcat8-docs
  tomcat8-examples tomcat8-user
The following NEW packages will be installed:
  authbind ca-certificates-java default-jre-headless fontconfig-config fonts-dejavu-core java-common libavahi-client3
  libavahi-common-data libavahi-common3 libcommons-collections3-java libcommons-dbcp-java libcommons-pool-java libcups2
  libecj-java libfontconfig1 libjpeg-turbo8 libjpeg8 liblcms2-2 libnspr4 libnss3 libnss3-nssdb libpcsclite1 libtomcat8-java
  libxi6 libxrender1 libxtst6 openjdk-8-jre-headless tomcat8 tomcat8-common x11-common
0 upgraded, 30 newly installed, 0 to remove and 0 not upgraded.
Need to get 37.4 MB of archives.
After this operation, 119 MB of additional disk space will be used.
Do you want to continue? [Y/n]


https://help.ubuntu.com/lts/serverguide/tomcat.html

http://laurel.heanet.ie:8080/manager/html
http://laurel.heanet.ie:8080/host-manager/html


libtomcat8-java - Apache Tomcat 8 - Servlet and JSP engine -- core libraries
tomcat8 - Apache Tomcat 8 - Servlet and JSP engine
tomcat8-admin - Apache Tomcat 8 - Servlet and JSP engine -- admin web applications
http://laurel.heanet.ie:8080/manager/html
http://laurel.heanet.ie:8080/host-manager/html
"install_activity.md" 60L, 3106C                                     
