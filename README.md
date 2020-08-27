# python-nmap-test
Simple code to test some functions

## Installation
Install python3-nmap as described here https://pypi.org/project/python3-nmap/  

Install other dependencies:  
```
pip3 install -r requirements.txt
```

## Usage:  
```
python3 pingsweep.py -i eth0 | python3 portscan.py -p21,22,80
python3 pingsweep.py -I 10.10.1.0/24 | python3 portscan.py -p21,22,80
```

```
python3 pingsweep.py | tee ips.txt
python3 portscan.py -p21,22,80 -f ips.txt
```
