
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow


boxes = np.array([(45, 33, 58, 79),
 (91, 32, 121, 80),
 (156, 32, 182, 81),
 (211, 33, 245, 80),
 (275, 32, 303, 80),
 (333, 31, 366, 81),
 (396, 32, 425, 80),
 (455, 32, 486, 81),
 (514, 32, 546, 81),
 (43, 116, 73, 164),
 (102, 117, 136, 164),
 (168, 116, 194, 165),
 (224, 115, 257, 165),
 (287, 117, 300, 163),
 (334, 116, 365, 165),
 (395, 116, 423, 164),
 (454, 116, 486, 165),
 (513, 116, 549, 165)])

def bounding_box_sorting(boxes):
    '''
    sorting boxes from right to left from && top to down
    '''
    num_boxes = boxes.shape[0]
    # sort from top to bottom and left to right
    sorted_boxes = sorted(boxes, key=lambda x: (x[1], x[0]))
    _boxes = list(sorted_boxes)
    # check if the next neighgour box x coordinates is greater then the current box x coordinates if not swap them.
    # repeat the swaping process to a threshold iteration and also select the threshold 
    threshold_value_y = 10
    for i in range(int(num_boxes/2)):
      for i in range(num_boxes - 1):
          if abs(_boxes[i + 1][1] - _boxes[i][1]) < threshold_value_y and (_boxes[i + 1][0] > _boxes[i][0]):
              tmp = _boxes[i]
              _boxes[i] = _boxes[i + 1]
              _boxes[i + 1] = tmp
    return _boxes

# create black image
w = max([max(x[0], x[2]) for x in boxes])
h = max([max([x[1],x[3]]) for x in boxes])
img = np.zeros((h+500,w+500))
print(img.shape)

# sorting boxes
print(boxes)
boxes = bounding_box_sorting(boxes)
print(boxes)

# For debugging purposes.
for i in range(len(boxes)):
    # print(boxes[i][:2])
    start_point = tuple(boxes[i][:2])
  
    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = tuple(boxes[i][-2:])

    # Draw a rectangle with blue line borders of thickness of 2 px
    img = cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)
    img = cv2.putText(img, str(i), start_point, cv2.FONT_HERSHEY_COMPLEX, 1, [125])

# show image
# cv2_imshow(img)
cv2.imshow(img)
