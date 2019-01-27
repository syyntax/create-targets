# create-targets
Generate a target list of IP addresses.
## Description
**create-targets** is a python script used to create a list of target IP addresses. This list can be used to configure host firewalls and to determine which hosts will be the targets of passive and interactive activity.

This application is intended for use on Linux systems and is compatible with Python 2.7 and Python 3.
## Download
Open a terminal shell and use git clone to download.
```bash
git clone https://github.com/syyntax/create-targets.git
```
## Installation
Run the **setup.py** script to move **create-targets.py** to the */usr/local/bin* directory and to install the man page.
```bash
sudo python setup.py
```
###### Run Script without setup.py
The script can also be used without running **setup.py**:
```bash
python create-targets.py --help
```
## Options
| Option                        | Description                                                                            |
|-------------------------------|----------------------------------------------------------------------------------------|
| -r, --random                  | Randomly shuffle the target list (default is  *False*).                                |
| -n RANGE, --net RANGE         | Provide a network range with CIDR notation.                                            |
| --ipv6                        | Indicate that the provided network range is IPv6 (default is *IPv4*).                  |
| -x LIST, --exclude LIST       | Exclude a comma-delimited list of IP addresses (no spaces).                            |
| -xl FILE, --exclude-list FILE | Exclude a list of IPs, newline-delimited, provided in a file.                          |
| -o FILE, --output FILE        | Output results to a file.  Default is *targets.list* in the current working directory. |

## Usage
After running **setup.py**, you can run the script by entering **create-targets** from the terminal.
```bash
create-targets --help
```
###### Create a target list
```bash
create-targets -n 192.168.1.0/24
```
###### Create a randomized target list
```bash
create-targets -n 192.168.1.0/24 -r
```
###### Create an IPv6 target list
```bash
create-targets -n ::0/120 --ipv6
```
###### Exclude a comma-delimited list from a target list
```bash
create-targets -n 192.168.1.0/24 -x 192.168.1.1,192.168.1.2,192.168.1.254
```
###### Exclude a list of IP addresses contained in a file
```bash
create-targets -n 192.168.1.0/24 -xl /home/user/Documents/excludes.txt
```
###### Output the results of a target list to a file
```bash
create-targets -n 192.168.1.0/24 -o /tmp/targets.txt
```
## Contact Me
Email me at [syyntax@protonmail.com](mailto:syyntax@protonmail.com) if you find any bugs, have suggestions or feedback, or want any additional information about **create-targets**.
