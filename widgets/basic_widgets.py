import wx

BTN_RED = 1
BTN_GREEN = 2
BTN_BLUE = 3


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 500))

        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText('Текст в статусной строке')

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        st = wx.StaticText(panel, label='Адрес: ')
        vbox.Add(st, flag=wx.ALL, border=10)
        inp = wx.TextCtrl(panel, value='г. Москва')
        vbox.Add(inp, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        rtb = wx.ToggleButton(panel, id=BTN_RED, label='Red')
        gtb = wx.ToggleButton(panel, id=BTN_GREEN, label='Green')
        btb = wx.ToggleButton(panel, id=BTN_BLUE, label='Blue')

        self.col = wx.Colour(0, 0, 0)
        self.pn = wx.Panel(panel)
        self.pn.SetBackgroundColour(self.col.GetAsString())

        vb1 = wx.GridBagSizer(10, 10)
        vb1.Add(rtb, (0, 0))
        vb1.Add(gtb, (1, 0))
        vb1.Add(btb, (2, 0))
        vb1.Add(self.pn, (0, 1), (3, 1), flag=wx.EXPAND)
        vb1.AddGrowableCol(1)

        vbox.Add(vb1, flag=wx.EXPAND | wx.ALL, border=10)

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)

        vbox.Add(wx.StaticLine(panel), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        pn2 = wx.Panel(panel)
        wx.StaticBox(pn2, label='Ваш пол:', size=(150, 50))
        rbn_1 = wx.RadioButton(pn2, label='Муж', pos=(10, 20), style=wx.RB_GROUP)
        rbn_2 = wx.RadioButton(pn2, label='Жен', pos=(100, 20))

        vb2 = wx.BoxSizer(wx.HORIZONTAL)
        vb2.Add(pn2)

        agree = wx.CheckBox(panel, label='Согласен на обработку')
        agree.SetValue(True)
        vb2.Add(agree, flag=wx.EXPAND | wx.ALL, border=20)

        links = ["Телефон", "email", "Skype"]
        cb = wx.ComboBox(panel, choices=links, style=wx.CB_READONLY)
        cb.SetSelection(0)
        sc = wx.SpinCtrl(panel, size=(110, 20), value='0', min=-100, max=100)
        vb2.Add(cb, flag=wx.LEFT | wx.TOP, border=15)
        vb2.Add(sc, flag=wx.LEFT | wx.TOP, border=15)
        vbox.Add(vb2, flag=wx.EXPAND | wx.ALL, border=10)

        self.gauge = wx.Gauge(panel, range=100)
        vbox.Add(self.gauge, flag=wx.EXPAND | wx.ALL, border=10)

        b_start = wx.Button(panel, label='Старт')
        b_stop = wx.Button(panel, label='Стоп')
        hb3 = wx.BoxSizer(wx.HORIZONTAL)
        hb3.AddMany([(b_start, 0, wx.LEFT | wx.RIGHT, 10), (b_stop, 0, wx.RIGHT, wx.BOTTOM, 10)])
        vbox.Add(hb3, flag=wx.ALIGN_CENTER)
        b_start.Bind(wx.EVT_BUTTON, self.onStart)
        b_stop.Bind(wx.EVT_BUTTON, self.onStop)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)
        self.count = 0
        self.gauge.SetValue(self.count)

        sld = wx.Slider(panel, value=200, minValue=150, maxValue=500, style=wx.SL_HORIZONTAL)
        vbox.Add(sld, flag=wx.EXPAND | wx.ALL, border=10)

        sld.Bind(wx.EVT_SCROLL, self.onSliderScroll)
        panel.SetSizer(vbox)

    def onSliderScroll(self, event):
        val = event.GetEventObject().GetValue()
        self.sb.SetStatusText(f"\tSlider {str(val)}")

    def onStop(self, event):
        self.timer.Stop()
        self.count = 0

    def onStart(self, event):
        if self.count > 100:
            return
        else:
            self.timer.Start(100)

    def onTimer(self, event):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
        if self.count >= 100:
            self.timer.Stop()

    def onToggle(self, event):
        btn = event.GetEventObject()
        val = 255 if btn.GetValue() else 0
        id = btn.GetId()

        r = self.col.Red()
        g = self.col.Green()
        b = self.col.Blue()

        if id == BTN_RED:
            self.col.Set(val, g, b)
        elif id == BTN_GREEN:
            self.col.Set(r, val, b)
        elif id == BTN_BLUE:
            self.col.Set(r, g, val)

        self.pn.SetBackgroundColour(self.col)
        self.pn.Refresh()


app = wx.App()
frame = MyFrame(None, 'Basic Widgets')
frame.Show()
app.MainLoop()
