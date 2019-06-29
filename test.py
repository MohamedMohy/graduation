import skimage.io
x= skimage.io.imread('Mask_RCNN/Screenshot from 2019-06-28 15-28-48.png')
print(x.shape)
from runner import run
image = skimage.io.imread('Mask_RCNN/images/12283150_12d37e6389_z.jpg')
run(image,"mohy.png")