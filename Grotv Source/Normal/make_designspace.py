import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Grotv Norm"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 900
a1.minimum = 200
a1.default = 200
a1.name = "weight"
a1.tag = "wght"
doc.addAxis(a1)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "GrotvNorm-ExtraLight.ufo"
s0.familyName = familyName
s0.styleName = "ExtraLight"
s0.location = dict(weight=200)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "GrotvNorm-Black.ufo"
s1.familyName = familyName
s1.styleName = "Black"
s1.location = dict(weight=900)
doc.addSource(s1)

#--------
# saving
#--------

path = "GrotvNorm.designspace"
doc.write(path)