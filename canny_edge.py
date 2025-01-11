import cv2

img = cv2.imread('/Users/miriamlopez/ThesisProject/sample_image_edge_533581 .png') # Read image

# Setting parameter values
t_lower = 102 # Lower Threshold
t_upper = 255 # Upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img, t_lower, t_upper)

cv2.imshow('original', img)
new_file = cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

