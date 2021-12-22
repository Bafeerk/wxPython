import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        self.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

    def onLeftDown(self, event):
        print('Нажатие на левую кнопку мыши')

app = wx.App()
frame = MyFrame(None, 'Event. Bind and Unbind')
frame.Show()
app.MainLoop()