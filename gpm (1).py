# This is Grid Portion Metrcis calculation of the generated map 

# importing libraries 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

truth = cv2.imread("ground_truth.pgm", cv2.IMREAD_GRAYSCALE)
adnn = cv2.imread("crsm_processed.pgm", cv2.IMREAD_GRAYSCALE)

true_positive = np.sum(truth == 0)
# white_pixel_count = np.sum(truth == 255)

# false_negative = 82
# false_positive = 107
# precision = true_positive/(true_positive + false_positive)
# sensitivity = true_positive/(true_positive + false_negative)


print("The number of black pixel: ", true_positive)
# print("The number of black pixel: ", white_pixel_count)
# print("The Precision: ", precision)
# print("The sensitivity: ", sensitivity)
cv2.imshow("image", truth)
cv2.imshow("img", adnn)
cv2.waitKey(0)