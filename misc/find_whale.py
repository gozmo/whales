from sklearn.cluster import KMeans
from PIL import Image

im = Image.open("w_7489.jpg")

pixels = []
coordinates = []

width, height = im.size
for w in xrange(width):
    for h in xrange(height):
        pixels.append(im.getpixel((w,h)))
        coordinates.append((w,h))

kmeans = KMeans(init='random',
                n_clusters=3,
                n_init=10)
print "clustering"
a = kmeans.fit(pixels)
print kmeans.cluster_centers_
