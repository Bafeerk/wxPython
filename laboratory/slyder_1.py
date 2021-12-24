import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))


app = wx.App()
frame = MyFrame(None, 'Color slider')
frame.Show()

app.MainLoop()
