import clr
import sys

# Add the paths to the Alibre Design assemblies and Python libraries
sys.path.append(r"C:\Program Files\Alibre Design 27.0.1.27039\Program")
sys.path.append(r"C:\Program Files\Alibre Design 27.0.1.27039\Program\Addons\AlibreScript")
clr.AddReference("AlibreX")
clr.AddReference("AlibreScriptAddOn")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

sys.path.append(r"C:\PROGRAM FILES\Alibre Design 27.0.1.27039\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 27.0.1.27039\PROGRAM\ADDONS\ALIBRESCRIPT")
sys.path.append(r"C:\PROGRAM FILES\Alibre Design 27.0.1.27039\PROGRAM\ADDONS\ALIBRESCRIPT\PythonLib\site-packages")

import AlibreX
import AlibreScript
from System.Runtime.InteropServices import Marshal

# Get the active Alibre Design application object
alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root
session = root.Sessions.Item(0)
objADPartSession = session

# Print the session file path and body count
#print(session.FilePath)
print(objADPartSession.Bodies.Count)

# Get the bodies and vertices
b = objADPartSession.Bodies
verts = b.Item(0).Vertices
print(verts.Count)

# Function to print a point's coordinates
def printpoint(x, y, z):
    print("{0} , {1} , {2}".format(x, y, z))

# This empty line signals the end of the function definition in an interactive shell

# Iterate through vertices and print their coordinates
for i in range(verts.Count):
    vert = verts.Item(i)
    point = vert.Point
    printpoint(point.X, point.Y, point.Z)

