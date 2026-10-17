---
title: Le dipendenze red hat
date: '2005-10-28T14:37:00+02:00'
url: /2005/10/28/le-dipendenze-red-hat/
aliases:
- /blog-static/2005/10/28/le-dipendenze-red-hat/
wp_id: 181
authors:
- nightolo
avatar: nightolo.jpg
categories:
- niente-a-senso
tags: []
---
Senza Parole

—  
[root@linux11 openldap]# /usr/local/libexec/slapd -d1 -f /usr/local/etc/openldap/slapd.conf  
@(#) $OpenLDAP: slapd 2.2.29 (Oct 27 2005 17:09:22) $  
root@linux11:/usr/local/src/openldap-2.2.29/servers/slapd  
daemon_init: listen on ldap:///  
daemon_init: 1 listeners to open…  
ldap_url_parse_ext(ldap:///)  
daemon: IPv6 socket() failed errno=97 (Address family not supported by protocol)  
daemon: initialized ldap:///  
daemon_init: 2 listeners opened  
slapd init: initiated server.  
slap_sasl_init: SASL library version mismatch: expected 2.1.21, got 2.1.10  
slapd shutdown: freeing system resources.  
slapd stopped.  
connections_destroy: nothing to destroy.  
[root@linux11 openldap]# ldconfig -v | grep sasl  
libkdesasl.so.1 -> libkdesasl.so.1.1.0  
libsasl2.so.2 -> libsasl2.so.2.0.10  
libsasl.so.7 -> libsasl.so.7.1.11  
libsasl2.so.2 -> libsasl2.so.2.0.21  
[root@linux11 openldap]# rpm -qa | grep sasl  
cyrus-sasl-md5-2.1.10-4  
cyrus-sasl-gssapi-2.1.10-4  
cyrus-sasl-2.1.10-4  
cyrus-sasl-plain-2.1.10-4  
cyrus-sasl-devel-2.1.10-4  
[root@linux11 openldap]# rpm -e cyrus-sasl-2.1.10-4  
error: Failed dependencies:  
libsasl.so.7 is needed by (installed) openldap-2.0.27-8  
libsasl.so.7 is needed by (installed) sendmail-8.12.8-9.90  
libsasl.so.7 is needed by (installed) squid-2.5.STABLE1-2  
libsasl.so.7 is needed by (installed) cyrus-sasl-devel-2.1.10-4  
libsasl.so.7 is needed by (installed) openldap-clients-2.0.27-8  
libsasl.so.7 is needed by (installed) mutt-1.4.1-1  
libsasl2.so.2 is needed by (installed) cyrus-sasl-devel-2.1.10-4  
cyrus-sasl = 2.1.10-4 is needed by (installed) cyrus-sasl-md5-2.1.10-4  
cyrus-sasl is needed by (installed) openldap-2.0.27-8  
cyrus-sasl = 2.1.10-4 is needed by (installed) cyrus-sasl-plain-2.1.10-4  
cyrus-sasl = 2.1.10-4 is needed by (installed) cyrus-sasl-devel-2.1.10-4  
cyrus-sasl = 2.1.10-4 is needed by (installed) cyrus-sasl-gssapi-2.1.10-4  
[root@linux11 openldap]# rpm -e cyrus-sasl-2.1.10-4 cyrus-sasl-md5-2.1.10-4 cyrus-sasl-plain-2.1.10-4 cyrus-sasl-devel-2.1.10-4 cyrus-sasl-gssapi-2.1.10-4  
error: Failed dependencies:  
libsasl.so.7 is needed by (installed) openldap-2.0.27-8  
libsasl.so.7 is needed by (installed) sendmail-8.12.8-9.90  
libsasl.so.7 is needed by (installed) squid-2.5.STABLE1-2  
libsasl.so.7 is needed by (installed) openldap-clients-2.0.27-8  
libsasl.so.7 is needed by (installed) mutt-1.4.1-1  
cyrus-sasl is needed by (installed) openldap-2.0.27-8  
cyrus-sasl-md5 is needed by (installed) openldap-2.0.27-8  
[root@linux11 openldap]# rpm -e cyrus-sasl-2.1.10-4 cyrus-sasl-md5-2.1.10-4 cyrus-sasl-plain-2.1.10-4 cyrus-sasl-devel-2.1.10-4 cyrus-sasl-gssapi-2.1.10-4 openldap-2.0.27-8 openldap-2.0.27-8 mutt-1.4.1-1 openldap-clients-2.0.27-8 squid-2.5.STABLE1-2 sendmail-8.12.8-9.90  
error: Failed dependencies:  
liblber.so.2 is needed by (installed) libuser-0.51.7-1  
liblber.so.2 is needed by (installed) autofs-3.1.7-36  
liblber.so.2 is needed by (installed) nss_ldap-202-5  
liblber.so.2 is needed by (installed) php-ldap-4.2.2-17.2  
liblber.so.2 is needed by (installed) evolution-1.2.2-5  
liblber.so.2 is needed by (installed) balsa-2.0.6-2  
liblber.so.2 is needed by (installed) pine-4.44-19.90.0  
liblber.so.2 is needed by (installed) gnomemeeting-0.96.0-4  
liblber.so.2 is needed by (installed) kdelibs-3.1-12  
liblber.so.2 is needed by (installed) kdebase-3.1-15  
libldap.so.2 is needed by (installed) libuser-0.51.7-1  
libldap.so.2 is needed by (installed) autofs-3.1.7-36  
libldap.so.2 is needed by (installed) nss_ldap-202-5  
libldap.so.2 is needed by (installed) gnupg-1.2.1-4  
libldap.so.2 is needed by (installed) php-ldap-4.2.2-17.2  
libldap.so.2 is needed by (installed) evolution-1.2.2-5  
libldap.so.2 is needed by (installed) am-utils-6.0.9-2  
libldap.so.2 is needed by (installed) balsa-2.0.6-2  
libldap.so.2 is needed by (installed) pine-4.44-19.90.0  
libldap.so.2 is needed by (installed) gnomemeeting-0.96.0-4  
libldap.so.2 is needed by (installed) kdelibs-3.1-12  
libldap.so.2 is needed by (installed) kdebase-3.1-15  
libldap.so.2 is needed by (installed) xemacs-21.4.12-6  
openldap = 2.0.27-8 is needed by (installed) openldap-devel-2.0.27-8  
openldap is needed by (installed) xemacs-21.4.12-6  
/usr/bin/newaliases is needed by (installed) mailman-2.1.1-4  
/usr/sbin/sendmail is needed by (installed) redhat-lsb-1.3-1  
/usr/sbin/sendmail is needed by (installed) squirrelmail-1.2.11-1  
smtpdaemon is needed by (installed) fetchmail-6.2.0-3  
smtpdaemon is needed by (installed) diskcheck-1.4-2  
[root@linux11 openldap]# rpm -e cyrus-sasl-2.1.10-4 cyrus-sasl-md5-2.1.10-4 cyrus-sasl-plain-2.1.10-4 cyrus-sasl-devel-2.1.10-4 cyrus-sasl-gssapi-2.1.10-4 openldap-2.0.27-8 openldap-2.0.27-8 mutt-1.4.1-1 openldap-clients-2.0.27-8 squid-2.5.STABLE1-2 sendmail-8.12.8-9.90 mailman-2.1.1-4 redhat-lsb-1.3-1 squirrelmail-1.2.11-1 fetchmail-6.2.0-3 diskcheck-1.4-2  
error: Failed dependencies:  
liblber.so.2 is needed by (installed) libuser-0.51.7-1  
liblber.so.2 is needed by (installed) autofs-3.1.7-36  
liblber.so.2 is needed by (installed) nss_ldap-202-5  
liblber.so.2 is needed by (installed) php-ldap-4.2.2-17.2  
liblber.so.2 is needed by (installed) evolution-1.2.2-5  
liblber.so.2 is needed by (installed) balsa-2.0.6-2  
liblber.so.2 is needed by (installed) pine-4.44-19.90.0  
liblber.so.2 is needed by (installed) gnomemeeting-0.96.0-4  
liblber.so.2 is needed by (installed) kdelibs-3.1-12  
liblber.so.2 is needed by (installed) kdebase-3.1-15  
libldap.so.2 is needed by (installed) libuser-0.51.7-1  
libldap.so.2 is needed by (installed) autofs-3.1.7-36  
libldap.so.2 is needed by (installed) nss_ldap-202-5  
libldap.so.2 is needed by (installed) gnupg-1.2.1-4  
libldap.so.2 is needed by (installed) php-ldap-4.2.2-17.2  
libldap.so.2 is needed by (installed) evolution-1.2.2-5  
libldap.so.2 is needed by (installed) am-utils-6.0.9-2  
libldap.so.2 is needed by (installed) balsa-2.0.6-2  
libldap.so.2 is needed by (installed) pine-4.44-19.90.0  
libldap.so.2 is needed by (installed) gnomemeeting-0.96.0-4  
libldap.so.2 is needed by (installed) kdelibs-3.1-12  
libldap.so.2 is needed by (installed) kdebase-3.1-15  
libldap.so.2 is needed by (installed) xemacs-21.4.12-6  
openldap = 2.0.27-8 is needed by (installed) openldap-devel-2.0.27-8  
openldap is needed by (installed) xemacs-21.4.12-6  
[root@linux11 openldap]# rpm -e –no-deps cyrus-sasl-2.1.10-4 cyrus-sasl-md5-2.1.10-4 cyrus-sasl-plain-2.1.10-4 cyrus-sasl-devel-2.1.10-4 cyrus-sasl-gssapi-2.1.10-4 openldap-2.0.27-8 openldap-2.0.27-8 mutt-1.4.1-1 openldap-clients-2.0.27-8 squid-2.5.STABLE1-2 sendmail-8.12.8-9.90 mailman-2.1.1-4 redhat-lsb-1.3-1 squirrelmail-1.2.11-1 fetchmail-6.2.0-3 diskcheck-1.4-2 openldap-devel-2.0.27-8 xemacs-21.4.12-6  
–no-deps: unknown option  
[root@linux11 openldap]# rpm -e –nodeps cyrus-sasl-2.1.10-4 cyrus-sasl-md5-2.1.10-4 cyrus-sasl-plain-2.1.10-4 cyrus-sasl-devel-2.1.10-4 cyrus-sasl-gssapi-2.1.10-4 openldap-2.0.27-8 openldap-2.0.27-8 mutt-1.4.1-1 openldap-clients-2.0.27-8 squid-2.5.STABLE1-2 sendmail-8.12.8-9.90 mailman-2.1.1-4 redhat-lsb-1.3-1 squirrelmail-1.2.11-1 fetchmail-6.2.0-3 diskcheck-1.4-2 openldap-devel-2.0.27-8 xemacs-21.4.12-6  
warning: /etc/mail/submit.cf saved as /etc/mail/submit.cf.rpmsave  
warning: /etc/mail/statistics saved as /etc/mail/statistics.rpmsave  
warning: /etc/openldap/ldap.conf saved as /etc/openldap/ldap.conf.rpmsave  
[root@linux11 openldap]# ^D  
localhost:~ night$
