#!/usr/bin/env python

#Helps to run system commands
import subprocess

#Helps to deal with arguements passed after python script (like --interface)
import optparse

#Regex Library
import re


def change_mac(interface,new_mac):
	print(f"[+] Changing MAC address for {interface} to {new_mac}")
	#Process to change mac address 
	subprocess.call(['sudo','ifconfig',interface,'down'])
	subprocess.call(['sudo','ifconfig',interface,'hw','ether',new_mac])
	subprocess.call(['sudo','ifconfig',interface,'up'])

def get_arguements():
	#Creating object 
	parser = optparse.OptionParser()
	#Adding arguements
	parser.add_option('-i','--interface',dest='interface',help='Interface to change MAC address')
	parser.add_option('-m','--mac',dest='new_mac',help='New MAC address')

	#Returns two values (arguements--interface,values--value of interface)
	(options,arguements) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info")
	elif not options.new_mac:
		parser.error("[-] Please specify a new_mac, use --help for more info")	
	
	return options


def get_current_mac(interface):
	''' Getting the current mac'''
	#Check_output helps to return output from the command provided
	ifconfig_result = str(subprocess.check_output(['ifconfig',interface]))
	mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result)
	
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Could not read MAC address")
 

options = get_arguements()

current_mac = get_current_mac(options.interface)
print(f"Current MAC = {current_mac}")

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
	print(f"[+] MAC address was successfully changed to {current_mac}")
else:
	print("[-] MAC address did not get changed.") 
