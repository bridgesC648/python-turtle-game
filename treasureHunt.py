#--------------------------------- Super Turtle Treasure Hunt -------------------------------------#
# Name: Christopher Bridges
#
# Course: CSCI 1470
#
# Assignment: CS1 Final Project
#--------------------------------------------------------------------------------------------------#
#DOCUMENTATION
#--------------------------------------------------------------------------------------------------#
# CONTENTS
# 1. Description
# 2. Modules
# 3. Game Modes
# 4. Difficulty Settings
# 5. Function List
# 6. Pseudocode
#--------------------------------------------------------------------------------------------------#
# DESCRIPTION
#--------------------------------------------------------------------------------------------------#
# A game with turtles, all about finding treasures.
#
#--------------------------------------------------------------------------------------------------#
# MODULES
#--------------------------------------------------------------------------------------------------#
# turtle:   Turtle graphics. Allows the use of turtles. 
#
# random:   Implements pseudo-random number generation for various distributions.
#
# time:     Provides various time-related functions.
#
# math:     Provides access to the mathematical functions defined by the C standard.
#
# winsound: Provides access to the basic sound-playing machinery provided by Windows platforms.
#--------------------------------------------------------------------------------------------------#
# GAME MODES
#--------------------------------------------------------------------------------------------------#
# Select from Classic, Timed, or Adventure.
#
# Classic:   Find three treasures. Don't fall in too many holes.
# Timed:     Find treasures until time runs out.
#
#--------------------------------------------------------------------------------------------------#
# DIFFICULTY
#--------------------------------------------------------------------------------------------------#
# Easy, Normal, and Hard modes provide different challenges.
#
# Easy:   No hazards. Very sensitive hot/cold functionality. Large treasures. Game continues
#         until all treasures are found or time runs out. 1.5 mins timed mode. Easy difficulty
#         Timed mode does not register high scores.
#
# Normal: 1:1 Treasure:Hazard ratio. Hazards stop appearing after 3 are encountered.
#         Moderately senstive hot/cold function. Medium sized treasures. Timed mode score
#         multiplier x2. Game continues until all treasures are found, or time runs out. 
#
# Hard:   1:2 Treasure:Hazard ratio. Always 2 active hazards. Small treasures. Insensitive
#         hot/cold function. Timed mode score multiplier x5. Game continues until either
#         all treasures are found (classic) or time runs out, or player loses 3 lives.
#
#--------------------------------------------------------------------------------------------------#
# FUNCTION LIST
#--------------------------------------------------------------------------------------------------#
# List of functions and brief descriptions, in alphabetical order.
#
# backToStart:      Resets window to default start menu.
# bindArrows:       Binds arrow keys to function calls.
# bindKeys:         Binds the ASDW keys to movement functions.
# checkForTreasuresAndHoles:    Checks for treasures and holes. 
# checkHighScore:   Determines whether the player's current score belongs in the high score list.
# displayScore:     Displays score message.
# distance:         Computes distance between two points.
# dWrite:           Tells dWriter turtle to write current environment to screen.
# endClassic:       Perform functions related to ending a classic game.
# endIntro:         Interrupts opening and cuts straight to starting menu.
# endTime:          Perform functions related to ending a timed game.
# eWrite:           Tells eWriter turtle to write current environment to screen.
# foundHole:        Called when turtle encounters a hazard.
# foundTreasure:    Called when a treasure is found. Either spawns a new treasure, or ends classic mode.
# generateHazards:  Makes new hazards.
# generateTreasure: Makes new treasures.        
# goBk:             Moves turtle backward when 'S' key is pressed. Also performs main game loop.
# goFd:             Moves turtle forward when 'W' key is pressed. Also performs main game loop.
# hotCold:          Changes turtle color based on distance to treasure.
# keepScore:        Computes score based on treasures found and difficulty setting.
# left:             Turns turtle to the left when 'A' key is pressed.
# menuMove:         Moves the cursor from one menu location to another and updates descriptive menu text
# modeWrite:        Tells modeWriter turtle to write the current mode to screen.
# moveCursorDown:   Moves menu cursor down.
# moveCursorLeft:   Moves menu cursor to the left.
# moveCursorRight:  Moves menu cursor to the right.
# moveCursorUp:     Moves menu cursor up.
# newClassic:       Starts a new classic-mode game.
# newTimed:         Starts a new timed-mode game.
# playIntroduction: Starts the opening animation.
# recordInsert:     Inserts a new record into its proper place in the high score list. Update highscores.txt.
# resetSpeed:       Sets the turtle's speed modifier to 1.
# resetTurtle:      Returns turtle to origin.
# right:            Turns turtle to the right when 'D' key is pressed.
# screenTransition: Transitions to the game over screen.
# select:           Make menu selections / controls spacebar functionality.
# setDifficulty:    Sets difficulty-related variable values. 
# setPosition:      Prompts user to enter coordinates for turtle, then moves. For demonstration purposes.
# stampTreasure:    Stamps a treasure location.
# stopMoving:       Sets variable "moving" to False when "W" or "S" key is released. (stops main loop)
# stopTurning:      Sets variable "turning" to False when "A" or "D" key is released.
# turtleBlink:      Turtle blinks briefly then remains visible.
# turtleBoost:      May give turtle a speed boost when encountering a treasure.
# turtleFall:       Drop turtle in a hole.
# turtleSpawn:      Puts the turtle on/back on the map.
# unbindArrows:     Remove arrow keys from function calls.
# unbindKeys:       Unbinds ASDW from movement functions.
# writeHighScores:  Writes the high score list to screen
#
#--------------------------------------------------------------------------------------------------#
# PSEUDOCODE
#--------------------------------------------------------------------------------------------------#
#
#------------------------------------
# MAIN PROGRAM
#------------------------------------
# Import necessary modules
# Define all of the functions.
# Set up menu coordinates list.
# Create screen and set its attributes.
# Register shape 'treasureStamp'
# Initialize game variables to default values
# Create all of the turtles and set their attributes
# Create the high scores list from highscores.txt:
#       open highscores.txt
#       split by line into tempList
#       initialize empty list 'highScoreList'
#       split each line by tab
#       cast index 1 to integer
#       call recordInsert to place record into highScoreList
# Close file
# Set keypress and keyrelease events for non-ASDW keys
# Print basic instructions to shell
# Tell screen to listen for keypresses.
# Call playIntroduction() to display opening animation
#
#------------------------------------
# MAIN LOOP PSEUDO CODE
#------------------------------------
# Is executed when the goFd or goBk function is called. Bound to key events. This loop basically
# executes over and over again until the game ends. 
#
#------------------------------------
# goFd():
#------------------------------------
# Declare 'moving' as global variable
# Unbind goFd() from 'w' key.
# Set moving to True
# while moving True and gameOver False:
#       if turningRight:
#	    turn right
#	    go forward
#	elif turningLeft:
#	    turn left
#	    go forward
#	else:
#	    go forward
#	Call hotCold to update turtle color
#	Call checkForTreasuresAndHoles to do that.
#
#------------------------------------
# checkForTreasuresAndHoles():
#------------------------------------
# Declare treasures, tx, ty, r as globals
# If not easy mode:
#	Check each hazard to see if you fell into one.
#	If you did, call foundHole()
# Once that's done, if you haven't lost the game:
#	Check distance to treasure.
#	If distance < treasure radius r:
#	    stampTreasure()
#	    treasures +1
#	    play gotchest.wav
#	    call foundTreasure()
#
#------------------------------------
# foundHole(hazardTuple):
#------------------------------------
# declare relevant variables as globals
# decrement lives
# put turtle in middle of hazard.
# call turtleFall(hazardTuple)
# if lives <= 0 and mode == 'classic':
#	gameOver <- True
#	moving <- False
#	unbind keys from movement
#	call screenTransition after 1000ms
# else:
#	try to remove hazardTuple from hazardList
#	If unable, print a message to shell.
#	make new hazard
#	clear hole
# 	respawn turtle
#
#------------------------------------
# foundTreasure():
#------------------------------------
# Declare relevant variables as globals
# if classic mode:
#	if treasures < 3:
#	    turtleBoost
#	    make new treasure
#	    hotCold
#	else:
#	    unbindKeys from movement
#	    gameOver <- True
#	    moving <- False
#	    call endClassic after 1500 ms
# elif timed mode:
#       update onscreen score
#	turtleboost
#	make new treasure
#	hotcold
#
#--------------------------------------------------------------------------------------------------#
# PLANNED FEATURES
#--------------------------------------------------------------------------------------------------#
# - ADVENTURE: I swear I'm going to do this. It's gonna be reaaallyyyy simple, but I'm gonna do it.
#              Eventually. On my own, probably after this class is over...
#--------------------------------------------------------------------------------------------------#

