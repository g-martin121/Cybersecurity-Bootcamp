#1/bin/bash
#print user info and check file
name="GiaVonna Martin"
echo "Hello, $name!"
if [ -f /var/log/syslog ]; then
    echo "Syslog found!"
else
    echo "Syslog missing!"
fi 
