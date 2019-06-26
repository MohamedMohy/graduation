import skimage.io
print(type(skimage.io.imread('Mask_RCNN/images/12283150_12d37e6389_z.jpg')))
from runner import run
image = skimage.io.imread('Mask_RCNN/images/12283150_12d37e6389_z.jpg')
run(image,"mohy.png")