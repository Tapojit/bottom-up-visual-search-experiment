#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Sun 08 Jan 2017 07:43:43 AM EST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


import random, datetime, math, json, xlsxwriter
from pprint import pprint
import gtk

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'untitled'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Stable"
StableClock = core.Clock()
textS = visual.TextStim(win=win, name='textS',
    text=u'Press any key to begin. ',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);


#change this to no.of frames

count_frames=72

# Initialize components for Routine "Crosshair"
CrosshairClock = core.Clock()
cross = visual.ImageStim(
    win=win, name='image_2',
    image=os.getcwd()+"/"+"crosshair.png", mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Initialize components for Routine "frame1"
frame1Clock = core.Clock()
frame1image = visual.ImageStim(
    win=win, name='frame1image',
    image=os.getcwd()+"/"+"img1.png", mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "frame2"
frame2Clock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text=u'You will be asked to respond to\nwhether the left or right corner is\ncut off the target diamond.\n\nThe target is designated by it being either\nthe only item on the screen, or the only\nitem of its color (either red or green)\non the screen.\n\nIf the left corner is cut, press the "z"\nkey. If the right corner is cut, press "/"',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "frame3"
frame3Clock = core.Clock()
text2 = visual.TextStim(win=win, name='text2',
    text=u'Please try to respond to every frame\nas quickly and accurately as possible.\nHowever, if you mess up, please try to\nkeep going and do not worry.\n\nAlso, please try to keep your eyes fixed\non the center of the screen, where the \nsmall cross will appear between displays.\n\n Wait for 5 seconds before pressing key. ',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Image"
ImageClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "frame1"-------
t = 0
frame1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
frame1Components = [frame1image, key_resp_4]
for thisComponent in frame1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "frame1"-------
while continueRoutine:
    # get current time
    t = frame1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *frame1image* updates
    if t >= 0.0 and frame1image.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame1image.tStart = t
        frame1image.frameNStart = frameN  # exact frame index
        frame1image.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frame1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "frame1"-------
for thisComponent in frame1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "frame1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "frame2"-------
t = 0
frame2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()# Initialize components for Routine "frame3"
# keep track of which components have finished
frame2Components = [text1, key_resp_2]
for thisComponent in frame2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "frame2"-------
while continueRoutine:
    # get current time
    t = frame2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text1* updates
    if t >= 0.0 and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frame2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "frame2"-------
for thisComponent in frame2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "frame2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "frame3"-------
t = 0
frame3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
frame3Components = [text2, key_resp_3]
for thisComponent in frame3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "frame3"-------
while continueRoutine:
    # get current time
    t = frame3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text2* updates
    if t >= 0.0 and text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2.tStart = t
        text2.frameNStart = frameN  # exact frame index
        text2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frame3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "frame3"-------
for thisComponent in frame3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "frame3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# set up handler to look after randomisation of conditions etc
Outer = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Outer')
thisExp.addLoop(Outer)  # add the loop to the experiment
thisOuter = Outer.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOuter.rgb)
if thisOuter != None:
    for paramName in thisOuter.keys():
        exec(paramName + '= thisOuter.' + paramName)

p=1
for thisOuter in Outer:
    currentLoop = Outer
    # abbreviate parameter names if possible (e.g. rgb = thisOuter.rgb)
    if thisOuter != None:
        for paramName in thisOuter.keys():
            exec(paramName + '= thisOuter.' + paramName)
    
    # ------Prepare to start Routine "Stable"-------
    t = 0
    
    StableClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    keyA=event.BuilderKeyResponse()
    # keep track of which components have finished
    StableComponents = [textS, keyA]
    for thisComponent in StableComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
#    if (continueRoutine==True):
    scaleVar=gtk.gdk.screen_width()/640
    from distractors import make_study,SETTINGS
    SETTINGS["frame size"]=[gtk.gdk.screen_width(), gtk.gdk.screen_height()]
    SETTINGS["seed"]=p
    
    #change it based on clutter preferences
    SETTINGS["use clutter?"]=True
#        SETTINGS["diamond spread"]=SETTINGS["diamond spread"]*scaleVar
#        SETTINGS["diamond scale"]=SETTINGS["diamond scale"]*scaleVar
    filetimeStamp="study "+make_study(SETTINGS)
    workbook=xlsxwriter.Workbook(str(filetimeStamp)+'.xlsx')
    worksheet=workbook.add_worksheet()
    worksheet.set_column(1, 1,25)
    worksheet.write('A1', 'color')
    worksheet.write('B1','condition')
    worksheet.write('C1','position')
    worksheet.write('D1', 'cutDir')
    worksheet.write('E1', 'corrAns')
    worksheet.write('F1', 'Distractor1')
    worksheet.write('G1', 'Distractor2')
    worksheet.write('H1', 'Distractor3')
    worksheet.write('I1', 'Distractor4')
    worksheet.write('J1', 'Distractor5')
    worksheet.write('K1', 'Distractor6')
    worksheet.write('L1', 'Distractor7')
    worksheet.write('M1', 'Distractor8')
    worksheet.write('N1', 'Distractor9')
    currentDir=os.getcwd()
    os.chdir(currentDir+ "/studies/"+str(filetimeStamp))
    with open('frames.json') as data_file:
        dataJson=json.load(data_file)
    row=1
    column=0
    os.chdir(currentDir)
    for i in range(count_frames):
        tarCol=dataJson["target color"][i]
        if (dataJson["target cut on"][i]=="left"):
            key="z"
        else: key="slash"
        worksheet.write_string(row,column,tarCol)
        worksheet.write_string(row,column+1,dataJson["clutter condition"][i])
        worksheet.write_string(row,column+2,str(dataJson["target index"][i]))
        worksheet.write_string(row,column+3,dataJson["target cut on"][i])
        worksheet.write_string(row,column+4,key)
        for x in range(9):
            if(x!=dataJson["target index"][i]):
                worksheet.write_string(row,column+5+x,str(dataJson["all cutoffs"][i][x]))
            else: worksheet.write_string(row,column+5+x,"nil")
        row+=1    
    workbook.close()

    
    
    
    
    # -------Start Routine "Stable"-------
    while continueRoutine:
        # get current time
        t = StableClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
	if t >= 0.0 and textS.status == NOT_STARTED:
            # keep track of start time/frame for later
            textS.tStart = t
            textS.frameNStart = frameN  # exact frame index
            textS.setAutoDraw(True)
        
        # *KeyA* updates
        if t>=0.0 and keyA.status==NOT_STARTED:
            # keep track of start time/frame for later
            keyA.tStart = t
            keyA.frameNStart = frameN  # exact frame index
            keyA.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(keyA.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if keyA.status==STARTED:
            theseKeys=event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyA.keys = theseKeys[-1]  # just the last key pressed
                keyA.rt = keyA.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StableComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stable"-------
    for thisComponent in StableComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
    # check responses
    if keyA.keys in ['', [], None]:  # No response was made
        keyA.keys=None
    thisExp.addData('keyA.keys',keyA.keys)
    if keyA.keys != None:  # we had a response
        thisExp.addData('keyA.rt', keyA.rt)
    thisExp.nextEntry()
    # the Routine "Stable" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Inner = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(str(filetimeStamp)+'.xlsx'),
        seed=None, name='Inner')
    thisExp.addLoop(Inner)  # add the loop to the experiment
    thisInner = Inner.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInner.rgb)
    if thisInner != None:
        for paramName in thisInner.keys():
            exec(paramName + '= thisInner.' + paramName)
    
    l=0
    image = visual.ImageStim(
        win=win, name='image',
        image=dataJson["filepath"][l], mask=None,
        ori=0, pos=(0, 0), size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0) 
    
    for thisInner in Inner:
        currentLoop = Inner
        # abbreviate parameter names if possible (e.g. rgb = thisInner.rgb)
        if thisInner != None:
            for paramName in thisInner.keys():
                exec(paramName + '= thisInner.' + paramName)
        
        # ------Prepare to start Routine "Crosshair"-------
        t = 0
        CrosshairClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        keyB = event.BuilderKeyResponse()
        # keep track of which components have finished
        CrosshairComponents = [cross,keyB]
        for thisComponent in CrosshairComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Crosshair"-------
        while continueRoutine and routineTimer.getTime()>0:
            # get current time
            t = CrosshairClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if t >= 0.0 and cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross.tStart = t
                cross.frameNStart = frameN  # exact frame index
                cross.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cross.status == STARTED and t >= frameRemains:
                cross.setAutoDraw(False)
            
            # *keyB* updates
            if t >= 0.0 and keyB.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyB.tStart = t
                keyB.frameNStart = frameN  # exact frame index
                keyB.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(keyB.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if keyB.status == STARTED and t >= frameRemains:
                keyB.status = STOPPED
            if keyB.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    keyB.keys = theseKeys[-1]  # just the last key pressed
                    keyB.rt = keyB.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CrosshairComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Crosshair"-------
        for thisComponent in CrosshairComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        # check responses
        if keyB.keys in ['', [], None]:  # No response was made
            keyB.keys=None
        Inner.addData('keyB',keyB.keys)
        if keyB.keys != None:  # we had a response
            Inner.addData('keyB.rt', keyB.rt)
                
        # the Routine "Crosshair" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Image"-------
        t = 0
        ImageClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        response=event.BuilderKeyResponse()
        # keep track of which components have finished
        ImageComponents = [image]
        for thisComponent in ImageComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Image"-------
        while continueRoutine and routineTimer.getTime()>0:
            # get current time
            t = ImageClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
                
             # *response* updates
            if t >= 0.0 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['z', 'slash'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    response.keys = theseKeys[-1]  # just the last key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(corrAns)) or (response.keys == corrAns):
                        response.corr = 1
                    else:
                        response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ImageComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Image"-------
        for thisComponent in ImageComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
            l+=1
            if (l<count_frames):
                image = visual.ImageStim(
                    win=win, name='image',
                    image=dataJson["filepath"][l], mask=None,
                    ori=0, pos=(0, 0), size=(2, 2),
                    color=[1,1,1], colorSpace='rgb', opacity=1,
                    flipHoriz=False, flipVert=False,
                    texRes=128, interpolate=True, depth=0.0) 
        
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               response.corr = 1  # correct non-response
            else:
               response.corr = 0  # failed to respond (incorrectly)
               
        # store data for trials (TrialHandler)
        Inner.addData('Key pressed',response.keys)
        Inner.addData('Correct?', response.corr)
        if response.keys != None:  # we had a response
            Inner.addData('Response reaction time', response.rt)
                    
        # the Routine "Image" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
            
    # completed 36 repeats of 'Inner'
    
#    thisExp.nextEntry()
    p+=1
    
# completed 10 repeats of 'Outer'

# Initialize components for Routine "frameFinal"
frameFClock = core.Clock()
textf = visual.TextStim(win=win, name='textf',
    text=u'Experiment over.\nThank you for participating',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# ------Prepare to start Routine "frameFinal"-------
t = 0
    
frameFClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_F = event.BuilderKeyResponse()
# keep track of which components have finished
frameFComponents = [textf, key_resp_F]
for thisComponent in frameFComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


# -------Start Routine "frameFinal"-------
while continueRoutine:
    # get current time
    t = frameFClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textf* updates
    if t >= 0.0 and textf.status == NOT_STARTED:
        # keep track of start time/frame for later
        textf.tStart = t
        textf.frameNStart = frameN  # exact frame index
        textf.setAutoDraw(True)
    
    # *key_resp_F* updates
    if t >= 0.0 and key_resp_F.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_F.tStart = t
        key_resp_F.frameNStart = frameN  # exact frame index
        key_resp_F.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_F.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_F.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_F.keys = theseKeys[-1]  # just the last key pressed
            key_resp_F.rt = key_resp_F.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in frameFComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "frameFinal"-------
for thisComponent in frameFComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "frameFinal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
