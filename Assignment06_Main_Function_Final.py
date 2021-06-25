# Assignment 06
# Group 16
#
# Programming Languages SUM2021

import tkinter
import threading
import time
import random
from queue import Queue

synch = threading.Barrier(6)
queue = Queue(maxsize = 0)
minimum = 1
maximum = 5

class Producer:
    #constructor
    def __init__(self, ID, Min, Max):
        self.ID = ID
        self.Min = Min
        self.Max = Max

    def generate(self):
        x = random.randint(self.Min, self.Max)
        return x

class Consumer:
    #constructor
    def __init__(self, ID):
        self.tally = 0
        self.ID = ID
    def consume(self):
        self.tally = self.tally + 1
        hold = queue.get()
        print('*' * 35)
        print('The tally amount is ' + str(self.tally))
        print('The produced item is item ' + str(hold))
        print('*' * 35)
        if self.ID == 4:
            consumeLabel2['text'] = "The Consumer ID is {}\nThe tally amount is {}\nThe produced item is item {}".format(self.ID, str(self.tally), str(hold))
        elif self.ID == 5:
            consumeLabel4['text'] = "The Consumer ID is {}\nThe tally amount is {}\nThe produced item is item {}".format(self.ID, str(self.tally), str(hold))
        elif self.ID == 6:
            consumeLabel6['text'] = "The Consumer ID is {}\nThe tally amount is {}\nThe produced item is item {}".format(self.ID, str(self.tally), str(hold))

class myThread (threading.Thread):
    def __init__(self, threadID, name, kill):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.kill = kill
    def run(self):
        print("Starting {} thread {}\n".format(self.name, self.threadID))
        if self.name == "Producer":
            producer(self)
        elif self.name == "Consumer":
            consumer(self)

def producer(self):
    producer = Producer(self.threadID, minimum, maximum)
    while self.kill == 0:
        hold = producer.generate()
        queue.put(hold)
        PQLabel['text']=str(queue.queue)
        synch.wait()
        time.sleep(2)

def consumer(self):
    consumer = Consumer(self.threadID)
    while self.kill == 0:
        time.sleep((self.threadID-3)/10)
        consumer.consume()
        synch.wait()
        time.sleep(2)   

class main():

    def __init__(self):
        self.end = 0

    def start(self):
        self.produceThread = myThread(1, "Producer", 0)
        self.produceThread2 = myThread(2, "Producer", 0)
        self.produceThread3 = myThread(3, "Producer", 0)
        self.consumeThread = myThread(4, "Consumer", 0)
        self.consumeThread2 = myThread(5, "Consumer", 0)
        self.consumeThread3 = myThread(6, "Consumer", 0)
        self.produceThread.start()
        self.produceThread2.start()
        self.produceThread3.start()
        self.consumeThread.start()
        self.consumeThread2.start()
        self.consumeThread3.start()

    def stop(self):
        self.produceThread.kill = 1
        self.consumeThread.kill = 1
        self.produceThread2.kill = 1
        self.produceThread3.kill = 1
        self.consumeThread2.kill = 1
        self.consumeThread3.kill = 1

if __name__ == "__main__":
    main = main()

    gui = tkinter.Tk()
    gui.title("Main_Interface_Assigment06")
    gui.geometry("1024x768")
    label = tkinter.Label(gui, text = "Welcome to Group 16's shop! Here you can purchase all the numbers you could ever want!", font=("Arial", 15), bg="white").pack()
    start = tkinter.Button(height = 1, width = 10, bg = "green", text = "Start", command = main.start)
    start.place(x=492, y=50)
    stop = tkinter.Button(height = 1, width = 10, bg = "red", text = "Stop", command = main.stop)
    stop.place(x=492, y=90)
    produceLabel = tkinter.Label(gui, text = "Producer's Output", font=("Arial", 15), bg="white")
    produceLabel.place(x=100, y=150)
    PQLabel = tkinter.Label(gui, text = "", font=("Arial", 15))
    PQLabel.place(x=100, y=200)
    canvas = tkinter.Canvas(gui, height=768, width=1024)
    canvas.create_rectangle(0, 0, 1024, 768,
                            outline = "black", fill = "black",
                            width = 2)
    canvas.place(x=450, y=150)
    consumeLabel1 = tkinter.Label(gui, text = '*' * 35, fg = 'white', bg='black', font=("Arial", 15), borderwidth=0)
    consumeLabel1.place(x=455, y=155)
    consumeLabel2 = tkinter.Label(gui, text = "The Consumer ID is NONE\nThe tally amount is NONE\nThe produced item is item NONE", fg = 'white', bg='black', font=("Arial", 15), borderwidth=0, anchor="nw")
    consumeLabel2.place(x=455, y=185)
    consumeLabel3 = tkinter.Label(gui, text = '*' * 35, fg = 'white', bg='black', font=("Arial", 15), borderwidth=0)
    consumeLabel3.place(x=455, y=275)
    consumeLabel4 = tkinter.Label(gui, text = "The Consumer ID is NONE\nThe tally amount is NONE\nThe produced item is item NONE", fg = 'white', bg='black', font=("Arial", 15), borderwidth=0, anchor="nw")
    consumeLabel4.place(x=455, y=305)
    consumeLabel5 = tkinter.Label(gui, text = '*' * 35, fg = 'white', bg='black', font=("Arial", 15), borderwidth=0)
    consumeLabel5.place(x=455, y=395)
    consumeLabel6 = tkinter.Label(gui, text = "The Consumer ID is NONE\nThe tally amount is NONE\nThe produced item is item NONE", fg = 'white', bg='black', font=("Arial", 15), borderwidth=0, anchor="nw")
    consumeLabel6.place(x=455, y=425)
    consumeLabel7 = tkinter.Label(gui, text = '*' * 35, fg = 'white', bg='black', font=("Arial", 15), borderwidth=0)
    consumeLabel7.place(x=455, y=515)
    
    gui.mainloop()
