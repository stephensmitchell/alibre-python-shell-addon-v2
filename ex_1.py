import sys
import clr
clr.AddReference("alibre-api")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference('System.Runtime.InteropServices')
from System.Runtime.InteropServices import Marshal
from com.alibre.automation import *
from AlibreScript.API import *
# HERE IS ONE METHOD TO GET THE SESSION
alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root
myPart = Part(root.TopmostSession)

# ALIBRE SCRIPT CODE
Win = Windows()
Win.InfoDialog('This code is from Alibre Script.', myPart.FileName)
Win.ErrorDialog('This code is from Alibre Script!', myPart.LastAuthor)
print(Win.QuestionDialog('This code is from Alibre Script?', myPart.CreatedBy))