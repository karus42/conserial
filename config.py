#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
from time import sleep

#--------- UKV config ------------#
SOC="H3"
NUM_CPU=8

SERIAL_PORT="/dev/ttyUSB0"
SERIAL_PORT_SC1="/dev/ttyUSB1"

BOOT_NFS=True
PLATFORM="salvator-x"

FEATBOX=False
PI_IPADDR="192.168.10.11"
PI_NUM="1"

FEATBOX_USB_MODULE=False
FEATBOX_USB2_CH1={'device':'1', 'memory':'port2', 'keyboard':'port1', 'mouse':'port3', 'function':'port4'}
FEATBOX_USB2_CH2={'device':'1', 'memory':'port2', 'keyboard':'port1', 'mouse':'port3', 'function':'port4'}
FEATBOX_USB3={'device':'1','function':'port4'}


IP_ADDR="192.168.10.38"
NET_MASK="255.255.255.0"
DEFAULT_GW="192.168.10.1"

SERVER_ADDR="192.168.10.108"

SER_USRNAME="rvc"
SER_PASS="Pass1234"


PASS_MEG="#### Result: OK ####"
FAIL_MEG="#### Result: NG ####"
SKIP_MEG="#### Result: SKIP ####"

RESTART_IF_FAILED=False
