@echo off
cd progfiles
del rapperlist.txt
del raps.txt
del wordlist.txt
echo. 2>rapperlist.txt
echo. 2>raps.txt
echo. 2>wordlist.txt
cd ..
for /f %f in ("dur /b sampleraps") do rapconverter.py %%f