# Screen List:
# start_menu
# tutorial
# classic_game
# victory
# game_over
# timed_game
# mode_select
# settings
# high_scores
# credits

from turtle import *
from random import *
from time import *
from math import *
from winsound import *

# MAIN GAME LOOP FUNCTIONS #

def checkForTreasuresAndHoles():
    global treasures, tx, ty, r
    if difficulty != 'easy':
        for h in hazardList:
            if kame.distance(h) < hr:
                foundHole(h)          
    if gameOver == False:            
        if kame.distance(tx,ty) <= r:
            stampTreasure(tx,ty,r)
            treasures += 1
            PlaySound('sounds\\gotchest.wav', SND_FILENAME | SND_ASYNC )
            foundTreasure()
            
def foundTreasure():
    ''' Do this if a treasure is found. '''
    global treasures, r, tx, ty, gameOver, moving
    if mode == 'classic':            
        if treasures < 3:
            turtleBoost()
            r, tx, ty = generateTreasure()
            hotCold()
        else:
            unbindKeys()
            gameOver = True
            moving = False
            wn.ontimer(endClassic, 1500)      
    elif mode == 'timed':
        scoreKeeper.clear()
        scoreKeeper.write(treasures, font=('Bauhaus 93', 36, 'normal'))
        turtleBoost()
        r, tx, ty = generateTreasure()
        hotCold()

def foundHole(hazardTuple):
    ''' What happens when you fall in a hole '''
    global lives, gameOver, moving
    lives -= 1
    kame.setpos(hazardTuple)
    turtleFall(hazardTuple)
    if lives <= 0 and mode == 'classic':
        gameOver = True
        moving = False
        unbindKeys()
        wn.ontimer(screenTransition, 1000)
    else:
        try:
            hazardList.remove(hazardTuple)
        except ValueError:
            print("Tried to remove hazard, but it was already gone...")            
        generateHazards()
        holey.clear()
        turtleSpawn()

#---------- Movement ----------#
def goFd():
    ''' Move turtle forward when 'w' key is pressed. '''
    global moving
    onkeypress(None, 'w') # Keep holding it, if you want.
    moving = True   
    while moving == True and gameOver == False:
        if turningRight == True:
            kame.rt(4*speedmod)
            kame.fd(10*speedmod)
        elif turningLeft == True:
            kame.lt(4*speedmod)
            kame.fd(10*speedmod)
        else:
            kame.fd(5*speedmod)
        hotCold()
        checkForTreasuresAndHoles()

def goBk():
    ''' Move turtle backward when 's' key is pressed. '''
    global moving
    onkeypress(None, 's')
    moving = True
    while moving == True and gameOver == False:
        if turningRight == True:
            kame.rt(4*speedmod)
            kame.bk(10*speedmod)
        elif turningLeft == True:
            kame.lt(4*speedmod)
            kame.bk(10*speedmod)
        else:
            kame.bk(5*speedmod)
        hotCold()
        checkForTreasuresAndHoles()
        
def left():
    ''' Rotates the turtle left when 'a' key is pressed. '''
    global turningLeft, wasntMoving, stopSpinning
    wn.onkeypress(None, 'a')
    turningLeft = True
    if moving == False:         # If turtle isn't moving when the key is pressed.
        stopSpinning = False     # We want it to still turn. 
        wasntMoving = True      # This is for if we start moving while still turrning.
        while stopSpinning == False:
            kame.lt(5)

def right():
    ''' rotates the turtle right when 'd' is pressed '''
    global turningRight, wasntMoving, stopSpinning
    wn.onkeypress(None, 'd')
    turningRight = True
    if moving == False:
        stopSpinning = False
        wasntMoving = True
        while stopSpinning == False:
            kame.rt(5)
    
def stopMoving():
    ''' Stops moving forward when 'w' or 's' is released. '''
    global moving
    onkeypress(goFd, 'w')
    onkeypress(goBk, 's')
    moving = False
    if turningRight == True:
        right()
    elif turningLeft == True:
        left()

def stopTurning():
    ''' stops turning '''
    global turningLeft, turningRight, wasntMoving, stopSpinning
    wn.onkeypress(left, 'a')
    wn.onkeypress(right, 'd')
    if turningLeft == True:
        turningLeft = False
    elif turningRight == True:
        turningRight = False
    if wasntMoving == True:
        wasntMoving = False
        stopSpinning = True
#-------------------- Menu Navigation  --------------------#
def goBack():
    ''' Should never have been necessary but whatever. '''
    global activeScreen
    activeScreen = 'settings'
    wn.bgpic('images\\settings.png')
    eWrite()
    dWrite()
    menuMove('settings_RESET_HIGH_SCORES', 'Reset the high score list')
    # Why is this necessary it makes no freaking sense
    # I know why now, but I'm too lazy to change it. 

def unbindArrows():
    ''' unbinds arrow keys during a game is in progress. '''
    for direction in ['Up', 'Down', 'Left', 'Right']:
        onkeypress(None, '{}'.format(direction))
        
