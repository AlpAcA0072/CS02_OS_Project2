import wx

f = open('output', encoding='utf-8')
fir_line = f.readline().strip().split(' ')
pid = fir_line[0]
file_name = fir_line[1]

app = wx.App()
window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(400, 300))
panel = wx.Panel(window)
window.Show(True)
app.MainLoop()
