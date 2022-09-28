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

> 這次我主要的內容是寫在bbcar_rpc.cpp，我自己多加上了Line, Apriltag, Demo等RPC function，Line主要的功能是偵測直線的位置，然後<br>
沿著直線走，Apriltag主要的功能是偵測Apriltag然後朝Apriltag的方向前進，Demo則是最主要用來Demo的function，裡面可能同時讀取<br>
Apriltag和line的訊息知道Apriltag和line所在的大概方位和距離，然後看到直線就是沿著現走，而看到帶有Apriltag的物體會將其視為障礙物<br>
並搶繞開，我是透過Xbee來下令執行這些RPC fucnction除了Demo的function外其他function主要是一次一個狀態，而執行完就會結束，但demo<br>
則是一次性帶有多種動作，而且會不斷的偵測並執行，因此可以多次繞過障礙物並且繼續偵測新的直線的方位。
