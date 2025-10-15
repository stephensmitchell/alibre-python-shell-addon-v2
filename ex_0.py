import sys
import clr

sys.path.append("C:\Program Files\Alibre Design 27.0.1.27039\Program")
sys.path.append("C:\Program Files\Alibre Design 27.0.1.27039\Program\Addons\AlibreScript")
clr.AddReference("AlibreX")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

# init sys.path
import AlibreX

# sys.path.append(Rhino.ApplicationSettings.FileSettings.InstallFolder.FullName + "Plug-ins\\IronPython\\Lib\\")
# sys.path.append(Rhino.ApplicationSettings.FileSettings.GetDataFolder(True) +
#                 "Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib\\")
sys.path.append("C:\\PROGRAM FILES\\Alibre Design 27.0.1.27039\\PROGRAM\\ADDONS\\ALIBRESCRIPT\\PythonLib")
sys.path.append("C:\\PROGRAM FILES\\Alibre Design 27.0.1.27039\\PROGRAM\\ADDONS\\ALIBRESCRIPT")
sys.path.append("C:\\PROGRAM FILES\\Alibre Design 27.0.1.27039\\PROGRAM\\ADDONS\\ALIBRESCRIPT\\PythonLib\\site-packages")

import AlibreScript

clr.AddReference('System.Runtime.InteropServices')

from System.Runtime.InteropServices import Marshal

alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root
session = root.Sessions.Item(0)
objADPartSession = session

print(session.FilePath)
print(objADPartSession.Bodies.Count)

b = objADPartSession.Bodies
verts = b.Item(0).Vertices

print(verts.Count)

def printpoint(x, y, z):
    print("{0} , {1} , {2}".format(x, y, z))
    
for i in range(verts.Count):
    vert = verts.Item(i)
    point = vert.Point
    printpoint(point.X, point.Y, point.Z)  # Calls the printpoint function defined later

def printpoint(x, y, z):
    print("{0} , {1} , {2}".format(x, y, z)) 