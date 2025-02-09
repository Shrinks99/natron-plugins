# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# Natron PyPlug
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Grain_AdvancedExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Grain_AdvancedExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.hw.grainadvanced"

def getLabel():
    return "Grain_Advanced"

def getVersion():
    return 1

def getGrouping():
    return "Filters"

def getPluginDescription():
    return "Applies user-definable film grain to an image\t"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.8, 0.502, 0.298)

    # Create the user parameters
    lastNode.Grain = lastNode.createPageParam("Grain", "Grain")
    param = lastNode.createIntParam("seed", "Seed")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0, 0)
    param.setDefaultValue(128, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Change this value to make different instances of this operator produce different noise.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.seed = param
    del param

    param = lastNode.createSeparatorParam("label_size", "Size")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_size = param
    del param

    param = lastNode.createDoubleParam("red_size", "Red")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(0.4, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.red_size = param
    del param

    param = lastNode.createDoubleParam("green_size", "Green")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(0.6, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.green_size = param
    del param

    param = lastNode.createDoubleParam("blue_size", "Blue")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(20, 0)
    param.setDefaultValue(1.6, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.blue_size = param
    del param

    param = lastNode.createDoubleParam("irregularity", "Irregularity")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.6, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.irregularity = param
    del param

    param = lastNode.createSeparatorParam("label_brights", "Intensity Bright")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_brights = param
    del param

    param = lastNode.createDoubleParam("red_m", "Red")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.15, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of red grain to add to a white pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.red_m = param
    del param

    param = lastNode.createDoubleParam("green_m", "Green")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.15, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of green grain to add to a white pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.green_m = param
    del param

    param = lastNode.createDoubleParam("blue_m", "Blue")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of blue grain to add to a white pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.blue_m = param
    del param

    param = lastNode.createSeparatorParam("label_darks", "Intensity Darks")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_darks = param
    del param

    param = lastNode.createDoubleParam("red_i", "Red")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0.2, 0)
    param.setDefaultValue(0.025, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of red grain to add to a black pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.red_i = param
    del param

    param = lastNode.createDoubleParam("green_i", "Green")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0.2, 0)
    param.setDefaultValue(0.01, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of green grain to add to a black pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.green_i = param
    del param

    param = lastNode.createDoubleParam("blue_i", "Blue")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0.2, 0)
    param.setDefaultValue(0.03, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Amount of blue grain to add to a black pixel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.blue_i = param
    del param

    param = lastNode.createSeparatorParam("label_softness", "Softness")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_softness = param
    del param

    param = lastNode.createDoubleParam("red_soft", "Red")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1.3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Blur the red channel of the grain.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.red_soft = param
    del param

    param = lastNode.createDoubleParam("green_soft", "Green")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1.1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Blur the green channel of the grain.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.green_soft = param
    del param

    param = lastNode.createDoubleParam("blue_soft", "Blue")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1.3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Blur the blue channel of the grain.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.blue_soft = param
    del param

    param = lastNode.createSeparatorParam("label_controls", "Global Controls")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_controls = param
    del param

    param = lastNode.createDoubleParam("Saturation1saturation", "Grain Saturation")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.85, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Control the grain\'s saturation.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Saturation1saturation = param
    del param

    param = lastNode.createChoiceParam("Saturation1luminanceMath", "Luminance Math")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Formula used to compute luminance from RGB values.  This only affects the grain saturation control.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Saturation1luminanceMath = param
    del param

    param = lastNode.createDouble2DParam("Scale_Ratioscale", "Aspect Ratio")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(2, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Edit the aspect ratio of the grain to match anamorphic plates")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Scale_Ratioscale = param
    del param

    param = lastNode.createBooleanParam("apply_alpha", "Alpha Masked")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Only apply grain to areas with alpha in the main input.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.apply_alpha = param
    del param

    param = lastNode.createBooleanParam("Merge4maskInvert", "Invert Alpha")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Inverts the alpha channel of the main input.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Merge4maskInvert = param
    del param

    param = lastNode.createBooleanParam("KeyMix1maskInvert", "Invert Mask")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Inverts the alpha channel of the mask input.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.KeyMix1maskInvert = param
    del param

    param = lastNode.createDoubleParam("Merge4mix", "Mix")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("Mix factor between the original and grained image.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Merge4mix = param
    del param

    param = lastNode.createSeparatorParam("label_credits", "")

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.label_credits = param
    del param

    param = lastNode.createStringParam("credits", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("Original node by <b>SPIN<span style=\"color:#b32026\">VFX</span></b> - 2017, Natron port by Henry Wilkinson - 2021")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Grain.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.credits = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Grain', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "SeNoise_red"
    lastNode = app.createNode("net.sf.openfx.SeNoise", 1, group)
    lastNode.setScriptName("SeNoise_red")
    lastNode.setLabel("SeNoise_red")
    lastNode.setPosition(921, 510)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.75, 0.75, 0.75)
    groupSeNoise_red = lastNode

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("replace")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("noiseSize")
    if param is not None:
        param.setValue(0.4, 0)
        param.setValue(0.4, 1)
        del param

    param = lastNode.getParam("noiseZ")
    if param is not None:
        param.setValue(129.3, 0)
        del param

    param = lastNode.getParam("fbmOctaves")
    if param is not None:
        param.setValue(2, 0)
        del param

    del lastNode
    # End of node "SeNoise_red"

    # Start of node "SeNoise_green"
    lastNode = app.createNode("net.sf.openfx.SeNoise", 1, group)
    lastNode.setScriptName("SeNoise_green")
    lastNode.setLabel("SeNoise_green")
    lastNode.setPosition(921, 586)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.75, 0.75, 0.75)
    groupSeNoise_green = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("replace")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("noiseSize")
    if param is not None:
        param.setValue(0.6, 0)
        param.setValue(0.6, 1)
        del param

    param = lastNode.getParam("noiseZ")
    if param is not None:
        param.setValue(135.3, 0)
        del param

    param = lastNode.getParam("fbmOctaves")
    if param is not None:
        param.setValue(2, 0)
        del param

    del lastNode
    # End of node "SeNoise_green"

    # Start of node "SeNoise_blue"
    lastNode = app.createNode("net.sf.openfx.SeNoise", 1, group)
    lastNode.setScriptName("SeNoise_blue")
    lastNode.setLabel("SeNoise_blue")
    lastNode.setPosition(921, 662)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.75, 0.75, 0.75)
    groupSeNoise_blue = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("replace")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("noiseSize")
    if param is not None:
        param.setValue(1.6, 0)
        param.setValue(1.6, 1)
        del param

    param = lastNode.getParam("noiseZ")
    if param is not None:
        param.setValue(385.3, 0)
        del param

    param = lastNode.getParam("fbmOctaves")
    if param is not None:
        param.setValue(2, 0)
        del param

    del lastNode
    # End of node "SeNoise_blue"

    # Start of node "Scale_Ratio"
    lastNode = app.createNode("net.sf.openfx.TransformPlugin", 1, group)
    lastNode.setScriptName("Scale_Ratio")
    lastNode.setLabel("Scale_Ratio")
    lastNode.setPosition(921, 751)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupScale_Ratio = lastNode

    del lastNode
    # End of node "Scale_Ratio"

    # Start of node "Blur_red"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_red")
    lastNode.setLabel("Blur_red")
    lastNode.setPosition(921, 825)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_red = lastNode

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1.3, 0)
        param.setValue(1.3, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("nearest")
        del param

    del lastNode
    # End of node "Blur_red"

    # Start of node "Blur_green"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_green")
    lastNode.setLabel("Blur_green")
    lastNode.setPosition(921, 879)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_green = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1.1, 0)
        param.setValue(1.1, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("nearest")
        del param

    del lastNode
    # End of node "Blur_green"

    # Start of node "Blur_blue"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur_blue")
    lastNode.setLabel("Blur_blue")
    lastNode.setPosition(921, 936)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_blue = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(1.3, 0)
        param.setValue(1.3, 1)
        del param

    param = lastNode.getParam("boundary")
    if param is not None:
        param.set("nearest")
        del param

    del lastNode
    # End of node "Blur_blue"

    # Start of node "Grade1"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade1")
    lastNode.setLabel("Grade1")
    lastNode.setPosition(921, 1026)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade1 = lastNode

    param = lastNode.getParam("multiply")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        param.setValue(2, 2)
        param.setValue(2, 3)
        del param

    param = lastNode.getParam("offset")
    if param is not None:
        param.setValue(-1, 0)
        param.setValue(-1, 1)
        param.setValue(-1, 2)
        param.setValue(-1, 3)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade1"

    # Start of node "Merge3"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge3")
    lastNode.setLabel("Merge3")
    lastNode.setPosition(921, 1157)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge3 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("b")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge3"

    # Start of node "Grade4"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade4")
    lastNode.setLabel("Grade4")
    lastNode.setPosition(754, 1168)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade4 = lastNode

    param = lastNode.getParam("black")
    if param is not None:
        param.setValue(0.025, 0)
        param.setValue(0.01, 1)
        param.setValue(0.03, 2)
        del param

    param = lastNode.getParam("white")
    if param is not None:
        param.setValue(0.15, 0)
        param.setValue(0.15, 1)
        param.setValue(0.2, 2)
        param.setValue(0, 3)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade4"

    # Start of node "Saturation1"
    lastNode = app.createNode("net.sf.openfx.SaturationPlugin", 2, group)
    lastNode.setScriptName("Saturation1")
    lastNode.setLabel("Saturation1")
    lastNode.setPosition(921, 1299)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupSaturation1 = lastNode

    param = lastNode.getParam("saturation")
    if param is not None:
        param.setValue(0.85, 0)
        del param

    param = lastNode.getParam("clampBlack")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Saturation1"

    # Start of node "Merge4"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge4")
    lastNode.setLabel("Merge4")
    lastNode.setPosition(551, 1390)
    lastNode.setSize(80, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge4 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("plus")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("b")
        del param

    param = lastNode.getParam("OutputChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge4"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(954, 1410)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Give_Alpha"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Give_Alpha")
    lastNode.setLabel("Give Alpha")
    lastNode.setPosition(330, 818)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupGive_Alpha = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("1")
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Give_Alpha"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(363, 1410)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "KeyMix1"
    lastNode = app.createNode("net.sf.openfx.KeyMix", 1, group)
    lastNode.setScriptName("KeyMix1")
    lastNode.setLabel("KeyMix1")
    lastNode.setPosition(553, 1575)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupKeyMix1 = lastNode

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "KeyMix1"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(923, 1575)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Mask"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(553, 1709)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Input"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input")
    lastNode.setLabel("Input")
    lastNode.setPosition(551, 299)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput = lastNode

    del lastNode
    # End of node "Input"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(584, 423)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(787, 423)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(363, 423)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(173, 1584)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(173, 423)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Dot8"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot8")
    lastNode.setLabel("Dot8")
    lastNode.setPosition(954, 423)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot8 = lastNode

    del lastNode
    # End of node "Dot8"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(746, 1575)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Clamp2"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp2")
    lastNode.setLabel("Clamp2")
    lastNode.setPosition(921, 1351)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp2 = lastNode

    param = lastNode.getParam("maximumEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Clamp2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupSeNoise_red.connectInput(0, groupDot8)
    groupSeNoise_green.connectInput(0, groupSeNoise_red)
    groupSeNoise_blue.connectInput(0, groupSeNoise_green)
    groupScale_Ratio.connectInput(0, groupSeNoise_blue)
    groupBlur_red.connectInput(0, groupScale_Ratio)
    groupBlur_green.connectInput(0, groupBlur_red)
    groupBlur_blue.connectInput(0, groupBlur_green)
    groupGrade1.connectInput(0, groupBlur_blue)
    groupMerge3.connectInput(0, groupGrade4)
    groupMerge3.connectInput(1, groupGrade1)
    groupGrade4.connectInput(0, groupDot4)
    groupSaturation1.connectInput(0, groupMerge3)
    groupMerge4.connectInput(0, groupDot3)
    groupMerge4.connectInput(1, groupDot1)
    groupMerge4.connectInput(2, groupDot2)
    groupDot1.connectInput(0, groupClamp2)
    groupGive_Alpha.connectInput(0, groupDot5)
    groupDot2.connectInput(0, groupGive_Alpha)
    groupKeyMix1.connectInput(0, groupMerge4)
    groupKeyMix1.connectInput(1, groupDot6)
    groupKeyMix1.connectInput(2, groupInvert1)
    groupOutput1.connectInput(0, groupKeyMix1)
    groupDot3.connectInput(0, groupInput)
    groupDot4.connectInput(0, groupDot3)
    groupDot5.connectInput(0, groupDot3)
    groupDot6.connectInput(0, groupDot7)
    groupDot7.connectInput(0, groupDot5)
    groupDot8.connectInput(0, groupDot4)
    groupInvert1.connectInput(0, groupMask)
    groupClamp2.connectInput(0, groupSaturation1)

    param = groupSeNoise_red.getParam("noiseSize")
    param.setExpression("thisGroup.red_size.get()", False, 0)
    param.setExpression("thisGroup.red_size.get()", False, 1)
    del param
    param = groupSeNoise_red.getParam("noiseZ")
    param.setExpression("frame+thisGroup.seed.get()+(thisGroup.irregularity.get()/2)", False, 0)
    del param
    param = groupSeNoise_green.getParam("noiseSize")
    param.setExpression("thisGroup.green_size.get()", False, 0)
    param.setExpression("thisGroup.green_size.get()", False, 1)
    del param
    param = groupSeNoise_green.getParam("noiseZ")
    param.setExpression("frame+6+thisGroup.seed.get()+(thisGroup.irregularity.get()/2)", False, 0)
    del param
    param = groupSeNoise_blue.getParam("noiseSize")
    param.setExpression("thisGroup.blue_size.get()", False, 0)
    param.setExpression("thisGroup.blue_size.get()", False, 1)
    del param
    param = groupSeNoise_blue.getParam("noiseZ")
    param.setExpression("frame+(3*thisGroup.seed.get())+(thisGroup.irregularity.get()/2)", False, 0)
    del param
    param = groupScale_Ratio.getParam("scale")
    group.getParam("Scale_Ratioscale").setAsAlias(param)
    del param
    param = groupBlur_red.getParam("size")
    param.setExpression("thisGroup.red_soft.get()", False, 0)
    param.setExpression("thisGroup.red_soft.get()", False, 1)
    del param
    param = groupBlur_green.getParam("size")
    param.setExpression("thisGroup.green_soft.get()", False, 0)
    param.setExpression("thisGroup.green_soft.get()", False, 1)
    del param
    param = groupBlur_blue.getParam("size")
    param.setExpression("thisGroup.blue_soft.get()", False, 0)
    param.setExpression("thisGroup.blue_soft.get()", False, 1)
    del param
    param = groupGrade4.getParam("black")
    param.setExpression("thisGroup.red_i.get()", False, 0)
    param.setExpression("thisGroup.green_i.get()", False, 1)
    param.setExpression("thisGroup.blue_i.get()", False, 2)
    del param
    param = groupGrade4.getParam("white")
    param.setExpression("thisGroup.red_m.get()", False, 0)
    param.setExpression("thisGroup.green_m.get()", False, 1)
    param.setExpression("thisGroup.blue_m.get()", False, 2)
    del param
    param = groupSaturation1.getParam("saturation")
    group.getParam("Saturation1saturation").setAsAlias(param)
    del param
    param = groupSaturation1.getParam("luminanceMath")
    group.getParam("Saturation1luminanceMath").setAsAlias(param)
    del param
    param = groupMerge4.getParam("maskInvert")
    group.getParam("Merge4maskInvert").setAsAlias(param)
    del param
    param = groupMerge4.getParam("mix")
    group.getParam("Merge4mix").setAsAlias(param)
    del param
    param = groupGive_Alpha.getParam("disableNode")
    param.setExpression("thisGroup.apply_alpha.get()", False, 0)
    del param
    param = groupKeyMix1.getParam("maskInvert")
    group.getParam("KeyMix1maskInvert").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Grain_AdvancedExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
