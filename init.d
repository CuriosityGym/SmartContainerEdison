#!/bin/sh
wpa_supplicant -B -Dnl80211 -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf

busybox udhcpc -i wlan0

python /home/root/mqtt.py
