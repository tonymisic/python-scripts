import wx
import pygame
import sys


class Window(wx.Frame):
    def create_window(tmp):
        app = wx.App()
        frame = wx.Frame(None, title=tmp)
        frame.Show()
        app.MainLoop()