def bindArrows():
    ''' Binds arrow keys back to cursor movement when a game is over. '''
    onkeypress(moveCursorUp, 'Up')
    onkeypress(moveCursorDown, 'Down')
    onkeypress(moveCursorLeft, 'Left')
    onkeypress(moveCursorRight, 'Right')

def unbindKeys():
    ''' Stops player from moving. '''
    for k in ['a', 's', 'd', 'w']:
        onkeypress(None, '{}'.format(k))
        onkeyrelease(None, '{}'.format(k))

def bindKeys():
    ''' Lets the player move again.'''
    onkeypress(left, 'a')
    onkeyrelease(stopTurning, 'a')
    onkeypress(goBk, 's')
    onkeyrelease(stopMoving, 's')
    onkeypress(right, 'd')
    onkeyrelease(stopTurning, 'd')
    onkeypress(goFd, 'w')
    onkeyrelease(stopMoving, 'w')
    
def menuMove(cursorDestination, descriptiveText):
    ''' Moves the cursor from one menu option to another, and updates
        the descriptive menu text to match that option. '''
    cursor.ht()
    if 'start_menu' in cursorDestination:
        writey.setpos(menuCoords['start_menu_TEXT'])
        if cursorDestination == 'start_menu_START':
            cursor.setheading(180)
        elif cursor.heading() != 0:
            cursor.setheading(0)
    elif cursorDestination == 'settings_ENVIRONMENT':
        cursor.setheading(0)
    PlaySound('sounds\\menumove.wav', SND_FILENAME | SND_ASYNC )
    #Beep(500, 100)
    cursor.setpos(menuCoords[cursorDestination])
    writey.clear()
    writey.write('{}'.format(descriptiveText), move=False, align='center', font=('Ariel', 18, 'normal'))
    cursor.st()

def modeWrite():
    ''' Directs the modeWrite turtle to change the mode upon selection. '''
    modeWriter.clear()
    modeWriter.write('{}'.format(mode), move=False, align='center', font=('Bauhaus 93', 18, 'normal'))

def eWrite():
    ''' Directs the eWriter turtle to write the currently selected environment.'''
    eWriter.clear()
    eWriter.write('{}'.format(environment), move=False, align='center', font=('Bauhaus 93', 18, 'normal'))
    
def dWrite():
    ''' Directs the dWriter turtle to write the currently selected difficulty.'''
    dWriter.clear()
    dWriter.write('{}'.format(difficulty), move=False, align='center', font=('Bauhaus 93', 18, 'normal'))

def moveCursorRight():
    ''' Moves cursor horizontally when applicable. '''
    if activeScreen == 'start_menu':
        if cursor.pos() == menuCoords['start_menu_MODE']:
            menuMove('start_menu_START', 'Start the game!')
        else:
            menuMove('start_menu_MODE', 'Select a mode of play')
			
    elif activeScreen == 'settings_environment':
        if cursor.pos() == menuCoords['settings_environment_FOREST']:
            wn.bgpic('images\\settings_environments_beach.png')
            menuMove('settings_environment_BEACH', 'Select a beach environment')
        elif cursor.pos() == menuCoords['settings_environment_BEACH']:
            wn.bgpic('images\\settings_environments_underwater.png')
            menuMove('settings_environment_UNDERWATER', 'Select an underwater environment')
        elif cursor.pos() == menuCoords['settings_environment_UNDERWATER']:
            wn.bgpic('images\\settings_environments_forest.png')
            menuMove('settings_environment_FOREST', 'Select a forest environment')

    elif activeScreen == 'settings_difficulty':
        if cursor.pos() == menuCoords['settings_difficulty_EASY']:
            wn.bgpic('images\\settings_difficulty_normal.png')
            menuMove('settings_difficulty_NORMAL', '')
        elif cursor.pos() == menuCoords['settings_difficulty_NORMAL']:
            wn.bgpic('images\\settings_difficulty_hard.png')
            menuMove('settings_difficulty_HARD', '')
        elif cursor.pos() == menuCoords['settings_difficulty_HARD']:
            wn.bgpic('images\\settings_difficulty_easy.png')
            menuMove('settings_difficulty_EASY', '')

    elif activeScreen == 'settings_reset_high_scores':
        if cursor.pos() == menuCoords['settings_reset_high_scores_YES']:
            menuMove('settings_reset_high_scores_NO', '')
        else:
            menuMove('settings_reset_high_scores_YES', '')

    elif activeScreen == 'game_over':
        if cursor.pos() == menuCoords['game_over_PLAY_AGAIN?']:
            menuMove('game_over_BACK', '')
        else:
            menuMove('game_over_PLAY_AGAIN?', '')

def moveCursorLeft():
    ''' Move cursor left '''
    if activeScreen == 'start_menu':
        if cursor.pos() == menuCoords['start_menu_MODE']:
            menuMove('start_menu_START', 'Start the game!')
        else:
            menuMove('start_menu_MODE', 'Selecta  mode of play')

    elif activeScreen == 'settings_environment':
        if cursor.pos() == menuCoords['settings_environment_FOREST']:
            wn.bgpic('images\\settings_environments_underwater.png')
            menuMove('settings_environment_UNDERWATER', 'Select an underwater environment')
        elif cursor.pos() == menuCoords['settings_environment_UNDERWATER']:
            wn.bgpic('images\\settings_environments_beach.png')
            menuMove('settings_environment_BEACH', 'Select a beach environment')
        else:
            wn.bgpic('images\\settings_environments_forest.png')
            menuMove('settings_environment_FOREST', 'Select a forest environment')

    elif activeScreen == 'settings_difficulty':
        if cursor.pos() == menuCoords['settings_difficulty_EASY']:
            wn.bgpic('images\\settings_difficulty_hard.png')
            menuMove('settings_difficulty_HARD', '')
        elif cursor.pos() == menuCoords['settings_difficulty_HARD']:
            wn.bgpic('images\\settings_difficulty_normal.png')
            menuMove('settings_difficulty_NORMAL', '')
        elif cursor.pos() == menuCoords['settings_difficulty_NORMAL']:
            wn.bgpic('images\\settings_difficulty_easy.png')
            menuMove('settings_difficulty_EASY', '')
            
    elif activeScreen == 'settings_reset_high_scores':
        if cursor.pos() == menuCoords['settings_reset_high_scores_YES']:
            menuMove('settings_reset_high_scores_NO', '')
        else:
            menuMove('settings_reset_high_scores_YES', '')

    elif activeScreen == 'game_over':
        if cursor.pos() == menuCoords['game_over_PLAY_AGAIN?']:
            menuMove('game_over_BACK', '')
        elif cursor.pos() == menuCoords['game_over_BACK']:
            menuMove('game_over_PLAY_AGAIN?', '')

