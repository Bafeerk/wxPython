import wx

ID_RED = 1
ID_GREEN = 2
ID_BLUE = 3
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        sl_red = wx.Slider(panel, value=0, minValue=0, maxValue=255, id=ID_RED)
        sl_green = wx.Slider(panel, value=0, minValue=0, maxValue=255, id=ID_GREEN)
        sl_blue = wx.Slider(panel, value=0, minValue=0, maxValue=255, id=ID_BLUE)
        self.tc = wx.TextCtrl(panel, value='0 0 0')
        vbox.Add(sl_red, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(sl_green, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(sl_blue, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(self.tc, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        sl_red.Bind(wx.EVT_SLIDER, self.onColor)
        sl_green.Bind(wx.EVT_SLIDER, self.onColor)
        sl_blue.Bind(wx.EVT_SLIDER, self.onColor)
        panel.SetSizer(vbox)

        self.color = wx.Colour(sl_red.GetValue(), sl_green.GetValue(), sl_blue.GetValue())
        self.font_color = wx.Colour(255, 255, 255)
        self.tc.SetBackgroundColour(self.color.GetAsString())
        self.tc.SetForegroundColour(self.font_color)

    def onColor(self, e):
        r = self.color.Red()
        g = self.color.Green()
        b = self.color.Blue()
        font = 0
        val = e.GetEventObject().GetValue()
        id = e.GetEventObject().GetId()
        if id == ID_RED:
            self.color.Set(val, g, b)
            font = r + g + val
        elif id == ID_GREEN:
            self.color.Set(r, val, b)
            font = r + val + b
        elif id == ID_BLUE:
            self.color.Set(r, g, val)
            font = r + g + val

        self.tc.SetBackgroundColour(self.color.GetAsString())
        self.tc.Refresh()
        if font > 450:
            self.font_color = wx.Colour(0, 0, 0)
            self.tc.SetForegroundColour(self.font_color)
        else:
            self.font_color = wx.Colour(255, 255, 255)
            self.tc.SetForegroundColour(self.font_color)
        self.tc.SetValue(f"{r} {g} {b}")

app = wx.App()
frame = MyFrame(None, 'Color slider')
frame.Show()

app.MainLoop()
