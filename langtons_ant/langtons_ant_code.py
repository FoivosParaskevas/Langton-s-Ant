import tkinter as tk
import pyautogui
from tkinter import filedialog
import turtle
from PIL import ImageTk, Image
import random as rn

class Demo:
    def __init__(self,root):
        self.root=root
        self.canvas=tk.Canvas(master = root, width = 800, height = 600)
        self.canvas.grid(row=0,column=0,padx=0,ipadx=10,rowspan=6,columnspan=10)


        self.ant = turtle.RawTurtle(self.canvas)
        self.ant.speed("fastest")
        self.ant.penup()
          
        #####IF_clearCounter_DOES_NOT_EXIST_IF_YOU_PRESS_CLEAR_BUTTON_BEFORE_ANYTHING_ELSE_YOU'LL_GET_AN_ERROR#####
        self.clearCounter=0

        #####IF_pauseCounter_TURNS_0_ANT_STOPS_MOVING#####
        self.pauseCounter=1

        #####STARTS_THE_SUITABLE_FUNCTION#####
        self.functionCounter=0

        #####WE_USE_destroyCounter_IN_ORDER_TO_DESTROY_THE_FRAME_THAT_SHOWS_THE_COUNTER_OF_THE_COLOURS_IN_ORDER_TO_CREATE_A_NEW_FRAME_FOR_OTHER_COLOURS#####
        self.destroyCounter=0
        
        self.resume=0

        self.create_buttons()


    #####CREATING_BUTTONS_AND_TOP_LABEL#####
    def create_buttons(self):
        self.label=tk.Label(root,text="Langton's Ant", width=25, font="Arial 20")
        self.label.grid(row=0,column=10,ipadx=3,ipady=3, columnspan=2)


        #####FIRST_COLUMN#####
        self.button=tk.Button(root,text="2 colours",padx=1, width=25, font="Arial 10", command=self.two_colours_primary)
        self.button.grid(row=1,column=10,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="3 colours (chaotic)",padx=1, width=25, font="Arial 10", command=self.three_colours_primary)
        self.button.grid(row=2,column=10,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="3 colours (simple)",padx=1, width=25, font="Arial 10", command=self.three_colours_simple_primary)
        self.button.grid(row=3,column=10,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="10 colours",padx=1, width=25, font="Arial 10", command=self.ten_colours_primary)
        self.button.grid(row=4,column=10,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="Random Spots",padx=1, width=25, font="Arial 10", command=self.random_spots_primary)
        self.button.grid(row=5,column=10,ipadx=3,ipady=35, columnspan=1)


        #####SECOND_COLUMN#####
        self.button=tk.Button(root,text="Resume",padx=1, width=25, font="Arial 10", command=self.resumeButton)
        self.button.grid(row=1,column=11,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="Pause",padx=1, width=25, font="Arial 10", command=self.pauseButton)
        self.button.grid(row=2,column=11,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="Clear",padx=1, width=25, font="Arial 10", command=self.clearScreen)
        self.button.grid(row=3,column=11,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="Screenshot",padx=1, width=25, font="Arial 10", command=self.takeScreenshot)
        self.button.grid(row=4,column=11,ipadx=3,ipady=35, columnspan=1)
        self.button=tk.Button(root,text="Quit\n(Press Pause Button First)",padx=1,fg="red", width=25, font="Arial 10", command=self.quitButton)
        self.button.grid(row=5,column=11,ipadx=3,ipady=27, columnspan=1)


        #####CREATS_STATISTIC_COUNTERS#####
        self.myText = tk.StringVar()
        self.label=tk.Label(root, textvariable=self.myText, font="Arial 10")
        self.label.grid(row=6, column=10,ipadx=60, ipady=35,columnspan=2)
        

    def invert(self, graph, ant, color): 
        graph[self.coordinate(ant)] = color 
  
    def coordinate(self, ant): 
        return (round(ant.xcor()), round(ant.ycor())) 



    #####LANGTON'S_ANT_2_COLOURS#####
    def two_colours(self):

        self.ant.showturtle()

        if self.clearCounter==0: self.clearCounter=1
        self.destroyCounter=1

        self.ant.shape('square')
        self.ant.shapesize(0.5)
        
        self.pos = self.coordinate(self.ant)                              

        if self.resume==0:
            self.clearScreen()
            self.maps={}
            self.ant.goto(0,0)
            self.stepCounter=0
            self.whiteCounter=0
            self.blackCounter=0

        self.pauseCounter=1

        
        while self.pauseCounter: 
              
            self.step = 10                                     
            if self.pos not in self.maps: 
                  
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.statistics()



            elif self.maps[self.pos] == "white":
                
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.whiteCounter-=1
                self.statistics()


            
            elif self.maps[self.pos] == "black": 
                self.ant.fillcolor("white") 
                self.invert(self.maps, self.ant, "white") 
                  
                self.ant.stamp() 
                self.ant.left(90) 
                self.ant.forward(self.step) 
                self.pos = self.coordinate(self.ant)

                self.whiteCounter+=1
                self.blackCounter-=1
                self.statistics()

            self.stepCounter+=1
            self.stepsCounter()
      


    #####LANGTON'S_ANT_3_COLOURS#####  
    def three_colours(self):
        
        self.ant.showturtle()

        if self.clearCounter==0: self.clearCounter=1
        self.destroyCounter=1
 
        self.ant.shape('square')     
        self.ant.shapesize(0.5)

        if self.resume==0:
            self.clearScreen()
            self.maps = {} 
            self.ant.goto(0,0)
            self.stepCounter=0
            self.whiteCounter=0
            self.blackCounter=0
            self.blueCounter=0
          
        self.pos = self.coordinate(self.ant)                              
        
        self.pauseCounter=1
        
        while self.pauseCounter: 
              
            self.step = 10                                     
            if self.pos not in self.maps: 
                  
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.statistics()


            elif self.maps[self.pos] == "white":

                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.whiteCounter-=1
                self.statistics()


                
            elif self.maps[self.pos] == "black": 
                self.ant.fillcolor("blue") 
                self.invert(self.maps, self.ant, "blue") 
                  
                self.ant.stamp() 
                self.ant.left(90) 
                self.ant.forward(self.step) 
                self.pos = self.coordinate(self.ant)

                self.blueCounter+=1
                self.blackCounter-=1
                self.statistics()
      

            elif self.maps[self.pos] == "blue":
                self.ant.fillcolor("white")
                self.invert(self.maps, self.ant, "white")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.whiteCounter+=1
                self.blueCounter-=1
                self.statistics()

            self.stepCounter+=1
            self.stepsCounter()



    #####LANGTON'S_ANT_3_COLOURS_SIMPLE#####  
    def three_colours_simple(self):
        
        self.ant.showturtle()
        
        if self.clearCounter==0: self.clearCounter=1
        self.destroyCounter=1

        if self.resume==0:
            self.clearScreen()
            self.maps = {}
            self.ant.goto(0,0)
            self.stepCounter=0
            self.whiteCounter=0
            self.blackCounter=0
            self.blueCounter=0
        
        self.ant.shape('square')
        self.ant.shapesize(0.5)
          
        self.pos = self.coordinate(self.ant)
        
        self.pauseCounter=1
        
        while self.pauseCounter:               
            self.step = 10                                     
            if self.pos not in self.maps: 
                  
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.statistics()


            elif self.maps[self.pos] == "white":

                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.whiteCounter-=1
                self.statistics()


                
            elif self.maps[self.pos] == "black": 
                self.ant.fillcolor("blue") 
                self.invert(self.maps, self.ant, "blue") 
                  
                self.ant.stamp() 
                self.ant.right(90) 
                self.ant.forward(self.step) 
                self.pos = self.coordinate(self.ant)

                self.blueCounter+=1
                self.blackCounter-=1
                self.statistics()
      

            elif self.maps[self.pos] == "blue":
                self.ant.fillcolor("white")
                self.invert(self.maps, self.ant, "white")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.whiteCounter+=1
                self.blueCounter-=1
                self.statistics()

            self.stepCounter+=1
            self.stepsCounter()

        
    #####LANGTON'S_ANT_10_COLOURS#####    
    def ten_colours(self):
        
        self.ant.showturtle()
        
        if self.clearCounter==0: self.clearCounter=1
        self.destroyCounter=1

        if self.resume==0:
            self.clearScreen()
            self.maps = {}
            self.ant.goto(0,0)
            self.stepCounter=0
            self.whiteCounter=0
            self.blackCounter=0
            self.blueCounter=0
            self.greenCounter=0
            self.purpleCounter=0
            self.yellowCounter=0
            self.orangeCounter=0
            self.pinkCounter=0
            self.cyanCounter=0
            self.redCounter=0
        
        self.ant.shape('square')
        self.ant.shapesize(0.5) 

        self.pos = self.coordinate(self.ant)
        
        self.pauseCounter=1
        
        while self.pauseCounter:               
            self.step = 10                                     
            if self.pos not in self.maps: 
                  
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.statistics()


            elif self.maps[self.pos] == "white":

                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.whiteCounter-=1
                self.statistics()

                
            elif self.maps[self.pos] == "black": 
                self.ant.fillcolor("blue") 
                self.invert(self.maps, self.ant, "blue") 
                  
                self.ant.stamp() 
                self.ant.left(90) 
                self.ant.forward(self.step) 
                self.pos = self.coordinate(self.ant)

                self.blueCounter+=1
                self.blackCounter-=1
                self.statistics()
      

            elif self.maps[self.pos] == "blue":
                self.ant.fillcolor("green")
                self.invert(self.maps, self.ant, "green")

                self.ant.stamp()
                self.ant.right(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)
                
                self.greenCounter+=1
                self.blueCounter-=1
                self.statistics()

            elif self.maps[self.pos] == "green":
                self.ant.fillcolor("purple")
                self.invert(self.maps, self.ant, "purple")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.purpleCounter+=1
                self.greenCounter-=1
                self.statistics()

            elif self.maps[self.pos] == "purple":
                self.ant.fillcolor("yellow")
                self.invert(self.maps, self.ant, "yellow")

                self.ant.stamp()
                self.ant.right(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.yellowCounter+=1
                self.purpleCounter-=1
                self.statistics()


            elif self.maps[self.pos] == "yellow":
                self.ant.fillcolor("orange")
                self.invert(self.maps, self.ant, "orange")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.orangeCounter+=1
                self.yellowCounter-=1
                self.statistics()


            elif self.maps[self.pos] == "orange":
                self.ant.fillcolor("pink")
                self.invert(self.maps, self.ant, "pink")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.pinkCounter+=1
                self.orangeCounter-=1
                self.statistics()

            elif self.maps[self.pos] == "pink":
                self.ant.fillcolor("cyan")
                self.invert(self.maps, self.ant, "cyan")

                self.ant.stamp()
                self.ant.right(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.cyanCounter+=1
                self.pinkCounter-=1
                self.statistics()

            elif self.maps[self.pos] == "cyan":
                self.ant.fillcolor("red")
                self.invert(self.maps, self.ant, "red")

                self.ant.stamp()
                self.ant.left(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.redCounter+=1
                self.cyanCounter-=1
                self.statistics()

            elif self.maps[self.pos] == "red":
                self.ant.fillcolor("white")
                self.invert(self.maps, self.ant, "white")

                self.ant.stamp()
                self.ant.right(90)
                self.ant.forward(self.step)
                self.pos=self.coordinate(self.ant)

                self.whiteCounter+=1
                self.redCounter-=1
                self.statistics()

            self.stepCounter+=1
            self.stepsCounter()





    #####LANGTON'S_ANT_RANDOM_SPOTS#####
    def random_spots(self):

        self.ant.showturtle()
        
        if self.clearCounter==0: self.clearCounter=1
        self.destroyCounter=1

        if self.resume==0:
            self.clearScreen()
            self.maps = {}
            self.ant.goto(0,0)
            self.stepCounter=0
            self.whiteCounter=0
            self.blackCounter=0
            
        
        self.ant.shape('square')
        self.ant.shapesize(0.5) 

        self.pos = self.coordinate(self.ant)
        
        self.pauseCounter=1
        if self.resume==0:
            for i in range(rn.randint(6,15)):
                    self.ant.goto(round(rn.randint(-100,100)/100)*100,round(rn.randint(-100,100)/100)*100)
                    self.pos = self.coordinate(self.ant)
                    
                    if self.pos not in self.maps:
                        self.ant.fillcolor("black")               
                        self.ant.stamp()                                  
                        self.invert(self.maps, self.ant, "black")
                        self.ant.goto(0,0)
                        self.ant.setheading(0)
                        self.blackCounter+=1
                    
        self.statistics()
        
        while self.pauseCounter: 
              
            self.step = 10                                     
            if self.pos not in self.maps: 
                  
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.statistics()



            elif self.maps[self.pos] == "white":
                
                self.ant.fillcolor("black")         
                  
                self.ant.stamp()                                  
                self.invert(self.maps, self.ant, "black") 
                self.ant.right(90) 
                  
                self.ant.forward(self.step)                          
                self.pos = self.coordinate(self.ant)

                self.blackCounter+=1
                self.whiteCounter-=1
                self.statistics()


            
            elif self.maps[self.pos] == "black": 
                self.ant.fillcolor("white") 
                self.invert(self.maps, self.ant, "white") 
                  
                self.ant.stamp() 
                self.ant.left(90) 
                self.ant.forward(self.step) 
                self.pos = self.coordinate(self.ant)

                self.whiteCounter+=1
                self.blackCounter-=1
                self.statistics()

            self.stepCounter+=1
            self.stepsCounter()


    
        
    def quitButton(self):
        self.root.destroy()

    #####SCREENSHOT_FUNCTION#####
    def takeScreenshot(self):
        myScreenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        myScreenshot.save(file_path)



    def clearScreen(self):
        if self.clearCounter==1:
            self.pauseButton()
            self.ant.hideturtle()
            self.ant.clear()
            self.ant.clearstamps()
            self.ant.goto(0,0)
            self.ant.setheading(0)
            self.maps={}
            self.stepCounter=0
            self.stepsCounter()
            self.whiteCounter=0
            self.blackCounter=0
            self.blueCounter=0
            self.greenCounter=0
            self.purpleCounter=0
            self.yellowCounter=0
            self.orangeCounter=0
            self.pinkCounter=0
            self.cyanCounter=0
            self.redCounter=0
            self.statistics()
                

    def resumeButton(self):
        self.pauseCounter=1
        self.resume=1
        
        if self.two_coloursCounter:
            self.two_colours()

        elif self.three_coloursCounter:
            self.three_colours()

        elif self.three_colours_simpleCounter:
            self.three_colours_simple()

        elif self.ten_coloursCounter:
            self.ten_colours()

        elif self.random_spotsCounter:
            self.random_spots()
        

        
    def pauseButton(self):
        self.pauseCounter=0



    def two_colours_primary(self):
        self.two_coloursCounter = 1
        self.three_coloursCounter = 0
        self.three_colours_simpleCounter = 0
        self.ten_coloursCounter = 0
        self.random_spotsCounter = 0
        self.callBack()

    def three_colours_primary(self):
        self.two_coloursCounter = 0
        self.three_coloursCounter = 1
        self.three_colours_simpleCounter = 0
        self.ten_coloursCounter = 0
        self.random_spotsCounter = 0
        self.callBack()

    def three_colours_simple_primary(self):
        self.two_coloursCounter = 0
        self.three_coloursCounter = 0
        self.three_colours_simpleCounter = 1
        self.ten_coloursCounter = 0
        self.random_spotsCounter = 0
        self.callBack()

    def ten_colours_primary(self):
        self.two_coloursCounter = 0
        self.three_coloursCounter = 0
        self.three_colours_simpleCounter = 0
        self.ten_coloursCounter = 1
        self.random_spotsCounter = 0
        self.callBack()

    def random_spots_primary(self):
        self.two_coloursCounter = 0
        self.three_coloursCounter = 0
        self.three_colours_simpleCounter = 0
        self.ten_coloursCounter = 0
        self.random_spotsCounter = 1
        self.callBack()

        

    def callBack(self):
        self.resume=0
        self.statisticsCounter=1
        if self.two_coloursCounter:
            self.createStatistics()
            self.two_colours()

        elif self.three_coloursCounter:
            self.createStatistics()
            self.three_colours()

        elif self.three_colours_simpleCounter:
            self.createStatistics()
            self.three_colours_simple()

        elif self.ten_coloursCounter:
            self.createStatistics()
            self.ten_colours()

        elif self.random_spotsCounter:
            self.createStatistics()
            self.random_spots()

        
    def stepsCounter(self):
        if self.stepCounter == 0 or self.stepCounter == 1: end = ''
        else: end= 's'
        self.myText.set("Step"+ end +"- "+str(self.stepCounter))
        

    def statistics(self):
        
        if self.two_coloursCounter:
            
            self.whiteText.set("- " +str(self.whiteCounter))
            self.blackText.set("- " +str(self.blackCounter))


        elif self.three_coloursCounter:

            self.whiteText.set("- " +str(self.whiteCounter))
            self.blackText.set("- " +str(self.blackCounter))
            self.blueText.set("- " +str(self.blueCounter))

        elif self.three_colours_simpleCounter:

            self.whiteText.set("- " +str(self.whiteCounter))
            self.blackText.set("- " +str(self.blackCounter))
            self.blueText.set("- " +str(self.blueCounter))

        elif self.ten_coloursCounter:

            self.whiteText.set("- " +str(self.whiteCounter))
            self.blackText.set("- " +str(self.blackCounter))
            self.blueText.set("- " +str(self.blueCounter))
            self.greenText.set("- " +str(self.greenCounter))
            self.purpleText.set("- " +str(self.purpleCounter))
            self.yellowText.set("- " +str(self.yellowCounter))
            self.orangeText.set("- " +str(self.orangeCounter))
            self.pinkText.set("- " +str(self.pinkCounter))
            self.cyanText.set("- " +str(self.cyanCounter))
            self.redText.set("- " +str(self.redCounter))
            

        elif self.random_spotsCounter:
            
            self.whiteText.set("- " +str(self.whiteCounter))
            self.blackText.set("- " +str(self.blackCounter))


    def createStatistics(self):
        if self.destroyCounter==1:
            self.frame.destroy()

        
        self.frame=tk.Frame(root)
        self.frame.grid(row=6,column=0,rowspan=2,columnspan=10)
            
        if self.two_coloursCounter:
            self.imgWhite=ImageTk.PhotoImage(Image.open("white.png"))
            self.white=tk.Label(self.frame, image=self.imgWhite)
            self.white.grid(row=6,column=0)
            self.whiteText=tk.StringVar()
            self.myWhite=tk.Label(self.frame, textvariable=self.whiteText)
            self.myWhite.grid(row=6,column=1)

            self.imgBlack=ImageTk.PhotoImage(Image.open("black.png"))
            self.black=tk.Label(self.frame, image=self.imgBlack)
            self.black.grid(row=7,column=0)
            self.blackText=tk.StringVar()
            self.myBlack=tk.Label(self.frame, textvariable=self.blackText)
            self.myBlack.grid(row=7,column=1)


        elif self.three_coloursCounter:
            self.imgWhite=ImageTk.PhotoImage(Image.open("white.png"))
            self.white=tk.Label(self.frame, image=self.imgWhite)
            self.white.grid(row=6,column=0)
            self.whiteText=tk.StringVar()
            self.myWhite=tk.Label(self.frame, textvariable=self.whiteText)
            self.myWhite.grid(row=6,column=1)

            self.imgBlack=ImageTk.PhotoImage(Image.open("black.png"))
            self.black=tk.Label(self.frame, image=self.imgBlack)
            self.black.grid(row=7,column=0)
            self.blackText=tk.StringVar()
            self.myBlack=tk.Label(self.frame, textvariable=self.blackText)
            self.myBlack.grid(row=7,column=1)

            self.imgBlue=ImageTk.PhotoImage(Image.open("blue.png"))
            self.blue=tk.Label(self.frame, image=self.imgBlue)
            self.blue.grid(row=6,column=2)
            self.blueText=tk.StringVar()
            self.myBlue=tk.Label(self.frame, textvariable=self.blueText)
            self.myBlue.grid(row=6,column=3)
            

        elif self.three_colours_simpleCounter:
            self.imgWhite=ImageTk.PhotoImage(Image.open("white.png"))
            self.white=tk.Label(self.frame, image=self.imgWhite)
            self.white.grid(row=6,column=0)
            self.whiteText=tk.StringVar()
            self.myWhite=tk.Label(self.frame, textvariable=self.whiteText)
            self.myWhite.grid(row=6,column=1)

            self.imgBlack=ImageTk.PhotoImage(Image.open("black.png"))
            self.black=tk.Label(self.frame, image=self.imgBlack)
            self.black.grid(row=7,column=0)
            self.blackText=tk.StringVar()
            self.myBlack=tk.Label(self.frame, textvariable=self.blackText)
            self.myBlack.grid(row=7,column=1)

            self.imgBlue=ImageTk.PhotoImage(Image.open("blue.png"))
            self.blue=tk.Label(self.frame, image=self.imgBlue)
            self.blue.grid(row=6,column=2)
            self.blueText=tk.StringVar()
            self.myBlue=tk.Label(self.frame, textvariable=self.blueText)
            self.myBlue.grid(row=6,column=3)

        elif self.ten_coloursCounter:
            self.imgWhite=ImageTk.PhotoImage(Image.open("white.png"))
            self.white=tk.Label(self.frame, image=self.imgWhite)
            self.white.grid(row=6,column=0)
            self.whiteText=tk.StringVar()
            self.myWhite=tk.Label(self.frame, textvariable=self.whiteText)
            self.myWhite.grid(row=6,column=1)

            self.imgBlack=ImageTk.PhotoImage(Image.open("black.png"))
            self.black=tk.Label(self.frame, image=self.imgBlack)
            self.black.grid(row=7,column=0)
            self.blackText=tk.StringVar()
            self.myBlack=tk.Label(self.frame, textvariable=self.blackText)
            self.myBlack.grid(row=7,column=1)

            self.imgBlue=ImageTk.PhotoImage(Image.open("blue.png"))
            self.blue=tk.Label(self.frame, image=self.imgBlue)
            self.blue.grid(row=6,column=2)
            self.blueText=tk.StringVar()
            self.myBlue=tk.Label(self.frame, textvariable=self.blueText)
            self.myBlue.grid(row=6,column=3)

            self.imgGreen=ImageTk.PhotoImage(Image.open("green.png"))
            self.green=tk.Label(self.frame, image=self.imgGreen)
            self.green.grid(row=7,column=2)
            self.greenText=tk.StringVar()
            self.myGreen=tk.Label(self.frame, textvariable=self.greenText)
            self.myGreen.grid(row=7,column=3)

            self.imgPurple=ImageTk.PhotoImage(Image.open("purple.png"))
            self.purple=tk.Label(self.frame, image=self.imgPurple)
            self.purple.grid(row=6,column=4)
            self.purpleText=tk.StringVar()
            self.myPurple=tk.Label(self.frame, textvariable=self.purpleText)
            self.myPurple.grid(row=6,column=5)

            self.imgYellow=ImageTk.PhotoImage(Image.open("yellow.png"))
            self.yellow=tk.Label(self.frame, image=self.imgYellow)
            self.yellow.grid(row=7,column=4)
            self.yellowText=tk.StringVar()
            self.myYellow=tk.Label(self.frame, textvariable=self.yellowText)
            self.myYellow.grid(row=7,column=5)

            self.imgOrange=ImageTk.PhotoImage(Image.open("orange.png"))
            self.orange=tk.Label(self.frame, image=self.imgOrange)
            self.orange.grid(row=6,column=6)
            self.orangeText=tk.StringVar()
            self.myOrange=tk.Label(self.frame, textvariable=self.orangeText)
            self.myOrange.grid(row=6,column=7)

            self.imgPink=ImageTk.PhotoImage(Image.open("pink.png"))
            self.pink=tk.Label(self.frame, image=self.imgPink)
            self.pink.grid(row=7,column=6)
            self.pinkText=tk.StringVar()
            self.myPink=tk.Label(self.frame, textvariable=self.pinkText)
            self.myPink.grid(row=7,column=7)

            self.imgCyan=ImageTk.PhotoImage(Image.open("cyan.png"))
            self.cyan=tk.Label(self.frame, image=self.imgCyan)
            self.cyan.grid(row=6,column=8)
            self.cyanText=tk.StringVar()
            self.myCyan=tk.Label(self.frame, textvariable=self.cyanText)
            self.myCyan.grid(row=6,column=9)
            
            self.imgRed=ImageTk.PhotoImage(Image.open("red.png"))
            self.red=tk.Label(self.frame, image=self.imgRed)
            self.red.grid(row=7,column=8)
            self.redText=tk.StringVar()
            self.myRed=tk.Label(self.frame, textvariable=self.redText)
            self.myRed.grid(row=7,column=9)
            

        elif self.random_spotsCounter:
            self.imgWhite=ImageTk.PhotoImage(Image.open("white.png"))
            self.white=tk.Label(self.frame, image=self.imgWhite)
            self.white.grid(row=6,column=0)
            self.whiteText=tk.StringVar()
            self.myWhite=tk.Label(self.frame, textvariable=self.whiteText)
            self.myWhite.grid(row=6,column=1)

            self.imgBlack=ImageTk.PhotoImage(Image.open("black.png"))
            self.black=tk.Label(self.frame, image=self.imgBlack)
            self.black.grid(row=7,column=0)
            self.blackText=tk.StringVar()
            self.myBlack=tk.Label(self.frame, textvariable=self.blackText)
            self.myBlack.grid(row=7,column=1)




root=tk.Tk()
Demo(root)
root.mainloop()
