import wx
import wx.stc as stc
import keyword

class CodeEditorBase(stc.StyledTextCtrl):
    def __init__(self, parent):
        super().__init__(self,parent)
        font = wx.Font(10, wx.FONTFAMILY_MODERN ,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_NORMAL)
        self.face = font.GetFaceName()
        self.size = font.GetPointSize()
        self.SetupBaseStyles()

    def EnableLineNumber(self, enable = True):
        if enable :
            self.SetMarginType(1, stc.STC_MARGIN_NUMBER)
            self.SetMarginMask(1,0)
            self.SetMarginWidth(1,25)
        else:
            self.SetMarginWidth(1,0)

    def GetFaces(self):
        return dict(font=self.face, size = self.size)

    def SetupBaseStyle(self):
        faces = self.GetFaces()
        default = "face:%(font)s, size:%(size)d" % faces
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, default)
        line = "back:#C0C0C0 " + default
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, line)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(font)s" % face)


