import pyb, sensor, image, time, math

enable_lens_corr = False # turn on for straighter lines...
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()

f_x = (2.8 / 3.984) * 160 # find_apriltags defaults to this if not set
f_y = (2.8 / 2.952) * 120 # find_apriltags defaults to this if not set
c_x = 160 * 0.5 # find_apriltags defaults to this if not set (the image.w * 0.5)
c_y = 120 * 0.5 # find_apriltags defaults to this if not set (the image.h * 0.5)

def degrees(radians):
   return (180 * radians) / math.pi

# All lines also have `x1()`, `y1()`, `x2()`, and `y2()` methods to get their end-points
# and a `line()` method to get all the above as one 4 value tuple for `draw_line()`.
uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)
while(True):
   clock.tick()
   # for 2.8mm lens...

   # `merge_distance` controls the merging of nearby lines. At 0 (the default), no
   # merging is done. At 1, any line 1 pixel away from another is merged... and so
   # on as you increase this value. You may wish to merge lines as line segment
   # detection produces a lot of line segment results.

   # `max_theta_diff` controls the maximum amount of rotation difference between
   # any two lines about to be merged. The default setting allows for 15 degrees.           10,15,
   img = sensor.snapshot()
   if enable_lens_corr: img.lens_corr(1.8)
   for l in img.find_line_segments(merge_distance = 20, max_theta_diff = 15):
      #if l[1] < 20 and l[3] < 40 and ((int(l[6])<60 or int(l[6])>120)) and l[0]< 120 and l[0]>40:
      if l.x1() > 40 and l.x1() < 120 and l.y1() < 3 and l.magnitude() > 5 and l.length() > 5 and ((int(l[6])<60 or int(l[6])>120)):
          if l[0]<60 and l[6]<90:
            print_args = ('r')
          elif l[6]>90 and l[0] >60:
            print_args = ('l')
          else:
            print_args = ('s')
          uart.write(("%c" % print_args).encode())
          time.sleep_ms(500)
          img.draw_line(l.line(), color = (255, 0, 0))
          #print(("%c" % print_args).encode())
          #uart.write(("%c" % print_args).encode())

   img = sensor.snapshot()
   for tag in img.find_apriltags(fx=f_x, fy=f_y, cx=c_x, cy=c_y): # defaults to TAG36H11
      img.draw_rectangle(tag.rect(), color = (255, 0, 0))
      img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
      # The conversion is nearly 6.2cm to 1 -> translation
      print_args = (tag.x_translation(), tag.y_translation(), tag.z_translation(), \
            degrees(tag.x_rotation()), degrees(tag.y_rotation()), degrees(tag.z_rotation()))
      if tag.x_translation()>1:
        print_args = ('l')
        uart.write(("%c" % print_args).encode())
        #print(("%c" % print_args).encode())
        time.sleep_ms(500)
      if tag.x_translation()<-1:
        print_args = ('r')
        uart.write(("%c" % print_args).encode())
        #print(("%c" % print_args).encode())
        time.sleep_ms(500)
      #print(("%c" % print_args).encode())
      print(tag.z_translation())
      if tag.z_translation() > -6:
        print_args = ('c')
        uart.write(("%c" % print_args).encode())
        #print(("%c" % print_args).encode())
        time.sleep_ms(9000)
      '''else:
        print_args = ('a')
        uart.write(("%c" % print_args).encode())
        print(("%c" % print_args).encode())
        time.sleep_ms(500)'''
        #print(("%c" % print_args).encode())
        # Translation units are unknown. Rotation units are in degrees.
        #uart.write(("Tx: %f, Ty %f, Tz %f, Rx %f, Ry %f, Rz %f" % print_args).encode())
      #uart.write(("FPS %f\r\n" % clock.fps()).encode())


   #print_args = ('n')
   #print("FPS %f" % clock.fps())