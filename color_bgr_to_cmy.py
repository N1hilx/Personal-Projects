import numpy as np


def bgr_to_cmy(bgr_image):
    # Value conversion
    cmy_image = np.zeros_like(bgr_image)
    cmy_image[:,:,0] = 255 - bgr_image[:,:,2]  # C = 255 - R
    cmy_image[:,:,1] = 255 - bgr_image[:,:,1]  # M = 255 - G
    cmy_image[:,:,2] = 255 - bgr_image[:,:,0]  # Y = 255 - B
    return cmy_image


# test
bgr_img = np.array([[[255,255,0],[150,50,0],[96,69,180]]])
print(bgr_to_cmy(bgr_img))
# [[[255   0   0]
#   [255 205 105]
#   [ 75 186 159]]]
