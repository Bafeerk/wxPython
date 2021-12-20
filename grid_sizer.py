import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND | wx.LEFT |wx.RIGHT | wx.TOP, border=10)

        gbox = wx.GridSizer(5, 4, 5, 5)
        gbox.AddMany([(wx.Button(panel, label='Cls'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='Bck'), wx.ID_ANY, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='Close'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='7'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='8'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='9'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='/'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='4'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='5'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='6'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='*'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='1'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='2'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='3'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='-'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='0'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='.'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='='), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='+'), wx.ID_ANY, wx.EXPAND),
                      ])

        vbox.Add(gbox, proportion=1, flag= wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

app = wx.App()
frame = MyFrame(None, 'Grid Sizer')
frame.Show()
app.MainLoop()