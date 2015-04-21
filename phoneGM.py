
# #####################################################
# Phone sim for Grand Marais museum
#
# Keypad-reading library written by Chris Crumpacker
# May 2013
# http://crumpspot.blogspot.com/2013/05/using-3x4-matrix-keypad-with-raspberry.html
#
# main structure is adapted from Bandono's
# matrixQPI which is wiringPi based.
# https://github.com/bandono/matrixQPi?source=cc
# #####################################################
 
import RPi.GPIO as GPIO
import time
import subprocess
 
class keypad():
    # CONSTANTS   
    KEYPAD = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
    ]
     
    ROW         = [18,23,24,25]
    COLUMN      = [4,17,22]
     
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
     
    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal < 0 or colVal > 2:
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]
         
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

if __name__ == '__main__':
    # Initialize the keypad class
    kp = keypad()

	# Loop while waiting for a keypress
    while True:
	digit = None
	while digit == None:
		digit = kp.getKey()

	#Print the digit
	print digit

	#if statements
	if (digit == 0):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_0_Operator.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 1):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_1_Ice_House.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 2):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_2_Fish_Man.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 3):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_3_Berry_Delivery.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 4):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_4_Firewood_Delivery.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 5):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_5_Honeywagon.mp3", shell=True)
		time.sleep(0.5)
	elif (digit == 6):
		subprocess.call("mpg123 /home/pi/GMH/GrandMaraisHeritage_6_Joe_The_Handyman.mp3", shell=True)
		time.sleep(0.5)
	#elif (digit == 7):
		#subprocess.call("mpg123 /home/pi/GMH/", shell=True)
		time.sleep(0.5)
	#elif (digit == 8):
		#subprocess.call("mpg123 /home/pi/GMH/", shell=True)
		#time.sleep(0.5)
	#elif (digit == "9"):
		#subprocess.call("mpg123 /home/pi/GMH/", shell=True)
		time.sleep(0.5)
	
	time.sleep(0.5)
