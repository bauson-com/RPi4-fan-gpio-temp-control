#/bin/bash
sudo rm /rpi-fan -fr || true
sudo mkdir /rpi-fan
sudo chmod 777 /rpi-fan -R
cp -f fan.py /rpi-fan/
echo "OFF" > /rpi-fan/status.txt
crontab -l | grep -q '/rpi-fan/fan.py'  && echo 'Fan Control exists.' || (crontab -l ; echo "*/5 * * * * /usr/bin/python /rpi-fan/fan.py") | crontab
crontab -l