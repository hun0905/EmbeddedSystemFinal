# Final
1.首先用 $git clone https://github.com/hun0905/Final.git    將所需的檔案抓下來<br> 
2.輸入$cd Final/final<br> 
3.使用$ sudo mbed compile --source . --source ~/ee2405/mbed-os-build/ -m B_L4S5I_IOT01A -t GCC_ARM -f進行編譯。<br> 
8.將從openmv中的main.py的code寫進openmv。<br> 
4.將車子前方對準直線。<br> 
5.輸入$cd Final/Python_PRC<br> 
6.輸入$sudo python3 car_control.py /dev/ttyUSB0<br> 
7.接著可以透過Xbee開始操控車子，當直線在前方附近時按下D會進入demo。<br> 
8.在此模式下車子會沿著直線前進，然後如果前方有標上Apriltag的障礙物就會直行閃避<br> 
9.再繞過障礙物之後會繼續尋找另一條直線，如果前方沒有直線的話，那就會停止，如果繼續進行此模式。<br>

這次我修改了
