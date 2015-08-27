#utf-8
#tested in python 2.7.10 - Daniel Sifton

import os
import wx
from bs4 import BeautifulSoup 
import csv
import time
import re 
import requests 
from selenium import webdriver

#we reassign these global variables inside the button functions: 
vendoropengui = 0 
csvopengui = 0
csvsavegui = 0

#modify your i/o paths below or uncomment and reset defaultDir=self.currentDirectory:
vendorpath = "/Users/daniel/Desktop/wxBits/vendors/"
csvinpath  = "/Users/daniel/Desktop/wxBits/input/" 
csvoutpath = "/Users/daniel/Desktop/wxBits/output/"



########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Inquisitor Mark One", size=(470, 237), style=wx.MINIMIZE_BOX | wx.CAPTION |  wx.CLOSE_BOX) 
                           #size controls for frame [and the image] 
        panel = wx.Panel(self, wx.ID_ANY,)
        #self.currentDirectory = os.getcwd()wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX 

        openFileDlgBtnV = wx.Button(panel, label="Vendor Input") 
        openFileDlgBtnV.Bind(wx.EVT_BUTTON, self.onOpenFileV)

        openFileDlgBtn = wx.Button(panel, label=".csv Input")
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
 
        saveFileDlgBtn = wx.Button(panel, label=".csv Output")
        saveFileDlgBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)

        startButton = wx.Button(panel, label="Start")
        self.Bind(wx.EVT_BUTTON, self.startButton)
      
      
        sizer = wx.BoxSizer(wx.VERTICAL) 

        sizer.Add(openFileDlgBtnV, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(openFileDlgBtn, 2, wx.ALL|wx.LEFT, 3)
        sizer.Add(saveFileDlgBtn, 2, wx.ALL|wx.LEFT, 3)

        sizer.Add(startButton, 2, wx.ALL|wx.LEFT, 3)
    
        panel.SetSizer(sizer)
        self.CreateStatusBar()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

 

    #----------------------------------------------------------------------
    def onOpenFileV(self, event): 
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a vendor file",
            defaultDir=vendorpath,
            defaultFile="",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.SetStatusText("You chose: %s" % path)
                global vendoropengui
                vendoropengui = path
                return vendoropengui
        dlg.Destroy()


    #----------------------------------------------------------------------
    def onOpenFile(self, event): 
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=csvinpath, 
            defaultFile="",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.SetStatusText("You chose: %s" % path)
                global csvopengui
                csvopengui = path
                return csvopengui          
        dlg.Destroy()
 
    #----------------------------------------------------------------------
    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Save file as ...(.csv)", 
            defaultDir=csvoutpath, 
            defaultFile="", 
            style=wx.SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.SetStatusText("You chose: %s" % path)
            global csvsavegui
            csvsavegui = path
            return csvsavegui
        dlg.Destroy()
 
#----------------------------------------------------------------------
    def startButton(self, event): 
    
        urls = csv.reader(open(csvopengui, "rU"))
        outurls = csv.writer(open(csvsavegui, "wb"))
        num_lines = len(open(csvopengui).read().splitlines())
        count = 1 
        start_time = time.time()
    
        
        execfile(vendoropengui) # exec(open("./filename").read()) [mod for python 3]
         
        self.SetStatusText("%f seconds" % (time.time() - start_time))  


#-----------------------------------------------------------------------

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("kanelong.png") #switch out your image here, if you don't like my son's artwork!
        dc.DrawBitmap(bmp, 0, 0)


#------------------------------------------------------------------------

# Run it!
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
