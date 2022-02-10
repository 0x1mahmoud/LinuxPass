# LinuxPass

About The Tool
----------
**LinuxPass** is a a cybersecurity tool mainly doing brute forcing on linux hashes and extract it on **hash.txt** file and after that it brute force the hash file by using JohnTheRipper tool..
**Why?** This tool can automate if you want to get the /etc/passwd file and /etc/shadow file then you doing unshadow to them and then you will crack it so it can be automated...
LinuxPass Tool is written in Python and support all versions

DISCLAIMER
----------

LinuxPass is for penetartion testers and security engineers if they want to extract the password hashes and brute force it to decode and get the password by "TXT"
this tool only work in linux env. **If you have a root Permission (privilge)** You can go with it and this will automate everything by using johntheripper tool.. **NOTE: Don't Use this tool without any permission**

Installing
---------------

### In Ubuntu

```
1. apt-get update
2. python should be installed in linux by default so make sure python is installed
3. sudo apt-get install john -y
```
**running**
`python linuxpass.py`

### Kali Linux

```
1. same in Ubuntu
```
**running**
`python linuxpass.py`

----------------------------------------------------------------------------

## Hope it can help...
@0x1mahmoud