def moveCursorDown():
    ''' Determines what happens when the Down keyboard arrow is
        pressed on a menu screen. '''
    if activeScreen == 'start_menu':
        if cursor.pos() == menuCoords['start_menu_MODE']:
            menuMove('start_menu_HIGH_SCORES', 'View high score list')            
        elif cursor.pos() == menuCoords['start_menu_HIGH_SCORES']:
            menuMove('start_menu_SETTINGS', 'Adjust game settings')            
        elif cursor.pos() == menuCoords['start_menu_SETTINGS']:
            menuMove('start_menu_TUTORIAL', 'How to play the game')            
        elif cursor.pos() == menuCoords['start_menu_TUTORIAL']:
            menuMove('start_menu_CREDITS', 'Credits and acknowledgements')
        elif cursor.pos() == menuCoords['start_menu_CREDITS']:
            menuMove('start_menu_EXIT', 'Quit the game')
        elif cursor.pos() == menuCoords['start_menu_EXIT']:
            menuMove('start_menu_MODE', 'Select a mode of play')
        elif cursor.pos() == menuCoords['start_menu_START']:
            menuMove('start_menu_HIGH_SCORES', 'View high score list')

    elif activeScreen == 'mode_select':
        if cursor.pos() == menuCoords['mode_select_CLASSIC']:
            menuMove('mode_select_TIMED', 'Find treasures for one minute')
        elif cursor.pos() == menuCoords['mode_select_TIMED']:
            menuMove('mode_select_ADVENTURE', 'Go on a treasure-finding adventure!')
        else:
            menuMove('mode_select_CLASSIC', 'Find three treasures with no time limit')

    elif activeScreen == 'settings':
        if cursor.pos() == menuCoords['settings_ENVIRONMENT']:
            menuMove('settings_DIFFICULTY', 'Adjust difficulty')
        elif cursor.pos() == menuCoords['settings_DIFFICULTY']:
            menuMove('settings_RESET_HIGH_SCORES', 'Reset the high score list')
        elif cursor.pos() == menuCoords['settings_RESET_HIGH_SCORES']:
            menuMove('settings_BACK', 'Go back to the main menu')
        else:
            menuMove('settings_ENVIRONMENT', 'Choose your environment')

    elif activeScreen == 'victory':
        if cursor.pos() == menuCoords['victory_PLAY_AGAIN?']:
            menuMove('victory_BACK', '')
        elif cursor.pos() == menuCoords['victory_BACK']:
            cursor.ht()
            cursor.setpos(menuCoords['victory_EXIT'])
            cursor.st()
        else:
            cursor.ht()
            cursor.setpos(menuCoords['victory_PLAY_AGAIN?'])
            cursor.st()
            
def moveCursorUp():
    ''' Determines what happens when the Up keyboard arrow is
        pressed on a menu screen. '''
    if activeScreen == 'start_menu':
        if cursor.pos() == menuCoords['start_menu_MODE']:
            menuMove('start_menu_EXIT', 'Quit the game')
        elif cursor.pos() == menuCoords['start_menu_EXIT']:
            menuMove('start_menu_CREDITS', 'Credits and acknowledgements')
        elif cursor.pos() == menuCoords['start_menu_CREDITS']:
            menuMove('start_menu_TUTORIAL', 'How to play the game')
        elif cursor.pos() == menuCoords['start_menu_TUTORIAL']:
            menuMove('start_menu_SETTINGS', 'Adjust game settings')
        elif cursor.pos() == menuCoords['start_menu_SETTINGS']:
            menuMove('start_menu_HIGH_SCORES', 'View high score list')
        elif cursor.pos() == menuCoords['start_menu_HIGH_SCORES']:
            menuMove('start_menu_MODE', 'Select a mode of play')
        elif cursor.pos() == menuCoords['start_menu_START']:
            menuMove('start_menu_EXIT', 'Quit the game')

    elif activeScreen == 'mode_select':
        if cursor.pos() == menuCoords['mode_select_CLASSIC']:
            menuMove('mode_select_ADVENTURE', 'Go on a treasure finding adventure!')
        elif cursor.pos() == menuCoords['mode_select_ADVENTURE']:
            menuMove('mode_select_TIMED', 'Find treasures for one minute')
        else:
            menuMove('mode_select_CLASSIC', 'Find three treasures with no time limit')

    elif activeScreen == 'settings':
        if cursor.pos() == menuCoords['settings_ENVIRONMENT']:
            menuMove('settings_BACK', 'Go back to the main menu')
        elif cursor.pos() == menuCoords['settings_BACK']:
            menuMove('settings_RESET_HIGH_SCORES', 'Reset the high score list')
        elif cursor.pos() == menuCoords['settings_RESET_HIGH_SCORES']:
            menuMove('settings_DIFFICULTY', 'Adjust difficulty')
        else:
            menuMove('settings_ENVIRONMENT', 'Choose your environment')
                     
    elif activeScreen == 'victory':
        if cursor.pos() == menuCoords['victory_PLAY_AGAIN?']:
            cursor.ht()
            cursor.setpos(menuCoords['victory_EXIT'])
            cursor.st()
        elif cursor.pos() == menuCoords['victory_EXIT']:
            cursor.ht()
            cursor.setpos(menuCoords['victory_BACK'])
            cursor.st()
        else:
            cursor.ht()
            cursor.setpos(menuCoords['victory_PLAY_AGAIN?'])
            cursor.st()

########################################################################################################
#------------------------------------- HERE'S THE SELECT FUNCTION -------------------------------------#
########################################################################################################
def select():
    ''' Determines what happens when the Spacebar is pressed. '''
    global activeScreen, r, tx, ty, mode, environment, background, difficulty, highScoreList
    
    # START MENU SELECTIONS:
    if activeScreen == 'start_menu':
        if cursor.pos() == menuCoords['start_menu_MODE']:
            activeScreen = 'mode_select'
            writey.clear()
            modeWriter.clear()
            wn.bgpic('images\\mode_select.png')
            menuMove('mode_select_CLASSIC', 'Find treasures with no time limit')
        elif cursor.pos() == menuCoords['start_menu_START']:
            if mode == 'classic':
                newClassic()
            elif mode == 'timed':
                newTimed()
        elif cursor.pos() == menuCoords['start_menu_HIGH_SCORES']:
            activeScreen = 'high_scores'
            cursor.ht()
            writey.clear()
            modeWriter.clear()
            wn.bgpic('images\\high_scores.png')
            writeHighScores()

        elif cursor.pos() == menuCoords['start_menu_SETTINGS']:
            activeScreen = 'settings'
            cursor.ht()
            modeWriter.clear()
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            writey.clear()
            writey.setpos(menuCoords['settings_TEXT'])
            menuMove('settings_ENVIRONMENT', 'Choose your environment.')

        elif cursor.pos() == menuCoords['start_menu_TUTORIAL']:
            activeScreen = 'tutorial'
            cursor.ht()
            modeWriter.clear()
            writey.clear()
            wn.bgpic('images\\how_to_play.png')

        elif cursor.pos() == menuCoords['start_menu_CREDITS']:
            activeScreen = 'credits'
            cursor.ht()
            modeWriter.clear()
            writey.clear()
            wn.bgpic('images\\credits.png')

        elif cursor.pos() == menuCoords['start_menu_EXIT']:
            wn.bye()
                
    # MODE SCREEN SELECTIONS
    elif activeScreen == 'mode_select':
        if cursor.pos() == menuCoords['mode_select_CLASSIC']:
            mode = 'classic'
        elif cursor.pos() == menuCoords['mode_select_TIMED']:
            mode = 'timed'
        else:
            mode = 'adventure'
        writey.clear()
        menuMove('start_menu_START', 'Start the game!')
        wn.bgpic('images\\start_menu.png')
        modeWrite()
        activeScreen = 'start_menu'

    # HIGH SCORE SCREEN
    elif activeScreen == 'high_scores':
        activeScreen = 'start_menu'
        wn.bgpic('images\\start_menu.png')
        backToStart()
