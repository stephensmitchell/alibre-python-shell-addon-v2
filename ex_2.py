import sys
clr.AddReference('System.Runtime.InteropServices')
from System.Runtime.InteropServices import Marshal
alibre = Marshal.GetActiveObject("AlibreX.AutomationHook")
root = alibre.Root
session = root.TopmostSession
objADPartSession = session
b = objADPartSession.Bodies
verts = b.Item(0).Vertices
listA = []
def printpoint(x, y, z):
    print("{0} , {1} , {2}".format(x, y, z))
    listA.append("{0} , {1} , {2}".format(x, y, z))
for i in range(verts.Count):
    vert = verts.Item(i)
    point = vert.Point
    printpoint(point.X, point.Y, point.Z)
from System.Windows.Forms import MessageBox, MessageBoxButtons
list_str = ', '.join(map(str, listA))
MessageBox.Show(list_str, "AlibreX Python Script", MessageBoxButtons.OK)