from sklearn.cluster import KMeans
from PIL import Image

class SegmentColours:
    def __init__(self, image_file_name):
        self._image = Image.open(image_file_name)
        self._iterations = 10
        self._clusters = 8

    def segment(self):
        for x in xrange(self._iterations):
            print "Iteration: %s, clustering" % x
            self._cluster_pixels()
            print "Updating pixels"
            self._update_pixels()
        return self._image


    def _cluster_pixels(self):
        pixels = list(self._image.getdata())

        self._kmeans = KMeans(init='random',
                        n_clusters=self._clusters,
                        n_init=10)
        self._kmeans.fit(pixels)

    def _classify_pixel(self, pixel):
        return self._kmeans.fit(pixel)

    def _update_pixels(self):
        width, height = self._image.size
        for w in xrange(width):
            for h in xrange(height):
                coordinate = (w,h)
                pixel = self._image.getpixel(coordinate)
                updated_pixel = self._classify_pixel(pixel)
                self._image.putpixel(coordinate, updated_pixel)

segment_colours = SegmentColours("w_7489.jpg")
segment_colours.segment()
