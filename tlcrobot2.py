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

GREEN = 0
RED = 1
YELLOW = 2


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
                pz.setOutput(GREEN,0)
                pz.setOutput(RED,0)
                pz.setOutput(YELLOW,0)
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
                pz.setOutput(GREEN,100)
                pz.setMotor(0,30)
                pz.setMotor(1,-30)

            if joystick.presses.dright:
                # ******** DO SOMETHING HERE ********  
                print("D Right")
                pz.setOutput(YELLOW,100)
                pz.setMotor(0,-30)
                pz.setMotor(1,30)

            if joystick.presses.dup:
                # ******** DO SOMETHING HERE ********  
                print("D Up")
                pz.setOutput(RED,100)
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
                
                      
                # ******** DO SOMETHING HERE ********
            if joystick.ly or joystick.rx:
                leftVertical = joystick.ly
                rightHorizontal = joystick.rx

                # We want to move the robot according to the joystick positions

                # leftVertical: 1.0 for full forward, -1.0 for full backward, 0.0 for stop.
                # rightHorizontal: 1.0 for full right, -1.0 for full left, 0.0 for straight

                #Work out motor speed based on forward-backward axis
                leftMotorSpeed = leftVertical * 50
                rightMotorSpeed = leftVertical * 50

                #Adjust motor speed based on right-left axis
                if rightHorizontal < 0:
                    # Turning Left, slow the left motor down
                    leftMotorSpeed  = leftMotorSpeed - leftMotorSpeed * -rightHorizontal
                elif rightHorizontal >0:
                    # Turning rigth, slow the right motor down
                    rightMotorSpeed = rightMotorSpeed - rightMotorSpeed * rightHorizontal

                
                print("Stick Left Y or Right X", joystick.ly, " ", joystick.rx)
                pz.setMotor(0,int(leftMotorSpeed))
                pz.setMotor(1,int(rightMotorSpeed))

             
                
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

