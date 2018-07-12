#! /data/data/com.termux/files/usr/bin/bash
clear

blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
sleep 1
figlet "Tools"
echo ""

echo "\033[31;1m#######################################"
echo "author = Mr_MuX/'02 feat Phr3ak3r'z_Id10ts404
echo "#######################################"
echo "\033[37;1m Suport by:AKATSUKI ATTACKER ID"
echo "#######################################"
echo "\033[31;1contact:kapan-kapan.com
echo "\033[37;1m#######################################"
echo ""
echo "\033[34;1m[1Install LITETOOLS"
echo "\033[34;1m[2 Install LITESPAM"
echo "\033[34;1m [0 exit"
echo -e $white"" 
read -p "pilih salah satu#%>" act; 
echo -e $cyan

if [ $act = 1 ] || [ $act = 01 ]
then
clear
echo -e $green" Installing LITETOOLS "
sleep 1
pkg update & pkg upgrade
pkg install git
git clone https://github.com/4L13199/LITETOOLS
echo -e $green "Install Done"
cd LITETOOLS
chmod +x LITETOOLS.isl
sh LITETOOLS.isl
fi

if [ $act = 2 ] || [ $act = 02 ]
then
clear
echo -e $green" Installing LITESPAM "
sleep 1
pkg update && pkg upgrade
pkg install php
pkg install git
pkg install toilet
git clone https://github.com/4L13199/LITESPAM
echo -e $green "Done Install"
cd LITESPAM
sh LITESPAM.sh
fi

if [ $act = exit ]
then
echo -e $blue" Thanks all"
sleep 1
echo -e $green" Selamat menikmati"
sleep 1
echo -e $green" Stop nonton bf ya"
sleep 1
echo -e $green" Loading...."
sleep 1
echo -e $red" Thanks For Use Tools Me "
sleep 1
echo -e $cyan
figlet -f smslant "Mr MuX/'02"
sleep 1
exit
fi
