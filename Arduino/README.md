Arduino Sketch
--------------

The Arduino sketch here controls the robot (which, in this case, moves with 2
DC motors and an H-Bridge.)

It works via Serial commands, so if you want to make your own interface to it
you can.

_*ANV <analog pin>*_
Sends the analog value (a 10-bit integer, from 0 to 1024) from an analog
pin given. If pin number is too big (0 > pin number > 5) than it will write back
an error message. If your Arduino platform supports more than this number
of analog pins, feel free to modify and re-compile the code.

_*LMS <motor speed>*_
Sets the left motor speed (which its speed-control PWN pin is given
in the global integers section). -255 to 255 number. 
Number < 0 is negative speed -> going backwards
Number = 0 is motor stop break -> motor stops
Number > 0 is positive speed -> motor goes forwards

_*RMS <motor speed>*_
Same like LMS.

_*SMS <left motor speed> <right motor speed>*_

Does the same like LMS and RMS, just in one command.