#----------------------------- SETTINGS SCREEN STUFF -----------------------------#
    # SETTINGS MAIN MENU #
    elif activeScreen == 'settings':
        if cursor.pos() == menuCoords['settings_ENVIRONMENT']:
            activeScreen = 'settings_environment'
            cursor.ht()
            eWriter.clear()
            dWriter.clear()
            wn.bgpic('images\\settings_environments_forest.png')
            cursor.setheading(90)
            menuMove('settings_environment_FOREST', 'Select a forest environment.')

        elif cursor.pos() == menuCoords['settings_DIFFICULTY']:
            activeScreen = 'settings_difficulty'
            cursor.ht()
            eWriter.clear()
            dWriter.clear()
            wn.bgpic('images\\settings_difficulty_normal.png')
            cursor.setheading(90)
            menuMove('settings_difficulty_NORMAL', '')

        elif cursor.pos() == menuCoords['settings_RESET_HIGH_SCORES']:
            activeScreen = 'settings_reset_high_scores'
            cursor.ht()
            dWriter.clear()
            eWriter.clear()
            writey.clear()
            wn.bgpic('images\\reset_high_scores.png')
            cursor.setpos(menuCoords['settings_reset_high_scores_YES'])
            cursor.st()

        elif cursor.pos() == menuCoords['settings_BACK']:
            activeScreen = 'start_menu'
            wn.bgpic('images\\start_menu.png')
            backToStart()

    # SETTINGS ENVIRONMENT MENU #
    elif activeScreen == 'settings_environment':
        if cursor.pos() == menuCoords['settings_environment_FOREST']:
            background = 'images\\forest.png'
            environment = 'forest'
            writey.clear()
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            menuMove('settings_ENVIRONMENT', 'Choose your environment.')
            activeScreen = 'settings'
        elif cursor.pos() == menuCoords['settings_environment_BEACH']:
            background = 'images\\beach.png'
            environment = 'beach'
            writey.clear()
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            menuMove('settings_ENVIRONMENT', 'Choose your environment.')
            activeScreen = 'settings'
        elif cursor.pos() == menuCoords['settings_environment_UNDERWATER']:
            background = 'images\\underwater.png'
            environment = 'underwater'
            writey.clear()
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            menuMove('settings_ENVIRONMENT', 'Choose your environment.')
            activeScreen = 'settings'

    # SETTINGS DIFFICULTY MENU #
    elif activeScreen == 'settings_difficulty':
        if cursor.pos() == menuCoords['settings_difficulty_EASY']:
            difficulty = 'easy'
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            cursor.setheading(0)
            menuMove('settings_DIFFICULTY', 'Adjust difficulty')
            activeScreen = 'settings'
        elif cursor.pos() == menuCoords['settings_difficulty_NORMAL']:
            difficulty = 'normal'
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            cursor.setheading(0)
            menuMove('settings_DIFFICULTY', 'Adjust difficulty')
            activeScreen = 'settings'
        elif cursor.pos() == menuCoords['settings_difficulty_HARD']:
            difficulty = 'hard'
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            cursor.setheading(0)
            menuMove('settings_DIFFICULTY', 'Adjust difficulty')
            activeScreen = 'settings'
  
    # SETTINGS RESET HIGH SCORES #
    elif activeScreen == 'settings_reset_high_scores':
        if cursor.pos() == menuCoords['settings_reset_high_scores_YES']:
            hs = open('highscores.txt', 'w')
            hs.close()
            highScoreList = []
            cursor.ht()
            wn.bgpic('images\\reset_done.png')
            wn.ontimer(goBack, 1000)
        elif cursor.pos() == menuCoords['settings_reset_high_scores_NO']:
            activeScreen = 'settings'
            wn.bgpic('images\\settings.png')
            eWrite()
            dWrite()
            menuMove('settings_RESET_HIGH_SCORES', 'Reset the high score list')
#----------------------------------END SETTING SCREEN STUFF------------------------------------#          
    # TUTORIAL SCREEN FUNCTIONALITY
    elif activeScreen == 'tutorial':
        wn.bgpic('images\\start_menu.png')
        modeWrite()
        activeScreen = 'start_menu'
        cursor.setpos(menuCoords['start_menu_TUTORIAL'])
        cursor.st()

    # CREDITS SCREEN FUNCTIONALITY
    elif activeScreen == 'credits':
        wn.bgpic('images\\start_menu.png')
        modeWrite()
        activeScreen = 'start_menu'
        cursor.setpos(menuCoords['start_menu_CREDITS'])
        cursor.st()
        
    # VICTORY SCREEN SELECTIONS (NEED UPDATE)    
    elif activeScreen == 'victory':
        if cursor.pos() == menuCoords['victory_PLAY_AGAIN?']:
            if mode == 'classic':
                newClassic()
            elif mode == 'timed':
                newTimed()
        elif cursor.pos() == menuCoords['victory_BACK']:
            cursor.ht()
            sketchy.clear()
            scoreKeeper.clear()
            wn.bgpic('images\\start_menu.png')
            activeScreen = 'start_menu'
            cursor.setpos(menuCoords['start_menu_MODE'])
            cursor.st()
            backToStart()
        elif cursor.pos() == menuCoords['victory_EXIT']:
            wn.bye()

    # GAME OVER SCREEN SELECTIONS
    elif activeScreen == 'game_over':
        if cursor.pos() == menuCoords['game_over_PLAY_AGAIN?']:
            # You don't get game-over in Timed mode.
            newClassic()
        elif cursor.pos() == menuCoords['game_over_BACK']:
            cursor.ht()
            sketchy.clear()
            scoreKeeper.clear()
            wn.bgpic('images\\start_menu.png')
            activeScreen = 'start_menu'
            cursor.setpos(menuCoords['start_menu_MODE'])
            cursor.st()
            backToStart()
    # INTRO ANIMATION
    elif activeScreen == 'introduction':
        ''' Breaks the intro out of its animation loops and goes on. '''
        activeScreen = 'start_menu'
            
#--------- Turtle Functions ----------#
def setPosition():
    ''' So the position of the turtle can be set manually for
        demonstration purposes. '''
    newX = int(wn.textinput("Enter new X", "Enter new X coordinate:"))
    newY = int(wn.textinput("Enter new Y", "Enter new Y coordinate:"))
    kame.setpos(newX, newY)
    wn.listen()

