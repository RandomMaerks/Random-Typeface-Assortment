import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Bolt Sans"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 90
a1.minimum = 16
a1.default = 90
a1.name = "opticalsize"
a1.tag = "opsz"
doc.addAxis(a1)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "BoltSans-Med.ufo"
s0.familyName = familyName
s0.styleName = "Macro"
s0.location = dict(opticalsize=90)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "BoltSansText-Med.ufo"
s1.familyName = familyName
s1.styleName = "Micro"
s1.location = dict(opticalsize=16)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'BoltSans-Med'
i0.familyName = familyName
i0.styleName = "Macro"
i0.path = os.path.join(root, "instances", "BoltSans-Med.ufo")
i0.location = dict(opticalsize=90)
i0.kerning = True
i0.info = True
i0.styleMapFamilyName = "Bolt Sans Macro"
i0.styleMapStyleName = "regular"
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'BoltSansText-Med'
i1.familyName = familyName
i1.styleName = "Micro"
i1.path = os.path.join(root, "instances", "BoltSansText-Med.ufo")
i1.location = dict(opticalsize=16)
i1.kerning = True
i1.info = True
i1.styleMapFamilyName = "Bolt Sans Micro"
i1.styleMapStyleName = "regular"
doc.addInstance(i1)


#--------
# saving
#--------

path = "BoltSans.designspace"
doc.write(path)