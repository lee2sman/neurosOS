#!/usr/bin/env python

from os import system
import curses
import time
from random import randint

def get_param(prompt_string):
  screen.clear()
  screen.border(0)
  screen.addstr(2, 2, prompt_string)
  screen.refresh()
  input = screen.getstr(10, 10, 60)
  return input

def execute_cmd(cmd_string):
  system("clear")
  a = system(cmd_string)
  print ""
  if a != 0:
    print "Command terminated with error"
    raw_input("Press enter")

x=0

#MAIN LOOP
while x != ord('4'):
  screen = curses.initscr()
  curses.start_color() # Lets you use colors when highlighting selected menu option
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE) # Sets up color pair #1, it does blue text with white background
  textColoring = curses.color_pair(1) #this is the coloring for a highlighted menu option
  screen.clear()
  screen.border(0)
  screen.addstr(4, 5, " ----------------------------------------------------------------")
  screen.addstr(5, 5, "|                                                                |__")
  screen.addstr(6, 5, "|                                                888     8888    |  |")
  screen.addstr(7, 5, "|                                               8   8   88   8   |[]|")
  screen.addstr(8, 5, "|  88   8 88888 8    8 8888     888     8888   8     8  88       |__|  ")
  screen.addstr(9, 5, "|  8 8  8 8     8    8 8   8   8   8   8       8     8   888     |  ")
  screen.addstr(10, 5, "|  8  8 8 8888  8    8 8888   8     8   888    8     8     88    |__")
  screen.addstr(11, 5, "|  8   88 8      8  8  8  8    8   8       8    8   8   8   88   |  |")
  screen.addstr(12, 5, "|  8    8 88888   88   8   8    888    88888     888     8888    |[]|")
  screen.addstr(13, 5, "|                                                                |__|")
  screen.addstr(14, 5, "|                                                                |")
  screen.addstr(15, 5, " ----------------------------------------------------------------")
  screen.addstr(18, 21, "+--------------------+") #MENU
  screen.addstr(19, 21, "|   | MENU           |")
  screen.addstr(20, 21, "+--------------------+")
  screen.addstr(21, 21, "| 1 | Examination    |")
  screen.addstr(22, 21, "| 2 | Information    |")
  screen.addstr(23, 21, "| 3 | Calendar       |")
  screen.addstr(24, 21, "| 4 | Quit           |")
  screen.addstr(25, 21, "+--------------------+")
  screen.refresh()
  x = screen.getch()
  if x == ord("4"):
    break
  elif x == ord('1'):
    screen.clear()
    screen.addstr(12, 12, "Welcome To The NeurosOS Exam", curses.color_pair(1))
    screen.addstr(15, 12, "Press (1) for Patients Previously In System", curses.A_STANDOUT)
    screen.addstr(16, 12, "Press (ENTER) for New Patients.", curses.A_BLINK)
    screen.getch()
    screen.clear()
    #EXAM SCREEN 2
    screen.clear()
    screen.addstr(12, 12, "Enter client's Blood Type", curses.color_pair(1))
    screen.addstr(15, 12, "Press (1) for O+ or O-", curses.A_STANDOUT)
    screen.addstr(16, 12, "Press (2) for A+ or A-", curses.A_STANDOUT)
    screen.addstr(17, 12, "Press (3) for B+ or B-", curses.A_STANDOUT)
    screen.addstr(18, 12, "Press (4) for AB+", curses.A_STANDOUT)
    screen.addstr(19, 12, "Press (5) for AB-", curses.A_STANDOUT)
    screen.addstr(20, 12, "Press (6) for Unknown", curses.A_STANDOUT)
    screen.getch()
    #EXAM SCREEN 3
    screen.clear()
    screen.addstr(12, 12, "Press [Enter] If The Client Has Used One of the Following Devices In The Past 8 Hours", curses.color_pair(1))
    screen.addstr(15, 12, "iOS or Android Device", curses.A_STANDOUT)
    screen.addstr(16, 12, "Laptop or Desktop Computer With Internet", curses.A_STANDOUT)
    screen.addstr(17, 12, "Smart-watch or networked health tracking device", curses.A_STANDOUT)
    screen.addstr(18, 12, "Other Screenbased or Networked Devices", curses.A_STANDOUT)
    screen.getch()
    #EXAM SCREEN 4
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(13, 12, "How would you rate your experience with the following?", curses.color_pair(1))
    screen.addstr(15, 12, "I regularly experience FOMO (Fear Of Missing Out)", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(16, 12, "I seek pleasure in anti-social ways", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(17, 12, "I hide behind my online persona", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(18, 12, "I maintain a positive online social presence despite bouts of sadness or depression", curses.A_STANDOUT)
    screen.getch()
    #EXAM SCREEN 5
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(15, 12, "Sometimes I use my phone as a way to avoid interaction with others", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(16, 12, "I prefer my online friendships to my IRL (In Real Life) friendships", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(17, 12, "Sometimes I'm unable to ignore the phone when working, in class, or talking to friends or family", curses.A_STANDOUT)
    screen.getch()
    #EXAM SCREEN 6
    screen.clear()
    screen.addstr(12, 12, "On a scale from 0 (not at all) to 9 (completely)", curses.color_pair(1))
    screen.addstr(18, 12, "I often check my phone to see if I've missed any notifications", curses.A_STANDOUT)
    screen.addstr(19, 12, "OR I tend to check all the notifications I have as they stream in througout the day", curses.A_STANDOUT)
    screen.getch()
    #EXAM SCREEN 7
    screen.clear()
    screen.addstr(12, 12, "Press [Enter] If You Have Experienced The Following Effects Via Technology In The Past Month or (2) To Skip", curses.color_pair(1))
    screen.addstr(15, 12, "Losing Track of Time While Browsing Internet", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Press [Enter] If You Have Experienced The Following Effects Via Technology In The Past Month or (2) To Skip", curses.color_pair(1))
    screen.addstr(16, 12, "Binge Streaming", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Press [Enter] If You Have Experienced The Following Effects Via Technology In The Past Month or (2) To Skip", curses.color_pair(1))
    screen.addstr(17, 12, "Being overwhelmed with tens or dozens of open browser tabs", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Do You Agree With The Following Sentiment?", curses.color_pair(1))
    screen.addstr(13, 12, "Press [ENTER] For YES. Press [0] To Skip.", curses.color_pair(1))
    screen.addstr(15, 12, "I Do Not NEED My Smartphone But I LIKE HAVING My Smartphone", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Do You Agree With The Following Sentiment?", curses.color_pair(1))
    screen.addstr(13, 12, "Press [ENTER] For YES. Press [0] To Skip.", curses.color_pair(1))
    screen.addstr(16, 12, "I Wish I Had An Assistant To Answer My Digital Communication", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Do You Agree With The Following Sentiment?", curses.color_pair(1))
    screen.addstr(13, 12, "Press [ENTER] For YES. Press [0] To Skip.", curses.color_pair(1))
    screen.addstr(17, 12, "Social Media Takes Up More Of My Time Than I Would Like", curses.A_STANDOUT)
    screen.getch()
    screen.clear()
    screen.addstr(12, 12, "Do You Agree With The Following Sentiment?", curses.color_pair(1))
    screen.addstr(13, 12, "Press [ENTER] For YES. Press [0] To Skip.", curses.color_pair(1))
    screen.addstr(18, 12, "I THINK I HAVE A PROBLEM", curses.A_BLINK)
    screen.getch()
    curses.endwin()
    execute_cmd("clear")
    raw_input("Press [ENTER] To Have Your Results Algorithmically Analyzed")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.2)
    print("Processing...")
    time.sleep(1)
    print("")
    print("")
    print("")
    print("Complete.")
    raw_input("Your custom Application is ready. Press [ENTER]")
    time.sleep(.4)
    print("")
    print("Your code is: ")
    print(randint(0,1000))
    raw_input("Press Enter")
    #execute_cmd("mkdir Volumes/USB_name/ClientName")
    #execute_cmd("cp /path/to/randomNumVideo.mp4 Volumes/USB-name/ClientName/neurosOS")
    execute_cmd("mplayer -noconsolecontrols om.mp3 2>&- 1>/dev/null &")
  elif x == ord('2'):
    curses.endwin()
    execute_cmd("cat /Users/2sman/Documents/ART_PROJECTS/NeurosOS/fineprint.txt")
    raw_input("Press Enter")
  elif x == ord('3'):
    curses.endwin()
    execute_cmd("cal -y 2016")
    raw_input("Press Enter")

curses.endwin()
execute_cmd("clear")