def resetTurtle():
    ''' Returns turtle to the origin. '''
    kame.setpos(0,0)

def hotCold():
    ''' Checks turtle's distance and changes its color. '''
    distance = kame.distance(tx, ty)
    if distance > maxx:
        kame.color(0,0,255)
    elif distance > minn:
        ratio = (distance - minn) / (maxx - minn)
        color = int(ratio*1023)
        if color > 767: # 767 = 256*3 - 1
            color = color - 767
            kame.color(0,256-color,255)
        elif color > 511: # 256*2 - 1
            kame.color(0,255,color-512)
        elif color > 255:
            color = color - 255
            kame.color(256-color,255,0)
        else:
            kame.color(255,color,0)
    else:
        kame.color(255,0,0)

def resetSpeed():
    ''' Called a short time after turtleBoost() to reset the speed '''
    global speedmod
    kame.clear()
    speedmod = 1
    kame.penup()

def turtleBoost():
    ''' Gives turtle a temporary speed boost '''
    global speedmod, speedmod
    outcome = randint(1,12)
    if 9 <= outcome <= 12:
        PlaySound('sounds\\boost.wav', SND_FILENAME | SND_ASYNC )
        speedmod = 2                 # Double movement.
        kame.pendown()               # RAINBOW TRAIL
        wn.ontimer(resetSpeed, 3000) # Reset after 3 seconds.
    
def turtleSpawn():
    ''' Called if turtle dies and game isn't over '''
    while kame.distance(tx,ty) < r + 10 or not all(kame.distance(h) > hr + 10 for h in hazardList):
        kame.setpos(randint(-225,225), randint(-225,225))
    turtleBlink()
    
def turtleFall(hazardTuple):
    ''' Drop kame in a hole! '''
    holey.setpos(hazardTuple)
    holey.stamp()
    PlaySound('sounds\\Blip003.wav', SND_FILENAME | SND_ASYNC )
    s = kame.pensize()
    kame.speed(4)
    while s > 0:
        kame.rt(36)
        s -= 1
        kame.pensize(s)
    kame.ht()
    kame.pensize(6)
    kame.speed('fastest')

def turtleBlink():
    ''' Turtle blinks then remains visible '''
    unbindKeys()
    i = .20
    while i >= 0:
        kame.st()
        sleep(i)
        kame.ht()
        sleep(i)
        i = i-.05
    kame.st()
    bindKeys()

#---------------- Game Control Functions -----------------#

def screenTransition():
    ''' Transitions to the game_over screen. '''
    kame.clear()
    holey.clear()
    sketchy.clear()
    for i in range(1, 21):
        wn.bgpic('images\\{}_go\\{}.png'.format(environment, i))
        wn.update()
        sleep(.016)
    endClassic()

def generateTreasure():
    ''' Sets the radius and location of a treasure.  '''
    radius = randint(rmin, rmax)
    centerx = randint(-250+radius, 225-radius)
    centery = randint(-250+radius, 225-radius)
    return radius, centerx, centery

def generateHazards():
    ''' Make a hole for the turtle to fall into. '''
    while len(hazardList) < numOfHazards:
        hx = tx+1
        hy = ty+1
        while distance(hx, hy, tx, ty) <= r+30 or kame.distance(hx,hy) <= hr + 30:
            hx=randint(-225, 225)
            hy=randint(-225, 225)
        hazardList.append((hx, hy))
    print(hazardList)

def setDifficulty():
    ''' Sets difficulty-related variables '''
    global time, diff_multiplier, minn, maxx, rmin, rmax, hr, numOfHazards, lives
    if difficulty == 'easy':
        time = 90000                # 1.5 mins to find treasures
        diff_multipler = 0          # No score accumulation
        minn = 20                   # Turtle red within 20 units
        maxx = 400                  # Turtle blue outside 400 units
        rmin = 30                   # treasure radius minimum
        rmax = 40                   # treasure radius maximum
    elif difficulty == 'normal':
        time = 60000            
        diff_multiplier = 2     
        minn = 40               
        maxx = 350              
        rmin = 20
        rmax = 30
        hr = 10
        numOfHazards = 1
        lives = 3
    elif difficulty == 'hard':
        time = 45000
        diff_multiplier = 4
        minn = 20
        maxx = 275
        rmin = 10
        rmax = 20
        hr = 20
        numOfHazards = 3
        lives = 3
            
def distance(x1, y1, x2, y2 ):
    ''' Computes distance from one point to another. '''
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

def stampTreasure(tx, ty, r):
    ''' Draws the treasure circle '''
    sketchy.penup()
    sketchy.setpos(tx, ty)
    sketchy.stamp()

def keepScore():
    ''' Increments the player's score based on current difficulty setting.
        Score is calculated by (# of treasures)*(difficulty multiplier) '''
    global score
    if difficulty == 'easy':
        m = 0
    elif difficulty == 'normal':
        m = 2
    elif difficulty == 'hard':
        m = 5
    score = treasures*m

def displayScore():
    ''' Displays the score on the screen. '''
    scoreKeeper.setpos(0,0)
    if environment == 'forest':
        scoreKeeper.color('white')
    elif environment == 'beach':
        scoreKeeper.color('black')
    else: scoreKeeper.color('white')
    if treasures == 0:
        scoreKeeper.write('You didn\'t find any treasures!\nBetter luck next time...', move=False, align='center', font=('Bauhaus 93', 25, 'normal'))
    elif treasures < 3:
        scoreKeeper.write('You found {} treasures!\nYou earned {} points. Not bad!'.format(treasures, score), move=False, align='center', font=('Bauhaus 93', 25, 'normal'))
    elif treasures < 6:
        scoreKeeper.write('You found {} treasures!\nYou earned {} points. Great job!'.format(treasures, score), move=False, align='center', font=('Bauhaus 93', 25, 'normal'))
    else:
        scoreKeeper.write('Holy cow!\nYou found {} treasures!\nYou earned {} points.\nYou\'re amazing!'.format(treasures, score), move=False, align='center', font=('Bauhaus 93', 25, 'normal'))
    sleep(2)
    scoreKeeper.clear()
    scoreKeeper.setpos(200,-225)

def endClassic():
    ''' Clear window, hide turtle, show victory or game over screen '''
    global activeScreen, hazardList
    moving = False
    hazardList = []
    holey.clear()
    sketchy.clear()
    kame.ht()
    if lives <= 0:
        activeScreen = 'game_over'
        wn.bgpic('images\\{}_go\\21.png'.format(environment))
        cursor.setheading(0)
        cursor.setpos(menuCoords['game_over_PLAY_AGAIN?'])
        cursor.st()
    else:
        activeScreen = 'victory'
        wn.bgpic('images\\victory.png')
        cursor.setheading(0)
        cursor.setpos(menuCoords['victory_PLAY_AGAIN?'])
        cursor.st()
    bindArrows()
    
