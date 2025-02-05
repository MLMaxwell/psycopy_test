#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Mon Sep  9 11:54:00 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'PWI'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/kenzieleigh/Desktop/Research Labs/Language Science/Experiment - PWI/PWI_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1512, 982], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.9922, 0.9608, 0.8902], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.9922, 0.9608, 0.8902]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Welcome!\n\nThe experiment will consist of four phases: a familiarization phase, a familiarization check, a practice trial, and experimental trials.\n\nDuring the familiarization phase, multiple single object images will be presented. You will be expected to familiarize yourself with the names of these images. Press enter when ready to move to the next screen. \n\nYou will then move on to a familiarization exercise to ensure you can correctly identify the names of these images.\n\nEach practice and experimental trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nYou will be reminded of these instructions prior to the start of the trials.\n\nIf at any time you need technical assistance or any questions/concerns, please contact the research assistant.\n\nPress enter when ready',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_respWelcome = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "familiarIntro" ---
    familiarization_intro = visual.TextStim(win=win, name='familiarization_intro',
        text='The familiarization stage will now begin.\n\nRemember to take your time and familiarize yourself with the name of each object. You will be asked to name these items in the trial.\n\nPress enter when ready to begin.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    familiarization_keyresp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "NamingIntro" ---
    NamingInstruct_text = visual.TextStim(win=win, name='NamingInstruct_text',
        text='This is the familiarization check \n\nAn image will appear on the screen. Please say the name of the image as quickly as possible. This familiarization check is about making sure you know the name of the object in the image.\n\nThe correct name of the image will appear on the screen after 3 seconds.\n\nPress enter when ready to begin.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    NamingInstruct_keyresp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practiceTrialInstructions" ---
    PTInstruct_text = visual.TextStim(win=win, name='PTInstruct_text',
        text='PRACTICE TRIAL INSTRUCTIONS\n\nEach trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nIf at any time you need technical assistance or any questions/concerns, please contact the research assistant.\n\nThe practice trial will now begin.\nPress enter when ready',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    PTInstruct_keyresp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TrialInstructions" ---
    TrialInstruct_text = visual.TextStim(win=win, name='TrialInstruct_text',
        text='TRIAL INSTRUCTIONS\n\nEach trial will begin with a red fixation cross that will remain on the screen for 300 ms. After the cross disappears, an image of a single object will appear superimposed with some text. Below the image, you will see a red dot indicating the microphone is ready to record. \n\nPlease say the name of the image as quickly as possible. This name should match the object name provided during the familiarization exercise. \n\nWhen finished stating the name, press enter to move to the next trial.\n\nThroughout the experiment, will receive seven 1 minute breaks that may be skipped at your discretion. \n\nIf at any time you need technical assitance or any questions/concerns, please contact the research assistant.\n\nThe trial will now begin\nPress enter when ready',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    TrialInstruct_keyresp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Trial_Set_1" ---
    Fixation_Set_1 = visual.ShapeStim(
        win=win, name='Fixation_Set_1', vertices='cross',
        size=(0.4, 0.4),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    image_2_set_1 = visual.ImageStim(
        win=win,
        name='image_2_set_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_1_set_1 = visual.ImageStim(
        win=win,
        name='image_1_set_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Recording_Circle_Set_1 = visual.ShapeStim(
        win=win, name='Recording_Circle_Set_1',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, -.35), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    Enter_Text_Set_1 = visual.TextStim(win=win, name='Enter_Text_Set_1',
        text='',
        font='Verdana',
        pos=(0, -.45), height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Enter_Response_Set_1 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "betweentrialbreak" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='You are done with that set. \nYou may now take up to a 1 minute rest.\nA countdown will appear when the experiment is close.\nPress enter at any time to bypass this break',
        font='Open Sans',
        pos=(0, .25), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    ten = visual.TextStim(win=win, name='ten',
        text='10',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    nine = visual.TextStim(win=win, name='nine',
        text='9',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    eight = visual.TextStim(win=win, name='eight',
        text='8',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    seven = visual.TextStim(win=win, name='seven',
        text='7',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    six = visual.TextStim(win=win, name='six',
        text='6',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    five = visual.TextStim(win=win, name='five',
        text='5',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    four = visual.TextStim(win=win, name='four',
        text='4',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    three = visual.TextStim(win=win, name='three',
        text='3',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    two = visual.TextStim(win=win, name='two',
        text='2',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    one = visual.TextStim(win=win, name='one',
        text='1',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    text_16end = visual.TextStim(win=win, name='text_16end',
        text='PRESS ENTER NOW',
        font='Open Sans',
        pos=(0, -.06), height=0.07, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "NewSetBegin" ---
    text_NewSet = visual.TextStim(win=win, name='text_NewSet',
        text='The next trial is begining now',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Trial_Set_2" ---
    Fixation_Set_2 = visual.ShapeStim(
        win=win, name='Fixation_Set_2', vertices='cross',
        size=(0.4, 0.4),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    image_2_set_2 = visual.ImageStim(
        win=win,
        name='image_2_set_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_1_set_2 = visual.ImageStim(
        win=win,
        name='image_1_set_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Recording_Circle_Set_2 = visual.ShapeStim(
        win=win, name='Recording_Circle_Set_2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, -.35), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    Enter_Text_Set_2 = visual.TextStim(win=win, name='Enter_Text_Set_2',
        text='',
        font='Open Sans',
        pos=(0, -.45), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Enter_Response_Set_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "betweentrialbreak" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='You are done with that set. \nYou may now take up to a 1 minute rest.\nA countdown will appear when the experiment is close.\nPress enter at any time to bypass this break',
        font='Open Sans',
        pos=(0, .25), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    ten = visual.TextStim(win=win, name='ten',
        text='10',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    nine = visual.TextStim(win=win, name='nine',
        text='9',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    eight = visual.TextStim(win=win, name='eight',
        text='8',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    seven = visual.TextStim(win=win, name='seven',
        text='7',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    six = visual.TextStim(win=win, name='six',
        text='6',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    five = visual.TextStim(win=win, name='five',
        text='5',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    four = visual.TextStim(win=win, name='four',
        text='4',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    three = visual.TextStim(win=win, name='three',
        text='3',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    two = visual.TextStim(win=win, name='two',
        text='2',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    one = visual.TextStim(win=win, name='one',
        text='1',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    text_16end = visual.TextStim(win=win, name='text_16end',
        text='PRESS ENTER NOW',
        font='Open Sans',
        pos=(0, -.06), height=0.07, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "NewSetBegin" ---
    text_NewSet = visual.TextStim(win=win, name='text_NewSet',
        text='The next trial is begining now',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Trial_Set_3" ---
    Fixation_Set_3 = visual.ShapeStim(
        win=win, name='Fixation_Set_3', vertices='cross',
        size=(0.4, 0.4),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    image_2_set_3 = visual.ImageStim(
        win=win,
        name='image_2_set_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_1_set_3 = visual.ImageStim(
        win=win,
        name='image_1_set_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Recording_Circle_Set_3 = visual.ShapeStim(
        win=win, name='Recording_Circle_Set_3',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, -.35), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    Enter_Text_Set_3 = visual.TextStim(win=win, name='Enter_Text_Set_3',
        text='',
        font='Open Sans',
        pos=(0, -.45), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Enter_Response_Set_3 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "betweentrialbreak" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='You are done with that set. \nYou may now take up to a 1 minute rest.\nA countdown will appear when the experiment is close.\nPress enter at any time to bypass this break',
        font='Open Sans',
        pos=(0, .25), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    ten = visual.TextStim(win=win, name='ten',
        text='10',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    nine = visual.TextStim(win=win, name='nine',
        text='9',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    eight = visual.TextStim(win=win, name='eight',
        text='8',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    seven = visual.TextStim(win=win, name='seven',
        text='7',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    six = visual.TextStim(win=win, name='six',
        text='6',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    five = visual.TextStim(win=win, name='five',
        text='5',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    four = visual.TextStim(win=win, name='four',
        text='4',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    three = visual.TextStim(win=win, name='three',
        text='3',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    two = visual.TextStim(win=win, name='two',
        text='2',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    one = visual.TextStim(win=win, name='one',
        text='1',
        font='Open Sans',
        pos=(0, -.06), height=0.5, wrapWidth=None, ori=0.0, 
        color=[0.8431, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    text_16end = visual.TextStim(win=win, name='text_16end',
        text='PRESS ENTER NOW',
        font='Open Sans',
        pos=(0, -.06), height=0.07, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "NewSetBegin" ---
    text_NewSet = visual.TextStim(win=win, name='text_NewSet',
        text='The next trial is begining now',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blank500" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Trial_Set_4" ---
    Fixation_Set_4 = visual.ShapeStim(
        win=win, name='Fixation_Set_4', vertices='cross',
        size=(0.4, 0.4),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    image_2_set_4 = visual.ImageStim(
        win=win,
        name='image_2_set_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_1_set_4 = visual.ImageStim(
        win=win,
        name='image_1_set_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Recording_Circle_Set_4 = visual.ShapeStim(
        win=win, name='Recording_Circle_Set_4',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, -.35), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.6627, -1.0000, -1.0000], fillColor=[0.6627, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    Enter_Text_Set_4 = visual.TextStim(win=win, name='Enter_Text_Set_4',
        text='',
        font='Open Sans',
        pos=(0, -.45), height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    Enter_Response_Set_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "goodbye" ---
    textGoodbye = visual.TextStim(win=win, name='textGoodbye',
        text='The experiment is over.\n\nThank you for participating.\nIf you have any questions or concerns, you may email\nRichard Futrell\nIRB\n\nPress enter to end',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "welcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('welcome.started', globalClock.getTime())
    key_respWelcome.keys = []
    key_respWelcome.rt = []
    _key_respWelcome_allKeys = []
    # keep track of which components have finished
    welcomeComponents = [textWelcome, key_respWelcome]
    for thisComponent in welcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_respWelcome* updates
        waitOnFlip = False
        
        # if key_respWelcome is starting this frame...
        if key_respWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_respWelcome.frameNStart = frameN  # exact frame index
            key_respWelcome.tStart = t  # local t and not account for scr refresh
            key_respWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_respWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_respWelcome.started')
            # update status
            key_respWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_respWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_respWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_respWelcome.status == STARTED and not waitOnFlip:
            theseKeys = key_respWelcome.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_respWelcome_allKeys.extend(theseKeys)
            if len(_key_respWelcome_allKeys):
                key_respWelcome.keys = _key_respWelcome_allKeys[-1].name  # just the last key pressed
                key_respWelcome.rt = _key_respWelcome_allKeys[-1].rt
                key_respWelcome.duration = _key_respWelcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('welcome.stopped', globalClock.getTime())
    # check responses
    if key_respWelcome.keys in ['', [], None]:  # No response was made
        key_respWelcome.keys = None
    thisExp.addData('key_respWelcome.keys',key_respWelcome.keys)
    if key_respWelcome.keys != None:  # we had a response
        thisExp.addData('key_respWelcome.rt', key_respWelcome.rt)
        thisExp.addData('key_respWelcome.duration', key_respWelcome.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blank500.started', globalClock.getTime())
    # keep track of which components have finished
    blank500Components = [text]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank500.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "familiarIntro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('familiarIntro.started', globalClock.getTime())
    familiarization_keyresp.keys = []
    familiarization_keyresp.rt = []
    _familiarization_keyresp_allKeys = []
    # keep track of which components have finished
    familiarIntroComponents = [familiarization_intro, familiarization_keyresp]
    for thisComponent in familiarIntroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "familiarIntro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *familiarization_intro* updates
        
        # if familiarization_intro is starting this frame...
        if familiarization_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            familiarization_intro.frameNStart = frameN  # exact frame index
            familiarization_intro.tStart = t  # local t and not account for scr refresh
            familiarization_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiarization_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'familiarization_intro.started')
            # update status
            familiarization_intro.status = STARTED
            familiarization_intro.setAutoDraw(True)
        
        # if familiarization_intro is active this frame...
        if familiarization_intro.status == STARTED:
            # update params
            pass
        
        # *familiarization_keyresp* updates
        waitOnFlip = False
        
        # if familiarization_keyresp is starting this frame...
        if familiarization_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            familiarization_keyresp.frameNStart = frameN  # exact frame index
            familiarization_keyresp.tStart = t  # local t and not account for scr refresh
            familiarization_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiarization_keyresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'familiarization_keyresp.started')
            # update status
            familiarization_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(familiarization_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(familiarization_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if familiarization_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = familiarization_keyresp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _familiarization_keyresp_allKeys.extend(theseKeys)
            if len(_familiarization_keyresp_allKeys):
                familiarization_keyresp.keys = _familiarization_keyresp_allKeys[-1].name  # just the last key pressed
                familiarization_keyresp.rt = _familiarization_keyresp_allKeys[-1].rt
                familiarization_keyresp.duration = _familiarization_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familiarIntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "familiarIntro" ---
    for thisComponent in familiarIntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('familiarIntro.stopped', globalClock.getTime())
    # check responses
    if familiarization_keyresp.keys in ['', [], None]:  # No response was made
        familiarization_keyresp.keys = None
    thisExp.addData('familiarization_keyresp.keys',familiarization_keyresp.keys)
    if familiarization_keyresp.keys != None:  # we had a response
        thisExp.addData('familiarization_keyresp.rt', familiarization_keyresp.rt)
        thisExp.addData('familiarization_keyresp.duration', familiarization_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "familiarIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blank500.started', globalClock.getTime())
    # keep track of which components have finished
    blank500Components = [text]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank500.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "NamingIntro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('NamingIntro.started', globalClock.getTime())
    NamingInstruct_keyresp.keys = []
    NamingInstruct_keyresp.rt = []
    _NamingInstruct_keyresp_allKeys = []
    # keep track of which components have finished
    NamingIntroComponents = [NamingInstruct_text, NamingInstruct_keyresp]
    for thisComponent in NamingIntroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NamingIntro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NamingInstruct_text* updates
        
        # if NamingInstruct_text is starting this frame...
        if NamingInstruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NamingInstruct_text.frameNStart = frameN  # exact frame index
            NamingInstruct_text.tStart = t  # local t and not account for scr refresh
            NamingInstruct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NamingInstruct_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NamingInstruct_text.started')
            # update status
            NamingInstruct_text.status = STARTED
            NamingInstruct_text.setAutoDraw(True)
        
        # if NamingInstruct_text is active this frame...
        if NamingInstruct_text.status == STARTED:
            # update params
            pass
        
        # *NamingInstruct_keyresp* updates
        waitOnFlip = False
        
        # if NamingInstruct_keyresp is starting this frame...
        if NamingInstruct_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NamingInstruct_keyresp.frameNStart = frameN  # exact frame index
            NamingInstruct_keyresp.tStart = t  # local t and not account for scr refresh
            NamingInstruct_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NamingInstruct_keyresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NamingInstruct_keyresp.started')
            # update status
            NamingInstruct_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NamingInstruct_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NamingInstruct_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NamingInstruct_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = NamingInstruct_keyresp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _NamingInstruct_keyresp_allKeys.extend(theseKeys)
            if len(_NamingInstruct_keyresp_allKeys):
                NamingInstruct_keyresp.keys = _NamingInstruct_keyresp_allKeys[-1].name  # just the last key pressed
                NamingInstruct_keyresp.rt = _NamingInstruct_keyresp_allKeys[-1].rt
                NamingInstruct_keyresp.duration = _NamingInstruct_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NamingIntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NamingIntro" ---
    for thisComponent in NamingIntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('NamingIntro.stopped', globalClock.getTime())
    # check responses
    if NamingInstruct_keyresp.keys in ['', [], None]:  # No response was made
        NamingInstruct_keyresp.keys = None
    thisExp.addData('NamingInstruct_keyresp.keys',NamingInstruct_keyresp.keys)
    if NamingInstruct_keyresp.keys != None:  # we had a response
        thisExp.addData('NamingInstruct_keyresp.rt', NamingInstruct_keyresp.rt)
        thisExp.addData('NamingInstruct_keyresp.duration', NamingInstruct_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "NamingIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blank500.started', globalClock.getTime())
    # keep track of which components have finished
    blank500Components = [text]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank500.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "practiceTrialInstructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('practiceTrialInstructions.started', globalClock.getTime())
    PTInstruct_keyresp.keys = []
    PTInstruct_keyresp.rt = []
    _PTInstruct_keyresp_allKeys = []
    # keep track of which components have finished
    practiceTrialInstructionsComponents = [PTInstruct_text, PTInstruct_keyresp]
    for thisComponent in practiceTrialInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practiceTrialInstructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PTInstruct_text* updates
        
        # if PTInstruct_text is starting this frame...
        if PTInstruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PTInstruct_text.frameNStart = frameN  # exact frame index
            PTInstruct_text.tStart = t  # local t and not account for scr refresh
            PTInstruct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PTInstruct_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PTInstruct_text.started')
            # update status
            PTInstruct_text.status = STARTED
            PTInstruct_text.setAutoDraw(True)
        
        # if PTInstruct_text is active this frame...
        if PTInstruct_text.status == STARTED:
            # update params
            pass
        
        # *PTInstruct_keyresp* updates
        waitOnFlip = False
        
        # if PTInstruct_keyresp is starting this frame...
        if PTInstruct_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PTInstruct_keyresp.frameNStart = frameN  # exact frame index
            PTInstruct_keyresp.tStart = t  # local t and not account for scr refresh
            PTInstruct_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PTInstruct_keyresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PTInstruct_keyresp.started')
            # update status
            PTInstruct_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PTInstruct_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PTInstruct_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PTInstruct_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = PTInstruct_keyresp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _PTInstruct_keyresp_allKeys.extend(theseKeys)
            if len(_PTInstruct_keyresp_allKeys):
                PTInstruct_keyresp.keys = _PTInstruct_keyresp_allKeys[-1].name  # just the last key pressed
                PTInstruct_keyresp.rt = _PTInstruct_keyresp_allKeys[-1].rt
                PTInstruct_keyresp.duration = _PTInstruct_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceTrialInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceTrialInstructions" ---
    for thisComponent in practiceTrialInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('practiceTrialInstructions.stopped', globalClock.getTime())
    # check responses
    if PTInstruct_keyresp.keys in ['', [], None]:  # No response was made
        PTInstruct_keyresp.keys = None
    thisExp.addData('PTInstruct_keyresp.keys',PTInstruct_keyresp.keys)
    if PTInstruct_keyresp.keys != None:  # we had a response
        thisExp.addData('PTInstruct_keyresp.rt', PTInstruct_keyresp.rt)
        thisExp.addData('PTInstruct_keyresp.duration', PTInstruct_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "practiceTrialInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('blank500.started', globalClock.getTime())
    # keep track of which components have finished
    blank500Components = [text]
    for thisComponent in blank500Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank500" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank500.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "TrialInstructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('TrialInstructions.started', globalClock.getTime())
    TrialInstruct_keyresp.keys = []
    TrialInstruct_keyresp.rt = []
    _TrialInstruct_keyresp_allKeys = []
    # keep track of which components have finished
    TrialInstructionsComponents = [TrialInstruct_text, TrialInstruct_keyresp]
    for thisComponent in TrialInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TrialInstructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrialInstruct_text* updates
        
        # if TrialInstruct_text is starting this frame...
        if TrialInstruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialInstruct_text.frameNStart = frameN  # exact frame index
            TrialInstruct_text.tStart = t  # local t and not account for scr refresh
            TrialInstruct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialInstruct_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrialInstruct_text.started')
            # update status
            TrialInstruct_text.status = STARTED
            TrialInstruct_text.setAutoDraw(True)
        
        # if TrialInstruct_text is active this frame...
        if TrialInstruct_text.status == STARTED:
            # update params
            pass
        
        # *TrialInstruct_keyresp* updates
        waitOnFlip = False
        
        # if TrialInstruct_keyresp is starting this frame...
        if TrialInstruct_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialInstruct_keyresp.frameNStart = frameN  # exact frame index
            TrialInstruct_keyresp.tStart = t  # local t and not account for scr refresh
            TrialInstruct_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialInstruct_keyresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TrialInstruct_keyresp.started')
            # update status
            TrialInstruct_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(TrialInstruct_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(TrialInstruct_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if TrialInstruct_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = TrialInstruct_keyresp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _TrialInstruct_keyresp_allKeys.extend(theseKeys)
            if len(_TrialInstruct_keyresp_allKeys):
                TrialInstruct_keyresp.keys = _TrialInstruct_keyresp_allKeys[-1].name  # just the last key pressed
                TrialInstruct_keyresp.rt = _TrialInstruct_keyresp_allKeys[-1].rt
                TrialInstruct_keyresp.duration = _TrialInstruct_keyresp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrialInstructions" ---
    for thisComponent in TrialInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('TrialInstructions.stopped', globalClock.getTime())
    # check responses
    if TrialInstruct_keyresp.keys in ['', [], None]:  # No response was made
        TrialInstruct_keyresp.keys = None
    thisExp.addData('TrialInstruct_keyresp.keys',TrialInstruct_keyresp.keys)
    if TrialInstruct_keyresp.keys != None:  # we had a response
        thisExp.addData('TrialInstruct_keyresp.rt', TrialInstruct_keyresp.rt)
        thisExp.addData('TrialInstruct_keyresp.duration', TrialInstruct_keyresp.duration)
    thisExp.nextEntry()
    # the Routine "TrialInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trial_1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_items_s1.csv'),
        seed=None, name='Trial_1')
    thisExp.addLoop(Trial_1)  # add the loop to the experiment
    thisTrial_1 = Trial_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            globals()[paramName] = thisTrial_1[paramName]
    
    for thisTrial_1 in Trial_1:
        currentLoop = Trial_1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
        if thisTrial_1 != None:
            for paramName in thisTrial_1:
                globals()[paramName] = thisTrial_1[paramName]
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank500.started', globalClock.getTime())
        # keep track of which components have finished
        blank500Components = [text]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank500.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Trial_Set_1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Set_1.started', globalClock.getTime())
        image_2_set_1.setImage(image_2)
        image_1_set_1.setImage(image)
        Enter_Text_Set_1.setText('Press Enter When Ready')
        Enter_Response_Set_1.keys = []
        Enter_Response_Set_1.rt = []
        _Enter_Response_Set_1_allKeys = []
        # keep track of which components have finished
        Trial_Set_1Components = [Fixation_Set_1, image_2_set_1, image_1_set_1, Recording_Circle_Set_1, Enter_Text_Set_1, Enter_Response_Set_1]
        for thisComponent in Trial_Set_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial_Set_1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Set_1* updates
            
            # if Fixation_Set_1 is starting this frame...
            if Fixation_Set_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Set_1.frameNStart = frameN  # exact frame index
                Fixation_Set_1.tStart = t  # local t and not account for scr refresh
                Fixation_Set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Set_1.started')
                # update status
                Fixation_Set_1.status = STARTED
                Fixation_Set_1.setAutoDraw(True)
            
            # if Fixation_Set_1 is active this frame...
            if Fixation_Set_1.status == STARTED:
                # update params
                pass
            
            # if Fixation_Set_1 is stopping this frame...
            if Fixation_Set_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_Set_1.tStartRefresh + .300-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_Set_1.tStop = t  # not accounting for scr refresh
                    Fixation_Set_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Set_1.stopped')
                    # update status
                    Fixation_Set_1.status = FINISHED
                    Fixation_Set_1.setAutoDraw(False)
            
            # *image_2_set_1* updates
            
            # if image_2_set_1 is starting this frame...
            if image_2_set_1.status == NOT_STARTED and tThisFlip >= .450-frameTolerance:
                # keep track of start time/frame for later
                image_2_set_1.frameNStart = frameN  # exact frame index
                image_2_set_1.tStart = t  # local t and not account for scr refresh
                image_2_set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2_set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_set_1.started')
                # update status
                image_2_set_1.status = STARTED
                image_2_set_1.setAutoDraw(True)
            
            # if image_2_set_1 is active this frame...
            if image_2_set_1.status == STARTED:
                # update params
                pass
            
            # *image_1_set_1* updates
            
            # if image_1_set_1 is starting this frame...
            if image_1_set_1.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                image_1_set_1.frameNStart = frameN  # exact frame index
                image_1_set_1.tStart = t  # local t and not account for scr refresh
                image_1_set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1_set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_set_1.started')
                # update status
                image_1_set_1.status = STARTED
                image_1_set_1.setAutoDraw(True)
            
            # if image_1_set_1 is active this frame...
            if image_1_set_1.status == STARTED:
                # update params
                pass
            
            # if image_1_set_1 is stopping this frame...
            if image_1_set_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_1_set_1.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_1_set_1.tStop = t  # not accounting for scr refresh
                    image_1_set_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_set_1.stopped')
                    # update status
                    image_1_set_1.status = FINISHED
                    image_1_set_1.setAutoDraw(False)
            
            # *Recording_Circle_Set_1* updates
            
            # if Recording_Circle_Set_1 is starting this frame...
            if Recording_Circle_Set_1.status == NOT_STARTED and tThisFlip >= .300-frameTolerance:
                # keep track of start time/frame for later
                Recording_Circle_Set_1.frameNStart = frameN  # exact frame index
                Recording_Circle_Set_1.tStart = t  # local t and not account for scr refresh
                Recording_Circle_Set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Recording_Circle_Set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Recording_Circle_Set_1.started')
                # update status
                Recording_Circle_Set_1.status = STARTED
                Recording_Circle_Set_1.setAutoDraw(True)
            
            # if Recording_Circle_Set_1 is active this frame...
            if Recording_Circle_Set_1.status == STARTED:
                # update params
                pass
            
            # if Recording_Circle_Set_1 is stopping this frame...
            if Recording_Circle_Set_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Recording_Circle_Set_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Recording_Circle_Set_1.tStop = t  # not accounting for scr refresh
                    Recording_Circle_Set_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recording_Circle_Set_1.stopped')
                    # update status
                    Recording_Circle_Set_1.status = FINISHED
                    Recording_Circle_Set_1.setAutoDraw(False)
            
            # *Enter_Text_Set_1* updates
            
            # if Enter_Text_Set_1 is starting this frame...
            if Enter_Text_Set_1.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Text_Set_1.frameNStart = frameN  # exact frame index
                Enter_Text_Set_1.tStart = t  # local t and not account for scr refresh
                Enter_Text_Set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Text_Set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Text_Set_1.started')
                # update status
                Enter_Text_Set_1.status = STARTED
                Enter_Text_Set_1.setAutoDraw(True)
            
            # if Enter_Text_Set_1 is active this frame...
            if Enter_Text_Set_1.status == STARTED:
                # update params
                pass
            
            # *Enter_Response_Set_1* updates
            waitOnFlip = False
            
            # if Enter_Response_Set_1 is starting this frame...
            if Enter_Response_Set_1.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Response_Set_1.frameNStart = frameN  # exact frame index
                Enter_Response_Set_1.tStart = t  # local t and not account for scr refresh
                Enter_Response_Set_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Response_Set_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Response_Set_1.started')
                # update status
                Enter_Response_Set_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Enter_Response_Set_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Enter_Response_Set_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Enter_Response_Set_1.status == STARTED and not waitOnFlip:
                theseKeys = Enter_Response_Set_1.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _Enter_Response_Set_1_allKeys.extend(theseKeys)
                if len(_Enter_Response_Set_1_allKeys):
                    Enter_Response_Set_1.keys = _Enter_Response_Set_1_allKeys[-1].name  # just the last key pressed
                    Enter_Response_Set_1.rt = _Enter_Response_Set_1_allKeys[-1].rt
                    Enter_Response_Set_1.duration = _Enter_Response_Set_1_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_Set_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Set_1" ---
        for thisComponent in Trial_Set_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Set_1.stopped', globalClock.getTime())
        # check responses
        if Enter_Response_Set_1.keys in ['', [], None]:  # No response was made
            Enter_Response_Set_1.keys = None
        Trial_1.addData('Enter_Response_Set_1.keys',Enter_Response_Set_1.keys)
        if Enter_Response_Set_1.keys != None:  # we had a response
            Trial_1.addData('Enter_Response_Set_1.rt', Enter_Response_Set_1.rt)
            Trial_1.addData('Enter_Response_Set_1.duration', Enter_Response_Set_1.duration)
        # the Routine "Trial_Set_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Trial_1'
    
    
    # --- Prepare to start Routine "betweentrialbreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('betweentrialbreak.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    betweentrialbreakComponents = [text_6, key_resp, ten, nine, eight, seven, six, five, four, three, two, one, text_16end]
    for thisComponent in betweentrialbreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "betweentrialbreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ten* updates
        
        # if ten is starting this frame...
        if ten.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            ten.frameNStart = frameN  # exact frame index
            ten.tStart = t  # local t and not account for scr refresh
            ten.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ten.started')
            # update status
            ten.status = STARTED
            ten.setAutoDraw(True)
        
        # if ten is active this frame...
        if ten.status == STARTED:
            # update params
            pass
        
        # if ten is stopping this frame...
        if ten.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ten.tStop = t  # not accounting for scr refresh
                ten.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ten.stopped')
                # update status
                ten.status = FINISHED
                ten.setAutoDraw(False)
        
        # *nine* updates
        
        # if nine is starting this frame...
        if nine.status == NOT_STARTED and tThisFlip >= 51-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nine.started')
            # update status
            nine.status = STARTED
            nine.setAutoDraw(True)
        
        # if nine is active this frame...
        if nine.status == STARTED:
            # update params
            pass
        
        # if nine is stopping this frame...
        if nine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                nine.tStop = t  # not accounting for scr refresh
                nine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nine.stopped')
                # update status
                nine.status = FINISHED
                nine.setAutoDraw(False)
        
        # *eight* updates
        
        # if eight is starting this frame...
        if eight.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
            # keep track of start time/frame for later
            eight.frameNStart = frameN  # exact frame index
            eight.tStart = t  # local t and not account for scr refresh
            eight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eight.started')
            # update status
            eight.status = STARTED
            eight.setAutoDraw(True)
        
        # if eight is active this frame...
        if eight.status == STARTED:
            # update params
            pass
        
        # if eight is stopping this frame...
        if eight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eight.tStop = t  # not accounting for scr refresh
                eight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eight.stopped')
                # update status
                eight.status = FINISHED
                eight.setAutoDraw(False)
        
        # *seven* updates
        
        # if seven is starting this frame...
        if seven.status == NOT_STARTED and tThisFlip >= 53-frameTolerance:
            # keep track of start time/frame for later
            seven.frameNStart = frameN  # exact frame index
            seven.tStart = t  # local t and not account for scr refresh
            seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'seven.started')
            # update status
            seven.status = STARTED
            seven.setAutoDraw(True)
        
        # if seven is active this frame...
        if seven.status == STARTED:
            # update params
            pass
        
        # if seven is stopping this frame...
        if seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                seven.tStop = t  # not accounting for scr refresh
                seven.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'seven.stopped')
                # update status
                seven.status = FINISHED
                seven.setAutoDraw(False)
        
        # *six* updates
        
        # if six is starting this frame...
        if six.status == NOT_STARTED and tThisFlip >= 54-frameTolerance:
            # keep track of start time/frame for later
            six.frameNStart = frameN  # exact frame index
            six.tStart = t  # local t and not account for scr refresh
            six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'six.started')
            # update status
            six.status = STARTED
            six.setAutoDraw(True)
        
        # if six is active this frame...
        if six.status == STARTED:
            # update params
            pass
        
        # if six is stopping this frame...
        if six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                six.tStop = t  # not accounting for scr refresh
                six.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'six.stopped')
                # update status
                six.status = FINISHED
                six.setAutoDraw(False)
        
        # *five* updates
        
        # if five is starting this frame...
        if five.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            five.frameNStart = frameN  # exact frame index
            five.tStart = t  # local t and not account for scr refresh
            five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'five.started')
            # update status
            five.status = STARTED
            five.setAutoDraw(True)
        
        # if five is active this frame...
        if five.status == STARTED:
            # update params
            pass
        
        # if five is stopping this frame...
        if five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                five.tStop = t  # not accounting for scr refresh
                five.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five.stopped')
                # update status
                five.status = FINISHED
                five.setAutoDraw(False)
        
        # *four* updates
        
        # if four is starting this frame...
        if four.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            four.frameNStart = frameN  # exact frame index
            four.tStart = t  # local t and not account for scr refresh
            four.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'four.started')
            # update status
            four.status = STARTED
            four.setAutoDraw(True)
        
        # if four is active this frame...
        if four.status == STARTED:
            # update params
            pass
        
        # if four is stopping this frame...
        if four.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                four.tStop = t  # not accounting for scr refresh
                four.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'four.stopped')
                # update status
                four.status = FINISHED
                four.setAutoDraw(False)
        
        # *three* updates
        
        # if three is starting this frame...
        if three.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            three.frameNStart = frameN  # exact frame index
            three.tStart = t  # local t and not account for scr refresh
            three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three.started')
            # update status
            three.status = STARTED
            three.setAutoDraw(True)
        
        # if three is active this frame...
        if three.status == STARTED:
            # update params
            pass
        
        # if three is stopping this frame...
        if three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                three.tStop = t  # not accounting for scr refresh
                three.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three.stopped')
                # update status
                three.status = FINISHED
                three.setAutoDraw(False)
        
        # *two* updates
        
        # if two is starting this frame...
        if two.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            two.frameNStart = frameN  # exact frame index
            two.tStart = t  # local t and not account for scr refresh
            two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two.started')
            # update status
            two.status = STARTED
            two.setAutoDraw(True)
        
        # if two is active this frame...
        if two.status == STARTED:
            # update params
            pass
        
        # if two is stopping this frame...
        if two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                two.tStop = t  # not accounting for scr refresh
                two.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two.stopped')
                # update status
                two.status = FINISHED
                two.setAutoDraw(False)
        
        # *one* updates
        
        # if one is starting this frame...
        if one.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one.started')
            # update status
            one.status = STARTED
            one.setAutoDraw(True)
        
        # if one is active this frame...
        if one.status == STARTED:
            # update params
            pass
        
        # if one is stopping this frame...
        if one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                one.tStop = t  # not accounting for scr refresh
                one.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one.stopped')
                # update status
                one.status = FINISHED
                one.setAutoDraw(False)
        
        # *text_16end* updates
        
        # if text_16end is starting this frame...
        if text_16end.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_16end.frameNStart = frameN  # exact frame index
            text_16end.tStart = t  # local t and not account for scr refresh
            text_16end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_16end.started')
            # update status
            text_16end.status = STARTED
            text_16end.setAutoDraw(True)
        
        # if text_16end is active this frame...
        if text_16end.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in betweentrialbreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "betweentrialbreak" ---
    for thisComponent in betweentrialbreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('betweentrialbreak.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "betweentrialbreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "NewSetBegin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('NewSetBegin.started', globalClock.getTime())
    # keep track of which components have finished
    NewSetBeginComponents = [text_NewSet]
    for thisComponent in NewSetBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NewSetBegin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_NewSet* updates
        
        # if text_NewSet is starting this frame...
        if text_NewSet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_NewSet.frameNStart = frameN  # exact frame index
            text_NewSet.tStart = t  # local t and not account for scr refresh
            text_NewSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_NewSet, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_NewSet.started')
            # update status
            text_NewSet.status = STARTED
            text_NewSet.setAutoDraw(True)
        
        # if text_NewSet is active this frame...
        if text_NewSet.status == STARTED:
            # update params
            pass
        
        # if text_NewSet is stopping this frame...
        if text_NewSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_NewSet.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_NewSet.tStop = t  # not accounting for scr refresh
                text_NewSet.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_NewSet.stopped')
                # update status
                text_NewSet.status = FINISHED
                text_NewSet.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NewSetBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NewSetBegin" ---
    for thisComponent in NewSetBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('NewSetBegin.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    Trial_2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_items_s2.csv'),
        seed=None, name='Trial_2')
    thisExp.addLoop(Trial_2)  # add the loop to the experiment
    thisTrial_2 = Trial_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in Trial_2:
        currentLoop = Trial_2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank500.started', globalClock.getTime())
        # keep track of which components have finished
        blank500Components = [text]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank500.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Trial_Set_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Set_2.started', globalClock.getTime())
        image_2_set_2.setImage(image_2)
        image_1_set_2.setImage(image)
        Enter_Text_Set_2.setText('Press Enter When Ready')
        Enter_Response_Set_2.keys = []
        Enter_Response_Set_2.rt = []
        _Enter_Response_Set_2_allKeys = []
        # keep track of which components have finished
        Trial_Set_2Components = [Fixation_Set_2, image_2_set_2, image_1_set_2, Recording_Circle_Set_2, Enter_Text_Set_2, Enter_Response_Set_2]
        for thisComponent in Trial_Set_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial_Set_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Set_2* updates
            
            # if Fixation_Set_2 is starting this frame...
            if Fixation_Set_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Set_2.frameNStart = frameN  # exact frame index
                Fixation_Set_2.tStart = t  # local t and not account for scr refresh
                Fixation_Set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Set_2.started')
                # update status
                Fixation_Set_2.status = STARTED
                Fixation_Set_2.setAutoDraw(True)
            
            # if Fixation_Set_2 is active this frame...
            if Fixation_Set_2.status == STARTED:
                # update params
                pass
            
            # if Fixation_Set_2 is stopping this frame...
            if Fixation_Set_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_Set_2.tStartRefresh + .300-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_Set_2.tStop = t  # not accounting for scr refresh
                    Fixation_Set_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Set_2.stopped')
                    # update status
                    Fixation_Set_2.status = FINISHED
                    Fixation_Set_2.setAutoDraw(False)
            
            # *image_2_set_2* updates
            
            # if image_2_set_2 is starting this frame...
            if image_2_set_2.status == NOT_STARTED and tThisFlip >= .450-frameTolerance:
                # keep track of start time/frame for later
                image_2_set_2.frameNStart = frameN  # exact frame index
                image_2_set_2.tStart = t  # local t and not account for scr refresh
                image_2_set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2_set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_set_2.started')
                # update status
                image_2_set_2.status = STARTED
                image_2_set_2.setAutoDraw(True)
            
            # if image_2_set_2 is active this frame...
            if image_2_set_2.status == STARTED:
                # update params
                pass
            
            # *image_1_set_2* updates
            
            # if image_1_set_2 is starting this frame...
            if image_1_set_2.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                image_1_set_2.frameNStart = frameN  # exact frame index
                image_1_set_2.tStart = t  # local t and not account for scr refresh
                image_1_set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1_set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_set_2.started')
                # update status
                image_1_set_2.status = STARTED
                image_1_set_2.setAutoDraw(True)
            
            # if image_1_set_2 is active this frame...
            if image_1_set_2.status == STARTED:
                # update params
                pass
            
            # if image_1_set_2 is stopping this frame...
            if image_1_set_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_1_set_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_1_set_2.tStop = t  # not accounting for scr refresh
                    image_1_set_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_set_2.stopped')
                    # update status
                    image_1_set_2.status = FINISHED
                    image_1_set_2.setAutoDraw(False)
            
            # *Recording_Circle_Set_2* updates
            
            # if Recording_Circle_Set_2 is starting this frame...
            if Recording_Circle_Set_2.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Recording_Circle_Set_2.frameNStart = frameN  # exact frame index
                Recording_Circle_Set_2.tStart = t  # local t and not account for scr refresh
                Recording_Circle_Set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Recording_Circle_Set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Recording_Circle_Set_2.started')
                # update status
                Recording_Circle_Set_2.status = STARTED
                Recording_Circle_Set_2.setAutoDraw(True)
            
            # if Recording_Circle_Set_2 is active this frame...
            if Recording_Circle_Set_2.status == STARTED:
                # update params
                pass
            
            # if Recording_Circle_Set_2 is stopping this frame...
            if Recording_Circle_Set_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Recording_Circle_Set_2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Recording_Circle_Set_2.tStop = t  # not accounting for scr refresh
                    Recording_Circle_Set_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recording_Circle_Set_2.stopped')
                    # update status
                    Recording_Circle_Set_2.status = FINISHED
                    Recording_Circle_Set_2.setAutoDraw(False)
            
            # *Enter_Text_Set_2* updates
            
            # if Enter_Text_Set_2 is starting this frame...
            if Enter_Text_Set_2.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Text_Set_2.frameNStart = frameN  # exact frame index
                Enter_Text_Set_2.tStart = t  # local t and not account for scr refresh
                Enter_Text_Set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Text_Set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Text_Set_2.started')
                # update status
                Enter_Text_Set_2.status = STARTED
                Enter_Text_Set_2.setAutoDraw(True)
            
            # if Enter_Text_Set_2 is active this frame...
            if Enter_Text_Set_2.status == STARTED:
                # update params
                pass
            
            # *Enter_Response_Set_2* updates
            waitOnFlip = False
            
            # if Enter_Response_Set_2 is starting this frame...
            if Enter_Response_Set_2.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Response_Set_2.frameNStart = frameN  # exact frame index
                Enter_Response_Set_2.tStart = t  # local t and not account for scr refresh
                Enter_Response_Set_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Response_Set_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Response_Set_2.started')
                # update status
                Enter_Response_Set_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Enter_Response_Set_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Enter_Response_Set_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Enter_Response_Set_2.status == STARTED and not waitOnFlip:
                theseKeys = Enter_Response_Set_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _Enter_Response_Set_2_allKeys.extend(theseKeys)
                if len(_Enter_Response_Set_2_allKeys):
                    Enter_Response_Set_2.keys = _Enter_Response_Set_2_allKeys[-1].name  # just the last key pressed
                    Enter_Response_Set_2.rt = _Enter_Response_Set_2_allKeys[-1].rt
                    Enter_Response_Set_2.duration = _Enter_Response_Set_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_Set_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Set_2" ---
        for thisComponent in Trial_Set_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Set_2.stopped', globalClock.getTime())
        # check responses
        if Enter_Response_Set_2.keys in ['', [], None]:  # No response was made
            Enter_Response_Set_2.keys = None
        Trial_2.addData('Enter_Response_Set_2.keys',Enter_Response_Set_2.keys)
        if Enter_Response_Set_2.keys != None:  # we had a response
            Trial_2.addData('Enter_Response_Set_2.rt', Enter_Response_Set_2.rt)
            Trial_2.addData('Enter_Response_Set_2.duration', Enter_Response_Set_2.duration)
        # the Routine "Trial_Set_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Trial_2'
    
    
    # --- Prepare to start Routine "betweentrialbreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('betweentrialbreak.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    betweentrialbreakComponents = [text_6, key_resp, ten, nine, eight, seven, six, five, four, three, two, one, text_16end]
    for thisComponent in betweentrialbreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "betweentrialbreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ten* updates
        
        # if ten is starting this frame...
        if ten.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            ten.frameNStart = frameN  # exact frame index
            ten.tStart = t  # local t and not account for scr refresh
            ten.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ten.started')
            # update status
            ten.status = STARTED
            ten.setAutoDraw(True)
        
        # if ten is active this frame...
        if ten.status == STARTED:
            # update params
            pass
        
        # if ten is stopping this frame...
        if ten.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ten.tStop = t  # not accounting for scr refresh
                ten.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ten.stopped')
                # update status
                ten.status = FINISHED
                ten.setAutoDraw(False)
        
        # *nine* updates
        
        # if nine is starting this frame...
        if nine.status == NOT_STARTED and tThisFlip >= 51-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nine.started')
            # update status
            nine.status = STARTED
            nine.setAutoDraw(True)
        
        # if nine is active this frame...
        if nine.status == STARTED:
            # update params
            pass
        
        # if nine is stopping this frame...
        if nine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                nine.tStop = t  # not accounting for scr refresh
                nine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nine.stopped')
                # update status
                nine.status = FINISHED
                nine.setAutoDraw(False)
        
        # *eight* updates
        
        # if eight is starting this frame...
        if eight.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
            # keep track of start time/frame for later
            eight.frameNStart = frameN  # exact frame index
            eight.tStart = t  # local t and not account for scr refresh
            eight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eight.started')
            # update status
            eight.status = STARTED
            eight.setAutoDraw(True)
        
        # if eight is active this frame...
        if eight.status == STARTED:
            # update params
            pass
        
        # if eight is stopping this frame...
        if eight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eight.tStop = t  # not accounting for scr refresh
                eight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eight.stopped')
                # update status
                eight.status = FINISHED
                eight.setAutoDraw(False)
        
        # *seven* updates
        
        # if seven is starting this frame...
        if seven.status == NOT_STARTED and tThisFlip >= 53-frameTolerance:
            # keep track of start time/frame for later
            seven.frameNStart = frameN  # exact frame index
            seven.tStart = t  # local t and not account for scr refresh
            seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'seven.started')
            # update status
            seven.status = STARTED
            seven.setAutoDraw(True)
        
        # if seven is active this frame...
        if seven.status == STARTED:
            # update params
            pass
        
        # if seven is stopping this frame...
        if seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                seven.tStop = t  # not accounting for scr refresh
                seven.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'seven.stopped')
                # update status
                seven.status = FINISHED
                seven.setAutoDraw(False)
        
        # *six* updates
        
        # if six is starting this frame...
        if six.status == NOT_STARTED and tThisFlip >= 54-frameTolerance:
            # keep track of start time/frame for later
            six.frameNStart = frameN  # exact frame index
            six.tStart = t  # local t and not account for scr refresh
            six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'six.started')
            # update status
            six.status = STARTED
            six.setAutoDraw(True)
        
        # if six is active this frame...
        if six.status == STARTED:
            # update params
            pass
        
        # if six is stopping this frame...
        if six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                six.tStop = t  # not accounting for scr refresh
                six.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'six.stopped')
                # update status
                six.status = FINISHED
                six.setAutoDraw(False)
        
        # *five* updates
        
        # if five is starting this frame...
        if five.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            five.frameNStart = frameN  # exact frame index
            five.tStart = t  # local t and not account for scr refresh
            five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'five.started')
            # update status
            five.status = STARTED
            five.setAutoDraw(True)
        
        # if five is active this frame...
        if five.status == STARTED:
            # update params
            pass
        
        # if five is stopping this frame...
        if five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                five.tStop = t  # not accounting for scr refresh
                five.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five.stopped')
                # update status
                five.status = FINISHED
                five.setAutoDraw(False)
        
        # *four* updates
        
        # if four is starting this frame...
        if four.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            four.frameNStart = frameN  # exact frame index
            four.tStart = t  # local t and not account for scr refresh
            four.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'four.started')
            # update status
            four.status = STARTED
            four.setAutoDraw(True)
        
        # if four is active this frame...
        if four.status == STARTED:
            # update params
            pass
        
        # if four is stopping this frame...
        if four.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                four.tStop = t  # not accounting for scr refresh
                four.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'four.stopped')
                # update status
                four.status = FINISHED
                four.setAutoDraw(False)
        
        # *three* updates
        
        # if three is starting this frame...
        if three.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            three.frameNStart = frameN  # exact frame index
            three.tStart = t  # local t and not account for scr refresh
            three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three.started')
            # update status
            three.status = STARTED
            three.setAutoDraw(True)
        
        # if three is active this frame...
        if three.status == STARTED:
            # update params
            pass
        
        # if three is stopping this frame...
        if three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                three.tStop = t  # not accounting for scr refresh
                three.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three.stopped')
                # update status
                three.status = FINISHED
                three.setAutoDraw(False)
        
        # *two* updates
        
        # if two is starting this frame...
        if two.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            two.frameNStart = frameN  # exact frame index
            two.tStart = t  # local t and not account for scr refresh
            two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two.started')
            # update status
            two.status = STARTED
            two.setAutoDraw(True)
        
        # if two is active this frame...
        if two.status == STARTED:
            # update params
            pass
        
        # if two is stopping this frame...
        if two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                two.tStop = t  # not accounting for scr refresh
                two.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two.stopped')
                # update status
                two.status = FINISHED
                two.setAutoDraw(False)
        
        # *one* updates
        
        # if one is starting this frame...
        if one.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one.started')
            # update status
            one.status = STARTED
            one.setAutoDraw(True)
        
        # if one is active this frame...
        if one.status == STARTED:
            # update params
            pass
        
        # if one is stopping this frame...
        if one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                one.tStop = t  # not accounting for scr refresh
                one.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one.stopped')
                # update status
                one.status = FINISHED
                one.setAutoDraw(False)
        
        # *text_16end* updates
        
        # if text_16end is starting this frame...
        if text_16end.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_16end.frameNStart = frameN  # exact frame index
            text_16end.tStart = t  # local t and not account for scr refresh
            text_16end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_16end.started')
            # update status
            text_16end.status = STARTED
            text_16end.setAutoDraw(True)
        
        # if text_16end is active this frame...
        if text_16end.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in betweentrialbreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "betweentrialbreak" ---
    for thisComponent in betweentrialbreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('betweentrialbreak.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "betweentrialbreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "NewSetBegin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('NewSetBegin.started', globalClock.getTime())
    # keep track of which components have finished
    NewSetBeginComponents = [text_NewSet]
    for thisComponent in NewSetBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NewSetBegin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_NewSet* updates
        
        # if text_NewSet is starting this frame...
        if text_NewSet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_NewSet.frameNStart = frameN  # exact frame index
            text_NewSet.tStart = t  # local t and not account for scr refresh
            text_NewSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_NewSet, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_NewSet.started')
            # update status
            text_NewSet.status = STARTED
            text_NewSet.setAutoDraw(True)
        
        # if text_NewSet is active this frame...
        if text_NewSet.status == STARTED:
            # update params
            pass
        
        # if text_NewSet is stopping this frame...
        if text_NewSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_NewSet.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_NewSet.tStop = t  # not accounting for scr refresh
                text_NewSet.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_NewSet.stopped')
                # update status
                text_NewSet.status = FINISHED
                text_NewSet.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NewSetBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NewSetBegin" ---
    for thisComponent in NewSetBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('NewSetBegin.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    Trial_3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_items_s3.csv'),
        seed=None, name='Trial_3')
    thisExp.addLoop(Trial_3)  # add the loop to the experiment
    thisTrial_3 = Trial_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    
    for thisTrial_3 in Trial_3:
        currentLoop = Trial_3
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank500.started', globalClock.getTime())
        # keep track of which components have finished
        blank500Components = [text]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank500.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Trial_Set_3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Set_3.started', globalClock.getTime())
        image_2_set_3.setImage(image_2)
        image_1_set_3.setImage(image_2)
        Enter_Text_Set_3.setText('Press Enter When Ready')
        Enter_Response_Set_3.keys = []
        Enter_Response_Set_3.rt = []
        _Enter_Response_Set_3_allKeys = []
        # keep track of which components have finished
        Trial_Set_3Components = [Fixation_Set_3, image_2_set_3, image_1_set_3, Recording_Circle_Set_3, Enter_Text_Set_3, Enter_Response_Set_3]
        for thisComponent in Trial_Set_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial_Set_3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Set_3* updates
            
            # if Fixation_Set_3 is starting this frame...
            if Fixation_Set_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Set_3.frameNStart = frameN  # exact frame index
                Fixation_Set_3.tStart = t  # local t and not account for scr refresh
                Fixation_Set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Set_3.started')
                # update status
                Fixation_Set_3.status = STARTED
                Fixation_Set_3.setAutoDraw(True)
            
            # if Fixation_Set_3 is active this frame...
            if Fixation_Set_3.status == STARTED:
                # update params
                pass
            
            # if Fixation_Set_3 is stopping this frame...
            if Fixation_Set_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_Set_3.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_Set_3.tStop = t  # not accounting for scr refresh
                    Fixation_Set_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Set_3.stopped')
                    # update status
                    Fixation_Set_3.status = FINISHED
                    Fixation_Set_3.setAutoDraw(False)
            
            # *image_2_set_3* updates
            
            # if image_2_set_3 is starting this frame...
            if image_2_set_3.status == NOT_STARTED and tThisFlip >= .450-frameTolerance:
                # keep track of start time/frame for later
                image_2_set_3.frameNStart = frameN  # exact frame index
                image_2_set_3.tStart = t  # local t and not account for scr refresh
                image_2_set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2_set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_set_3.started')
                # update status
                image_2_set_3.status = STARTED
                image_2_set_3.setAutoDraw(True)
            
            # if image_2_set_3 is active this frame...
            if image_2_set_3.status == STARTED:
                # update params
                pass
            
            # *image_1_set_3* updates
            
            # if image_1_set_3 is starting this frame...
            if image_1_set_3.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                image_1_set_3.frameNStart = frameN  # exact frame index
                image_1_set_3.tStart = t  # local t and not account for scr refresh
                image_1_set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1_set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_set_3.started')
                # update status
                image_1_set_3.status = STARTED
                image_1_set_3.setAutoDraw(True)
            
            # if image_1_set_3 is active this frame...
            if image_1_set_3.status == STARTED:
                # update params
                pass
            
            # if image_1_set_3 is stopping this frame...
            if image_1_set_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_1_set_3.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_1_set_3.tStop = t  # not accounting for scr refresh
                    image_1_set_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_set_3.stopped')
                    # update status
                    image_1_set_3.status = FINISHED
                    image_1_set_3.setAutoDraw(False)
            
            # *Recording_Circle_Set_3* updates
            
            # if Recording_Circle_Set_3 is starting this frame...
            if Recording_Circle_Set_3.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Recording_Circle_Set_3.frameNStart = frameN  # exact frame index
                Recording_Circle_Set_3.tStart = t  # local t and not account for scr refresh
                Recording_Circle_Set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Recording_Circle_Set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Recording_Circle_Set_3.started')
                # update status
                Recording_Circle_Set_3.status = STARTED
                Recording_Circle_Set_3.setAutoDraw(True)
            
            # if Recording_Circle_Set_3 is active this frame...
            if Recording_Circle_Set_3.status == STARTED:
                # update params
                pass
            
            # if Recording_Circle_Set_3 is stopping this frame...
            if Recording_Circle_Set_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Recording_Circle_Set_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Recording_Circle_Set_3.tStop = t  # not accounting for scr refresh
                    Recording_Circle_Set_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recording_Circle_Set_3.stopped')
                    # update status
                    Recording_Circle_Set_3.status = FINISHED
                    Recording_Circle_Set_3.setAutoDraw(False)
            
            # *Enter_Text_Set_3* updates
            
            # if Enter_Text_Set_3 is starting this frame...
            if Enter_Text_Set_3.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Text_Set_3.frameNStart = frameN  # exact frame index
                Enter_Text_Set_3.tStart = t  # local t and not account for scr refresh
                Enter_Text_Set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Text_Set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Text_Set_3.started')
                # update status
                Enter_Text_Set_3.status = STARTED
                Enter_Text_Set_3.setAutoDraw(True)
            
            # if Enter_Text_Set_3 is active this frame...
            if Enter_Text_Set_3.status == STARTED:
                # update params
                pass
            
            # *Enter_Response_Set_3* updates
            waitOnFlip = False
            
            # if Enter_Response_Set_3 is starting this frame...
            if Enter_Response_Set_3.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Response_Set_3.frameNStart = frameN  # exact frame index
                Enter_Response_Set_3.tStart = t  # local t and not account for scr refresh
                Enter_Response_Set_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Response_Set_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Response_Set_3.started')
                # update status
                Enter_Response_Set_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Enter_Response_Set_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Enter_Response_Set_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Enter_Response_Set_3.status == STARTED and not waitOnFlip:
                theseKeys = Enter_Response_Set_3.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _Enter_Response_Set_3_allKeys.extend(theseKeys)
                if len(_Enter_Response_Set_3_allKeys):
                    Enter_Response_Set_3.keys = _Enter_Response_Set_3_allKeys[-1].name  # just the last key pressed
                    Enter_Response_Set_3.rt = _Enter_Response_Set_3_allKeys[-1].rt
                    Enter_Response_Set_3.duration = _Enter_Response_Set_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_Set_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Set_3" ---
        for thisComponent in Trial_Set_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Set_3.stopped', globalClock.getTime())
        # check responses
        if Enter_Response_Set_3.keys in ['', [], None]:  # No response was made
            Enter_Response_Set_3.keys = None
        Trial_3.addData('Enter_Response_Set_3.keys',Enter_Response_Set_3.keys)
        if Enter_Response_Set_3.keys != None:  # we had a response
            Trial_3.addData('Enter_Response_Set_3.rt', Enter_Response_Set_3.rt)
            Trial_3.addData('Enter_Response_Set_3.duration', Enter_Response_Set_3.duration)
        # the Routine "Trial_Set_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Trial_3'
    
    
    # --- Prepare to start Routine "betweentrialbreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('betweentrialbreak.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    betweentrialbreakComponents = [text_6, key_resp, ten, nine, eight, seven, six, five, four, three, two, one, text_16end]
    for thisComponent in betweentrialbreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "betweentrialbreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *ten* updates
        
        # if ten is starting this frame...
        if ten.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            ten.frameNStart = frameN  # exact frame index
            ten.tStart = t  # local t and not account for scr refresh
            ten.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ten.started')
            # update status
            ten.status = STARTED
            ten.setAutoDraw(True)
        
        # if ten is active this frame...
        if ten.status == STARTED:
            # update params
            pass
        
        # if ten is stopping this frame...
        if ten.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                ten.tStop = t  # not accounting for scr refresh
                ten.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ten.stopped')
                # update status
                ten.status = FINISHED
                ten.setAutoDraw(False)
        
        # *nine* updates
        
        # if nine is starting this frame...
        if nine.status == NOT_STARTED and tThisFlip >= 51-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nine.started')
            # update status
            nine.status = STARTED
            nine.setAutoDraw(True)
        
        # if nine is active this frame...
        if nine.status == STARTED:
            # update params
            pass
        
        # if nine is stopping this frame...
        if nine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                nine.tStop = t  # not accounting for scr refresh
                nine.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nine.stopped')
                # update status
                nine.status = FINISHED
                nine.setAutoDraw(False)
        
        # *eight* updates
        
        # if eight is starting this frame...
        if eight.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
            # keep track of start time/frame for later
            eight.frameNStart = frameN  # exact frame index
            eight.tStart = t  # local t and not account for scr refresh
            eight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eight.started')
            # update status
            eight.status = STARTED
            eight.setAutoDraw(True)
        
        # if eight is active this frame...
        if eight.status == STARTED:
            # update params
            pass
        
        # if eight is stopping this frame...
        if eight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                eight.tStop = t  # not accounting for scr refresh
                eight.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eight.stopped')
                # update status
                eight.status = FINISHED
                eight.setAutoDraw(False)
        
        # *seven* updates
        
        # if seven is starting this frame...
        if seven.status == NOT_STARTED and tThisFlip >= 53-frameTolerance:
            # keep track of start time/frame for later
            seven.frameNStart = frameN  # exact frame index
            seven.tStart = t  # local t and not account for scr refresh
            seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'seven.started')
            # update status
            seven.status = STARTED
            seven.setAutoDraw(True)
        
        # if seven is active this frame...
        if seven.status == STARTED:
            # update params
            pass
        
        # if seven is stopping this frame...
        if seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                seven.tStop = t  # not accounting for scr refresh
                seven.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'seven.stopped')
                # update status
                seven.status = FINISHED
                seven.setAutoDraw(False)
        
        # *six* updates
        
        # if six is starting this frame...
        if six.status == NOT_STARTED and tThisFlip >= 54-frameTolerance:
            # keep track of start time/frame for later
            six.frameNStart = frameN  # exact frame index
            six.tStart = t  # local t and not account for scr refresh
            six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'six.started')
            # update status
            six.status = STARTED
            six.setAutoDraw(True)
        
        # if six is active this frame...
        if six.status == STARTED:
            # update params
            pass
        
        # if six is stopping this frame...
        if six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                six.tStop = t  # not accounting for scr refresh
                six.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'six.stopped')
                # update status
                six.status = FINISHED
                six.setAutoDraw(False)
        
        # *five* updates
        
        # if five is starting this frame...
        if five.status == NOT_STARTED and tThisFlip >= 55-frameTolerance:
            # keep track of start time/frame for later
            five.frameNStart = frameN  # exact frame index
            five.tStart = t  # local t and not account for scr refresh
            five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'five.started')
            # update status
            five.status = STARTED
            five.setAutoDraw(True)
        
        # if five is active this frame...
        if five.status == STARTED:
            # update params
            pass
        
        # if five is stopping this frame...
        if five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                five.tStop = t  # not accounting for scr refresh
                five.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five.stopped')
                # update status
                five.status = FINISHED
                five.setAutoDraw(False)
        
        # *four* updates
        
        # if four is starting this frame...
        if four.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            four.frameNStart = frameN  # exact frame index
            four.tStart = t  # local t and not account for scr refresh
            four.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'four.started')
            # update status
            four.status = STARTED
            four.setAutoDraw(True)
        
        # if four is active this frame...
        if four.status == STARTED:
            # update params
            pass
        
        # if four is stopping this frame...
        if four.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                four.tStop = t  # not accounting for scr refresh
                four.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'four.stopped')
                # update status
                four.status = FINISHED
                four.setAutoDraw(False)
        
        # *three* updates
        
        # if three is starting this frame...
        if three.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            three.frameNStart = frameN  # exact frame index
            three.tStart = t  # local t and not account for scr refresh
            three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'three.started')
            # update status
            three.status = STARTED
            three.setAutoDraw(True)
        
        # if three is active this frame...
        if three.status == STARTED:
            # update params
            pass
        
        # if three is stopping this frame...
        if three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                three.tStop = t  # not accounting for scr refresh
                three.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'three.stopped')
                # update status
                three.status = FINISHED
                three.setAutoDraw(False)
        
        # *two* updates
        
        # if two is starting this frame...
        if two.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            two.frameNStart = frameN  # exact frame index
            two.tStart = t  # local t and not account for scr refresh
            two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'two.started')
            # update status
            two.status = STARTED
            two.setAutoDraw(True)
        
        # if two is active this frame...
        if two.status == STARTED:
            # update params
            pass
        
        # if two is stopping this frame...
        if two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                two.tStop = t  # not accounting for scr refresh
                two.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'two.stopped')
                # update status
                two.status = FINISHED
                two.setAutoDraw(False)
        
        # *one* updates
        
        # if one is starting this frame...
        if one.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one.started')
            # update status
            one.status = STARTED
            one.setAutoDraw(True)
        
        # if one is active this frame...
        if one.status == STARTED:
            # update params
            pass
        
        # if one is stopping this frame...
        if one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                one.tStop = t  # not accounting for scr refresh
                one.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'one.stopped')
                # update status
                one.status = FINISHED
                one.setAutoDraw(False)
        
        # *text_16end* updates
        
        # if text_16end is starting this frame...
        if text_16end.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            text_16end.frameNStart = frameN  # exact frame index
            text_16end.tStart = t  # local t and not account for scr refresh
            text_16end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_16end.started')
            # update status
            text_16end.status = STARTED
            text_16end.setAutoDraw(True)
        
        # if text_16end is active this frame...
        if text_16end.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in betweentrialbreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "betweentrialbreak" ---
    for thisComponent in betweentrialbreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('betweentrialbreak.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "betweentrialbreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "NewSetBegin" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('NewSetBegin.started', globalClock.getTime())
    # keep track of which components have finished
    NewSetBeginComponents = [text_NewSet]
    for thisComponent in NewSetBeginComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NewSetBegin" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_NewSet* updates
        
        # if text_NewSet is starting this frame...
        if text_NewSet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_NewSet.frameNStart = frameN  # exact frame index
            text_NewSet.tStart = t  # local t and not account for scr refresh
            text_NewSet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_NewSet, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_NewSet.started')
            # update status
            text_NewSet.status = STARTED
            text_NewSet.setAutoDraw(True)
        
        # if text_NewSet is active this frame...
        if text_NewSet.status == STARTED:
            # update params
            pass
        
        # if text_NewSet is stopping this frame...
        if text_NewSet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_NewSet.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_NewSet.tStop = t  # not accounting for scr refresh
                text_NewSet.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_NewSet.stopped')
                # update status
                text_NewSet.status = FINISHED
                text_NewSet.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NewSetBeginComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NewSetBegin" ---
    for thisComponent in NewSetBeginComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('NewSetBegin.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    Trial_4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_items_s4.csv'),
        seed=None, name='Trial_4')
    thisExp.addLoop(Trial_4)  # add the loop to the experiment
    thisTrial_4 = Trial_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            globals()[paramName] = thisTrial_4[paramName]
    
    for thisTrial_4 in Trial_4:
        currentLoop = Trial_4
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                globals()[paramName] = thisTrial_4[paramName]
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank500.started', globalClock.getTime())
        # keep track of which components have finished
        blank500Components = [text]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank500.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "Trial_Set_4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Set_4.started', globalClock.getTime())
        image_2_set_4.setImage(image_2)
        image_1_set_4.setImage(image)
        Enter_Text_Set_4.setText('Press Enter When Ready')
        Enter_Response_Set_4.keys = []
        Enter_Response_Set_4.rt = []
        _Enter_Response_Set_4_allKeys = []
        # keep track of which components have finished
        Trial_Set_4Components = [Fixation_Set_4, image_2_set_4, image_1_set_4, Recording_Circle_Set_4, Enter_Text_Set_4, Enter_Response_Set_4]
        for thisComponent in Trial_Set_4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial_Set_4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Set_4* updates
            
            # if Fixation_Set_4 is starting this frame...
            if Fixation_Set_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Set_4.frameNStart = frameN  # exact frame index
                Fixation_Set_4.tStart = t  # local t and not account for scr refresh
                Fixation_Set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Set_4.started')
                # update status
                Fixation_Set_4.status = STARTED
                Fixation_Set_4.setAutoDraw(True)
            
            # if Fixation_Set_4 is active this frame...
            if Fixation_Set_4.status == STARTED:
                # update params
                pass
            
            # if Fixation_Set_4 is stopping this frame...
            if Fixation_Set_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_Set_4.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_Set_4.tStop = t  # not accounting for scr refresh
                    Fixation_Set_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Set_4.stopped')
                    # update status
                    Fixation_Set_4.status = FINISHED
                    Fixation_Set_4.setAutoDraw(False)
            
            # *image_2_set_4* updates
            
            # if image_2_set_4 is starting this frame...
            if image_2_set_4.status == NOT_STARTED and tThisFlip >= .450-frameTolerance:
                # keep track of start time/frame for later
                image_2_set_4.frameNStart = frameN  # exact frame index
                image_2_set_4.tStart = t  # local t and not account for scr refresh
                image_2_set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2_set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_set_4.started')
                # update status
                image_2_set_4.status = STARTED
                image_2_set_4.setAutoDraw(True)
            
            # if image_2_set_4 is active this frame...
            if image_2_set_4.status == STARTED:
                # update params
                pass
            
            # *image_1_set_4* updates
            
            # if image_1_set_4 is starting this frame...
            if image_1_set_4.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                image_1_set_4.frameNStart = frameN  # exact frame index
                image_1_set_4.tStart = t  # local t and not account for scr refresh
                image_1_set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1_set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_set_4.started')
                # update status
                image_1_set_4.status = STARTED
                image_1_set_4.setAutoDraw(True)
            
            # if image_1_set_4 is active this frame...
            if image_1_set_4.status == STARTED:
                # update params
                pass
            
            # if image_1_set_4 is stopping this frame...
            if image_1_set_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_1_set_4.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_1_set_4.tStop = t  # not accounting for scr refresh
                    image_1_set_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_set_4.stopped')
                    # update status
                    image_1_set_4.status = FINISHED
                    image_1_set_4.setAutoDraw(False)
            
            # *Recording_Circle_Set_4* updates
            
            # if Recording_Circle_Set_4 is starting this frame...
            if Recording_Circle_Set_4.status == NOT_STARTED and tThisFlip >= .3-frameTolerance:
                # keep track of start time/frame for later
                Recording_Circle_Set_4.frameNStart = frameN  # exact frame index
                Recording_Circle_Set_4.tStart = t  # local t and not account for scr refresh
                Recording_Circle_Set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Recording_Circle_Set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Recording_Circle_Set_4.started')
                # update status
                Recording_Circle_Set_4.status = STARTED
                Recording_Circle_Set_4.setAutoDraw(True)
            
            # if Recording_Circle_Set_4 is active this frame...
            if Recording_Circle_Set_4.status == STARTED:
                # update params
                pass
            
            # if Recording_Circle_Set_4 is stopping this frame...
            if Recording_Circle_Set_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Recording_Circle_Set_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Recording_Circle_Set_4.tStop = t  # not accounting for scr refresh
                    Recording_Circle_Set_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Recording_Circle_Set_4.stopped')
                    # update status
                    Recording_Circle_Set_4.status = FINISHED
                    Recording_Circle_Set_4.setAutoDraw(False)
            
            # *Enter_Text_Set_4* updates
            
            # if Enter_Text_Set_4 is starting this frame...
            if Enter_Text_Set_4.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Text_Set_4.frameNStart = frameN  # exact frame index
                Enter_Text_Set_4.tStart = t  # local t and not account for scr refresh
                Enter_Text_Set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Text_Set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Text_Set_4.started')
                # update status
                Enter_Text_Set_4.status = STARTED
                Enter_Text_Set_4.setAutoDraw(True)
            
            # if Enter_Text_Set_4 is active this frame...
            if Enter_Text_Set_4.status == STARTED:
                # update params
                pass
            
            # *Enter_Response_Set_4* updates
            waitOnFlip = False
            
            # if Enter_Response_Set_4 is starting this frame...
            if Enter_Response_Set_4.status == NOT_STARTED and tThisFlip >= 4.3-frameTolerance:
                # keep track of start time/frame for later
                Enter_Response_Set_4.frameNStart = frameN  # exact frame index
                Enter_Response_Set_4.tStart = t  # local t and not account for scr refresh
                Enter_Response_Set_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Enter_Response_Set_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Enter_Response_Set_4.started')
                # update status
                Enter_Response_Set_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Enter_Response_Set_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Enter_Response_Set_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Enter_Response_Set_4.status == STARTED and not waitOnFlip:
                theseKeys = Enter_Response_Set_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _Enter_Response_Set_4_allKeys.extend(theseKeys)
                if len(_Enter_Response_Set_4_allKeys):
                    Enter_Response_Set_4.keys = _Enter_Response_Set_4_allKeys[-1].name  # just the last key pressed
                    Enter_Response_Set_4.rt = _Enter_Response_Set_4_allKeys[-1].rt
                    Enter_Response_Set_4.duration = _Enter_Response_Set_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_Set_4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Set_4" ---
        for thisComponent in Trial_Set_4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Set_4.stopped', globalClock.getTime())
        # check responses
        if Enter_Response_Set_4.keys in ['', [], None]:  # No response was made
            Enter_Response_Set_4.keys = None
        Trial_4.addData('Enter_Response_Set_4.keys',Enter_Response_Set_4.keys)
        if Enter_Response_Set_4.keys != None:  # we had a response
            Trial_4.addData('Enter_Response_Set_4.rt', Enter_Response_Set_4.rt)
            Trial_4.addData('Enter_Response_Set_4.duration', Enter_Response_Set_4.duration)
        # the Routine "Trial_Set_4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'Trial_4'
    
    
    # --- Prepare to start Routine "goodbye" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('goodbye.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    goodbyeComponents = [textGoodbye, key_resp_2]
    for thisComponent in goodbyeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "goodbye" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textGoodbye* updates
        
        # if textGoodbye is starting this frame...
        if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textGoodbye.frameNStart = frameN  # exact frame index
            textGoodbye.tStart = t  # local t and not account for scr refresh
            textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textGoodbye.started')
            # update status
            textGoodbye.status = STARTED
            textGoodbye.setAutoDraw(True)
        
        # if textGoodbye is active this frame...
        if textGoodbye.status == STARTED:
            # update params
            pass
        
        # if textGoodbye is stopping this frame...
        if textGoodbye.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textGoodbye.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                textGoodbye.tStop = t  # not accounting for scr refresh
                textGoodbye.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textGoodbye.stopped')
                # update status
                textGoodbye.status = FINISHED
                textGoodbye.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2 is stopping this frame...
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                # update status
                key_resp_2.status = FINISHED
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in goodbyeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbye" ---
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('goodbye.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
