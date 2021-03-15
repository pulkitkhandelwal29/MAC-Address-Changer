# MAC Address Changer
<hr>
MAC Address (Media Access Control)

## Characteristics of MAC Address
* Permanent
* Physical 
* Unique
* Assigned by manufacturer

MAC address is used within the network to identify devices and transfer data between devices

## Why change MAC address?
1.Increase anonymity<br>
2.Impersonate other devices (sometimes there is filtering that "this" particular MAC address can only connect to network)<br>
3.Bypass filters

## Changing mac address manually
ifconfig wlan0 down									<br>
ifconfig wlan0 hw ether 00:11:22:33:44:55     (New MAC) <br>
ifconfig wlan0 up <br>

(wlan0 = interface name)
(00:11:22:33:44:55 =New MAC)
