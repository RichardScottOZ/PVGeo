"""
Read GSLib Point Set
~~~~~~~~~~~~~~~~~~~~

Read GSLib point set file
"""
# sphinx_gallery_thumbnail_number = 1
import vtki
from vtki import examples
from PVGeo.gslib import GSLibPointSetReader

################################################################################
points_url = 'http://www.trainingimages.org/uploads/3/4/7/0/34703305/b_100sampledatawl.sgems'
filename, _ = examples.downloads._retrieve_file(points_url, 'b_100sampledatawl.sgems')

point_set = GSLibPointSetReader().apply(filename)
print(point_set)

################################################################################
point_set.plot()
