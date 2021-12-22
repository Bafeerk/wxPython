import wx

BTN1 = 1
BTN2 = 2

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title= title, size=(600, 300))

        btn1 = wx.Button(self, BTN1, label='Button 1')
        btn2 = wx.Button(self, BTN2, label='Button 2')
        btn1.SetPosition(wx.Point(10, 10))
        btn2.SetPosition(wx.Point(200, 10))

        self.Bind(wx.EVT_BUTTON, self.onButton_1, id=BTN1)
        self.Bind(wx.EVT_BUTTON, self.onButton_2, id=BTN2)

    def onButton_1(self, event):
        print('Нажата первая кнопка')

    def onButton_2(self, event):
        print('Нажата вторая кнопка')
app = wx.App()
frame = MyFrame(None, 'Event. Different types of id')
frame.Show()
app.MainLoop()