def endTime():
    ''' Ends a timed game. '''
    global activeScreen, gameOver, treasures, hazardList
    hazardList = []
    gameOver = True
    sketchy.clear()
    holey.clear()
    scoreKeeper.clear()
    kame.ht()
    keepScore()
    displayScore()
    wn.bgpic('images\\victory.png')
    cursor.setheading(0)
    cursor.setpos(menuCoords['victory_PLAY_AGAIN?'])
    cursor.st()
    bindArrows()
    activeScreen = 'victory'
    
    if checkHighScore(score):
        yourInitials = wn.textinput("A new record!", "Please enter your initials: ").upper()
        if len(yourInitials) > 3:
            yourInitials = yourInitials[:3]
        recordInsert([yourInitials, score])
        wn.listen()

def newClassic():
    ''' Start a new classic mode game. '''
    global activeScreen, tx, ty, r, gameOver, mode, score, treasures, lives
    moving = False                      # WHY WOULD YOU BE MOVING AT THIS TIME STOP IT.
    lives = 3                           # Reset life count
    treasures = 0                       # Reset treasure count
    gameOver = False                    # Game's not over. It's just beginning.
    cursor.ht()                         # Hide the cursor.
    modeWriter.clear()                  # Clear mode writing.
    writey.clear()                      # Clear menu descriptive text.
    activeScreen = 'classic_game'       # Set active screen
    wn.bgpic(background)                # Change background
    setDifficulty()                     # set values of difficulty-related variables.
    unbindArrows()                      # Unbind arrow keys so they don't do anything, even though they SHOULDN'T.
    r, tx, ty = generateTreasure()      # Generate the first treasure.
    kame.setpos(tx+1, ty+1)             # Set turtle near treasure.
    while kame.distance(tx,ty) < r:     # Now move it somewhere else.
        kame.setpos(randint(-200,200), randint(-200,200)) # A randomly determined somewhere else.
    if difficulty != 'easy':            # If we're not in easy mode
        generateHazards()               # Generate some hazards
    turtleBlink()                       # Blink a bit
    hotCold()                           # Check position relative to treasure.
    bindKeys()                          # Bind movement to ASDW keys.

def newTimed():
    ''' Start a new timed mode game. '''
    global activeScreen, tx, ty, r, timesUp, score, treasures, gameOver, mode
    setDifficulty()         # Check difficulty and set variables approriately
    unbindArrows()          # Unbind the arrow keys so they don't do anything.
    gameOver = False
    score = 0
    treasures = 0
    cursor.ht()             # Lose the cursor
    modeWriter.clear()      # And the modeWriter
    writey.clear()          # In fact just get rid of all turtles drawings. 
    activeScreen = 'timed_game'
    wn.bgpic(background)
    scoreKeeper.write(score, move = False, align='center', font=('Bauhaus 93', 36, 'normal'))
    r, tx, ty = generateTreasure()
    kame.setpos(tx+1, ty+1)
    while kame.distance(tx,ty) < r:
        kame.setpos(randint(-200,200), randint(-200,200))
    if difficulty != 'easy':
        generateHazards()
    turtleBlink()
    hotCold()
    wn.ontimer(endTime, time)

def backToStart():
    ''' Resets cursors etc to start screen defaults '''
    menuMove('start_menu_MODE', 'Select a mode of play.')
    eWriter.clear()
    dWriter.clear()
    modeWrite()

def recordInsert(record):
    ''' Sorts a new record into the high score list and updates highscores.txt. '''
    if len(highScoreList) == 0:
        highScoreList.append(record)
    elif len(highScoreList) == 1:
        if record[1] > highScoreList[0][1]:
            highScoreList.append(record)
        else:
            highScoreList.insert(0, record)
    else:
        if record[1] < highScoreList[0][1]:
            highScoreList.insert(0, record)
        elif record[1] > highScoreList[-1][1]:
            highScoreList.append(record)
        else:
            for i in range(len(highScoreList) - 1):
                if highScoreList[i][1] <= record[1] <= highScoreList[i+1][1]:
                    highScoreList.insert(i+1, record)
                    break              
    # Only save the top 10 scores.                
    if len(highScoreList) > 10:
        while len(highScoreList)>10:
            highScoreList.pop(0)   
    # Update highscores.txt and close it
    hs = open('highscores.txt', 'w')
    for record in highScoreList:
        hs.write('{}\t'.format(record[0]))
        hs.write('{}\n'.format(record[1]))
    hs.close()

def checkHighScore(score)->bool:
    ''' See if the player's current score is a new record. '''
    if score == 0:
        return False
    elif highScoreList == []:
        return True
    elif len(highScoreList) < 10:
        return True
    elif score > highScoreList[0][1]:
        return True
    else:
        return False

def writeHighScores():
    ''' Writes the high score list onto the screen in an orderly fashion. '''
    writey.setpos(menuCoords['high_scores_START_WRITING'])
    y = writey.ycor()
    x = writey.xcor()
    for i in range(len(highScoreList)):
        writey.write('{}. {}'.format(i+1, highScoreList[-(i+1)][0]), align='center', font=('Bauhaus 93', 30, 'normal'))
        writey.setpos(-x, y)      
        writey.write('{}'.format(highScoreList[-(i+1)][1]), align='center', font=('Bauhaus 93', 30, 'normal'))
        y-=35
        writey.setpos(x,y)

def endIntro():
    ''' Stop the intro animation early. '''
    PlaySound(None, SND_FILENAME)
    wn.bgpic('images\\start_menu.png')
    cursor.st()
    writey.write('Select a mode of play.', move = False, align='center', font=('Ariel Black', 18, 'normal'))
    modeWrite()

def playIntroduction():
    ''' play intro animation '''
    global activeScreen
    while activeScreen == 'introduction':
        wn.bgcolor('black')
        for i in range(115,135):
            if activeScreen == 'introduction':
                wn.bgpic('images\\intro\\pythonlogo\\{}.png'.format(i))
                wn.update()
                sleep(.007)
            else:
                endIntro()
                return None
        sleep(1)
        for i in range(135, 150):
            if activeScreen == 'introduction':
                wn.bgpic('images\\intro\\words\\{}.png'.format(i))
                wn.update()
                sleep(.033)
            else:
                endIntro()
                return None
        sleep(3)
        for i in range(150, 157):
            if activeScreen == 'introduction':
                wn.bgpic('images\\intro\\wordfade\\{}.png'.format(i))
                wn.update()
                sleep(.033)
            else:
                endIntro()
                return None
        sleep(1)
        PlaySound('sounds\\slowsteps.wav', SND_FILENAME | SND_LOOP | SND_ASYNC )
        for i in range(1,115):
            if i == 46:
                PlaySound(None, SND_FILENAME)
            if i == 71:
                PlaySound('sounds\\openchest.wav', SND_FILENAME | SND_ASYNC )
            if i == 88:
                PlaySound('sounds\\gotchest.wav', SND_FILENAME | SND_ASYNC )
                sleep(.2)
            if i == 90:
                PlaySound('sounds\\faststeps.wav', SND_FILENAME | SND_LOOP | SND_ASYNC )
            if i == 108:
                PlaySound(None, SND_FILENAME)
            if activeScreen == 'introduction':
                wn.bgpic('images\\intro\\turtleanimation\\{}.png'.format(i))
                wn.update()
                sleep(.033)
            else:
                endIntro()
                return None
        sleep(1)
        for i in range(157, 168):
            if activeScreen == 'introduction':
                wn.bgpic('images\\intro\\menufadein\\{}.png'.format(i))
                wn.update()
                sleep(.033)
            else:
                endIntro()
                return None

        activeScreen = 'start_menu'
        endIntro()
        
