from elma import Level

# Load the existing level
input_filename = R"C:\Programs\EOL\lev\unstable.lev"
output_filename = R"C:\Programs\EOL\lev\test.lev"
# 100000000376832 is a floating point number (so recs don't crash). You can add a small offset to centralize the rec position
offset=100000000376832-27.3

level = Level.load(input_filename)

for polygon in level.polygons:
    for point in polygon.points:
        point.x += offset
        #point.y += offset

for object in level.objects:
    object.point.x += offset
    #object.point.y += offset

for picture in level.pictures:
    picture.point.x += offset
    #picture.point.y += offset

level.save(output_filename, True)