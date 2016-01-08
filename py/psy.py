#!/usr/bin/env python
# System Infomation Gathering

import subprocess

#Command1
def uname_func():

	uname="uname"
	uname_arg="-a"
	print "Gathering system information with %s command:\n" % uname
	subprocess.call([uname, uname_arg])

#Command2
def disk_func():

	diskspace="df"
	diskspace_arg="-hi"
	print "Gathering diskspace information %s command:\n" % diskspace
	subprocess.call([diskspace, diskspace_arg])

#Main function that call other functions
def main():
	uname_func()
	disk_func()

main()
