clear
sleep 1.0
cd $PREFIX/bin
rm -rf main.py
rm -rf CircLe
cd $HOME/Bomber
mv CircLe main.py /data/data/com.termux/files/usr/bin
cd /data/data/com.termux/files/usr/bin
chmod +x CircLe main.py
cd $HOME/Bomber
clear
sleep 1.0
echo -e "\033[1;94m   Now Type: CircLe"
rm -rf setup.sh
