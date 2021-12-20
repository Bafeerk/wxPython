import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        hbox = wx.BoxSizer()
        fb = wx.FlexGridSizer(4, 2, 10, 10)
        fb.AddMany([(wx.StaticText(panel, label='Ф.И.О.')),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label='email')),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label='Адрес')),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label='О себе')),
                    (wx.TextCtrl(panel, style=wx.NB_MULTILINE), wx.ID_ANY, wx.EXPAND)

        ])

        fb.AddGrowableCol(1, 1)
        fb.AddGrowableRow(3, 1)
        hbox.Add(fb, proportion=1, flag= wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(hbox)

app = wx.App()
frame = MyFrame(None, 'Flex Grid Sizer')
frame.Show()
app.MainLoop()