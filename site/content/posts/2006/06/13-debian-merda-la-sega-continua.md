---
title: DEBIAN MERDA, LA SEGA CONTINUA
date: '2006-06-13T15:14:00+02:00'
url: /2006/06/13/debian-merda-la-sega-continua/
aliases:
- /blog-static/2006/06/13/debian-merda-la-sega-continua/
wp_id: 539
authors:
- asbesto
avatar: asbesto.jpg
categories:
- niente-a-senso
tags: []
---
Installo la quickcam.

`  
modprobe c-qcam  
`

**nessun problema, il modulo viene caricato, la qcam viene vista.**

installo xawtv.

`  
norad:/dev# apt-get install xawtv  
Reading Package Lists... Done  
Building Dependency Tree... Done  
Suggested packages:  
xawtv-plugin-qt tv-fonts  
The following NEW packages will be installed:  
xawtv  
0 upgraded, 1 newly installed, 0 to remove and 12 not upgraded.  
Need to get 0B/241kB of archives.  
After unpacking 754kB of additional disk space will be used.  
Preconfiguring packages ...  
Selecting previously deselected package xawtv.  
(Reading database ... 107736 files and directories currently installed.)  
Unpacking xawtv (from .../archives/xawtv_3.94-1_i386.deb) ...  
Setting up xawtv (3.94-1) ...`

norad:/dev#  


lancio xawtv.

`  
asbesto@norad:~$ xawtv  
This is xawtv-3.94, running on Linux/i686 (2.4.32)  
v4l-conf had some trouble, trying to continue anyway  
no video grabber device available  
asbesto@norad:~$  
`

**non funziona. GRAZIE, CRISTO JAVE’.** Tralascio di mostrarvi le 138 prove fatte (permessi, devices creati e quant’altro) e **NON HO TEMPO COSI’ LEVO LA MERDA DI MEZZO**

`  
norad:~# apt-get remove xawtv  
Reading Package Lists... Done  
Building Dependency Tree... Done  
The following packages will be REMOVED:  
xawtv  
0 upgraded, 0 newly installed, 1 to remove and 12 not upgraded.  
Need to get 0B of archives.  
After unpacking 754kB disk space will be freed.  
Do you want to continue? [Y/n] y  
(Reading database ... 107771 files and directories currently installed.)  
Removing xawtv ...  
norad:~#  
`

bene. **ORA PERO’ SONO CURIOSO e vado a FARMI UN GIRO NEL FILESYSTEM**

`  
norad:/dev# v /usr/share/xawtv/  
total 112  
drwxr-xr-x 2 root root 4096 Jun 13 03:13 .  
drwxr-xr-x 224 root root 4096 Jun 13 03:13 ..  
-rw-r--r-- 1 root root 792 Aug 18 2004 Index.map  
-rw-r--r-- 1 root root 1948 Aug 18 2004 argentina.list  
-rw-r--r-- 1 root root 441 Aug 18 2004 ccir-h.list  
(...)`

norad:/dev# rm -r /usr/lib/xawtv/  
bilinear.so drv1-v4l.so linear-blend.so write-avi.so  
conv-mjpeg.so flt-disor.so linedoubler.so write-dv.so  
cubic.so flt-gamma.so read-avi.so  
drv0-v4l2-old.so flt-invert.so read-dv.so  
drv0-v4l2.so flt-smooth.so snd-oss.so  


**CHE BELLA DEBIAN, MA QUANT’E’ PULITA DEBIAN**

![merda.gif](/wp-content/upload/2006/06/merda.gif)
