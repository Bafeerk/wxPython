import wx

BTN1 = 1
BTN2 = 2

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title= title, size=(600, 300))

        panel = wx.Panel(self)
        btn = wx.Button(panel, wx.ID_ANY, 'Кнопка')

        btn.Bind(wx.EVT_BUTTON, self.onButtonPress)
        panel.Bind(wx.EVT_BUTTON, self.onPanelPress)
        self.Bind(wx.EVT_BUTTON, self.onFramePress)

    def onButtonPress(self, event):
        print('Событие кнопки')
        #event.Skip()

    def onPanelPress(self, event):
        print('Событие панели')
        #event.Skip()

    def onFramePress(self, event):
        print('Событие окна')
app = wx.App()
frame = MyFrame(None, 'Event. Propagation')
frame.Show()
app.MainLoop()