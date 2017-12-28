#! /usr/bin/python3

# Think Create Learn
#
# ROSI remote control template
# Use a remote control to control a robot

# ======================================================================================================
# Imports
# ======================================================================================================
import rosi_library as robot
from approxeng.input.selectbinder import ControllerResource

import piconzero3 as pz, time




# ======================================================================================================
# Constants
# ======================================================================================================
MOTOR_LEFT = 1
MOTOR_RIGHT = 0

CLOCKWISE = 1
ANTICLOCKWISE = -1

# ======================================================================================================
# Global variables
# ======================================================================================================


# ======================================================================================================
# Functions
# ======================================================================================================


# ======================================================================================================
# Main program
# ======================================================================================================
try:

    # Variable to indicate if we are still running
    running = True

    robot.start()

    pz.init()
    pz.setOutputConfig(0, 1)


    with ControllerResource() as joystick:
        print ("Found joystick")
        while running and joystick.connected:

            presses = joystick.check_presses()
            
            if joystick.presses.start:
                # We want to exit the program                
                running = False
               
            if joystick.presses.triangle:
                # ******** DO SOMETHING HERE ********
                print("triangle")
                pz.setOutput(0,0)
                pz.setMotor(0,0)
                pz.setMotor(1,0)

            if joystick.presses.cross:
                # ******** DO SOMETHING HERE ********
                print("Cross")
                
                           
            if joystick.presses.square:
                # ******** DO SOMETHING HERE ********
                print("square")
                pz.setMotor(0,20)
                pz.setMotor(1,0)
                
            if joystick.presses.circle:
                # ******** DO SOMETHING HERE ********
                print("circle")
                pz.setMotor(0,0)
                pz.setMotor(1,20)
                
                
            if joystick.presses.dleft:
                # ******** DO SOMETHING HERE ********    
                print("D Left")
                pz.setMotor(0,30)
                pz.setMotor(1,-30)

            if joystick.presses.dright:
                # ******** DO SOMETHING HERE ********  
                print("D Right")
                pz.setMotor(0,-30)
                pz.setMotor(1,30)

            if joystick.presses.dup:
                # ******** DO SOMETHING HERE ********  
                print("D Up")
                pz.setOutput(0,100)
                pz.setMotor(0,50)
                pz.setMotor(1,50)
                

            if joystick.presses.ddown:
                # ******** DO SOMETHING HERE ********  
                print("D Down")
                pz.setMotor(0,-50)
                pz.setMotor(1,-50)

            if joystick.presses.l1:
                # ******** DO SOMETHING HERE ********  
                print("l1")
                pz.setMotor(0,30)
                pz.setMotor(1,0)
                time.sleep(0.1)
                pz.setMotor(0,0)
                pz.setMotor(1,0)

            if joystick.presses.l2:
                # ******** DO SOMETHING HERE ********  
                print("l2")
                pz.setMotor(0,0)
                pz.setMotor(1,30)
                time.sleep(0.1)
                pz.setMotor(0,0)
                pz.setMotor(1,0)

            if joystick.presses.r1:
                # ******** DO SOMETHING HERE ********  
                print("r1")

            if joystick.presses.r2:
                # ******** DO SOMETHING HERE ********  
                print("r2")    
                
                
            if joystick.ly:
                # ******** DO SOMETHING HERE ********    
                print("Stick Left Y ", joystick.ly)
                pz.setMotor(0,int(joystick.ly*30))
                pz.setMotor(1,int(joystick.ly*30))

            if joystick.rx:
                # ******** DO SOMETHING HERE ********    
                print("Stick Right X ", joystick.rx)
                pz.setMotor(0,-int(joystick.rx*30))
                pz.setMotor(1,int(joystick.rx*30))


             
                
            # Give the computer a bit of time to rest
            robot.wait(0.1)

    pz.cleanup()
    robot.finish()

except IOError:
    print("Unable to find any joystick")
except robot.RosiException as e:
    print(e.value)
except KeyboardInterrupt:
    robot.finish()    