#------------------------------------------ Main Program ------------------------------------------#

#-------------------------------------------- Setup -----------------------------------------------#

menuCoords = {'start_menu_TEXT': (0, 75),
              'start_menu_MODE': (-125, 40),
              'start_menu_START': (125,40),
              'start_menu_HIGH_SCORES': (-70,-10),
              'start_menu_SETTINGS': (-70, -60),
              'start_menu_TUTORIAL': (-70,-105),
              'start_menu_CREDITS': (-70,-150),
              'start_menu_EXIT': (-70,-200),
              'mode_select_CLASSIC': (-90,0),
              'mode_select_TIMED':(-90,-80),
              'mode_select_ADVENTURE': (-90,-160),
              'settings_TEXT': (0, 100),
              'settings_ENVIRONMENT': (-185, 50),
              'settings_environment_FOREST': (-165, -125),
              'settings_environment_BEACH': (0, -125),
              'settings_environment_UNDERWATER': (165, -125),
              'settings_DIFFICULTY': (-185, -25),
              'settings_difficulty_EASY': (-165, 100),
              'settings_difficulty_NORMAL': (0, 100),
              'settings_difficulty_HARD': (165, 100),
              'settings_RESET_HIGH_SCORES':(-100, -105),
              'settings_reset_high_scores_YES': (-180, -95),
              'settings_reset_high_scores_NO': (20, -95),
              'settings_BACK': (-100, -190),
              'high_scores_START_WRITING': (-65, 100),
              'victory_PLAY_AGAIN?': (-90,-10),
              'victory_BACK':(-90,-90),
               'victory_EXIT': (-90, -170),
              'game_over_PLAY_AGAIN?': (-195,-125),
              'game_over_BACK': (10, -125) }

wn = Screen()
wn.setup(width=500, height=500)
wn.title('Super Turtle Treasure Hunt!')
wn.bgcolor('black')

treasureStamp = "chest.gif"
wn.register_shape(treasureStamp, shape=None)

gameOver = False                        # Indicates that the game is not over.
moving = False                          # Indicates that kame is moving either fwd or back
turningLeft = False                     # Indicates that kame is/isn't turning left
turningRight = False                    # Indicates that kame is/isn't turning right
stopSpinning = False                    # Should kame turn?
wasntMoving = False                     # Was kame moving?
activeScreen = 'introduction'           # Indicates which screen is currently active
background = 'images\\beach.png'        # Indicates background file string associated with current environment.
environment = 'beach'                   # Indicates current environment
difficulty = 'normal'                   # Indicates current difficulty setting
mode = 'classic'                        # Indicates current game mode
score = 0                               # Keeps track of player's current score
treasures = 0                           # How many treasures have been collected
r, tx, ty = 0, 0, 0                     # Initializes radius and coordinates of treasure.
colormode(255)                          # Sets our color mode to RGB for hotCold() function.
maxx = 350                              # Distance beyond which turtle is blue
minn = 39                               # Distance within which turtle is red
hazardList = []                         # Holds coordinate pairs of active hazards
diff_multiplier = 2                     # Score multiplier. Changes w/ difficulty.
time = 60000                            # Timed mode 1 minute by default
rmin = 20                               # Minimum treasure radius
rmax = 30                               # Maximum treasure radius
speedmod = 1                            # Determines turtle move distance.
hr = 20                                 # Default hazard radius
numOfHazards = 1                        # Default number of hazards
lives = 3                               # Initialize "lives"

#-------------------------------------- Turtles -------------------------------------------------#
sketchy = Turtle(visible = False)       # Stamps treasures when found.
timey = Turtle(visible = False)         # SUPPOSED to display the time remaining on the screen. Actually does nothing.
holey = Turtle(visible = False)         # Stamps a hole when you run into it.
scoreKeeper = Turtle(visible = False)   # Displays score on the screen.
writey = Turtle(visible = False)        # Writes descriptive menu text.
modeWriter = Turtle(visible = False)    # Writes the current mode where appropriate
eWriter = Turtle(visible = False)       # Writes the current environment where appropriate
dWriter = Turtle(visible = False)       # Writes the current difficulty where appropriate

sketchy.resizemode('auto')
sketchy.pensize(3)
sketchy.shape(treasureStamp)

modeWriter.color('#157d00', '#157d00')
modeWriter.penup()
modeWriter.setpos(60,25)

eWriter.penup()
eWriter.color('#157d00')
eWriter.setpos(95,40)

dWriter.penup()
dWriter.color('#157d00')
dWriter.setpos(95,-40)

writey.penup()
writey.speed(10)
writey.setpos(menuCoords['start_menu_TEXT'])

cursor = Turtle(visible = False)
cursor.speed(10)
cursor.penup()
cursor.resizemode('auto')
cursor.pensize(10)

holey.penup()
holey.shape('circle')
holey.resizemode('auto')
holey.pensize(8)
cursor.setpos(menuCoords['start_menu_MODE'])

kame = Turtle(visible = False)
kame.shape('turtle')
kame.penup()
kame.resizemode('auto')
kame.pensize(6)
kame.speed('fastest')

scoreKeeper.penup()
scoreKeeper.color('white', 'black')
scoreKeeper.setpos(200, -225)

#--------- Set up High Scores list -----------#
try:
    hs = open('highscores.txt')
except:
    hs = open('highscores.txt', 'w')
    hs.close()
    hs = open('highscores.txt')
    
tempList = hs.read().split('\n')
hs.close()

highScoreList = []
if tempList != ['']:
    tempList.pop()
    for element in tempList:
        newRecord = element.split('\t')
        newRecord[1] = int(newRecord[1])
        recordInsert(newRecord)

#--------- Keypresses --------#
onkeypress(resetTurtle, 'b')
onkeypress(setPosition, 'c')
onkeypress(moveCursorDown, 'Down')
onkeypress(moveCursorUp, 'Up')
onkeypress(moveCursorLeft, 'Left')
onkeypress(moveCursorRight, 'Right')
onkeypress(select, 'space')

print("Basic controls:\n-Use the arrow keys to navigate menus.\n-Use SPACE to make a selection or go back.\n-Use ASDW to move.\n-Move cursor to right side of 'Modes' and press 'Space' to start game.")

wn.listen()
playIntroduction()


