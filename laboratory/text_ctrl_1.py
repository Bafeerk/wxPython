import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        box = wx.BoxSizer()
        tc1 = wx.TextCtrl(panel, style=wx.TE_CENTER)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL | wx.TE_PROCESS_ENTER)
        #tc2.SetBackgroundColour('#ffee55')
        tc2.Bind(wx.EVT_TEXT_ENTER, self.onText)
        box.Add(tc1)
        box.Add(tc2)
        panel.SetSizer(box)
    def onText(self, e):
        print(e.GetEventObject().GetValue())


app = wx.App()
frame = MyFrame(None, 'Styles of TextCtrl')
frame.Show()
app.MainLoop()