
## Network Scanner 🌐

Network Scanner is a simple ARP scanner which can be used to scan for live hosts in a network. It basically returns the MAC address and IP address of the devices of the same network. It can scan for multiple subnets also. It simply produces the output in a List format. This can be used in the first phases of a pentest where you have access to a network.


## Usage 🚀
#### Clone the github repository and change the directory
```bash
$ git clone https://github.com/okieLoki/Network-Scanner
$ cd Network-Scanner
```
#### Run python3 to executive the file
```bash
$ python3 network_scanner.py -t (target ip)
```
```bash
$ python3 network_scanner.py --target (target ip)
```

You can also scan subnets using the same command.
To know more about subnets visit this [link](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/)

#### To get help about the commands use the help command
```bash
$ python3 network_scanner.py -h
```
```bash
$ python3 network_scanner.py -help
```

## Gathering MAC and IP addresses

If we are connected on IP Address: 192.168.20.230 and the Route IP is: 192.168.20.1 and our Subnet mask is 255.255.255.0 then the 0 simply means that that block 1-254 is available to the client, while the rest of the blocks are available to the host.

Now keep that in mind and look at this image below:

[sub-net table](images/subnet.png)

As you can see the Mask length for the 255.255.255.0 is 24, you can calculate this yourself by converting the Subnet Mask into binary and then counting all the ones. Example: 255.255.255.0 into binary: 1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 So the number of ones are 24.

(Note: You can find out your mask length by typing `ifconfig` on your linux terminal or `ipconfig` on your windows terminal.) 

Your can now specify your target subnet by using `--target 192.168.20.20/24` or `-t 192.168.20.20/24`. For your case the number might not be 24, please check it using the above steps.

## Screenshots 📸

![](images/image.jpeg)


## Python Libraries used 📚

- scapy
- optscanner

