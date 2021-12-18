import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        vBox = wx.BoxSizer()
        #img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap('images/js.png'))
        #img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap('images/python.png'))

        #img1.SetPosition((10, 10))
        #img2.SetPosition((300, 40))

        #vBox.Add(img1, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        #vBox.Add(img2, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        mp = wx.Panel(panel)
        mp.SetBackgroundColour('#88cc88')
        vBox.Add(mp, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vBox)


app = wx.App()
frame = MyFrame(None, 'Box Sizer')
frame.Show()
app.MainLoop()