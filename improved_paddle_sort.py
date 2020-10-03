
def bounding_box_sorting(boxes):
    num_boxes = boxes.shape[0]
    # sort from top to bottom and left to right
    sorted_boxes = sorted(dt_boxes, key=lambda x: (x[0][1], x[0][0]))
    _boxes = list(sorted_boxes)
    # print('::::::::::::::::::::::::::testing')
    for j in range
    # check if the next neighgour box x coordinates is greater then the current box x coordinates if not swap them.
    # repeat the swaping process to a threshold iteration and also select the threshold 
    threshold_value_y = 10
    for i in range(5):
      for i in range(num_boxes - 1):
          if abs(_boxes[i + 1][0][1] - _boxes[i][0][1]) < threshold_value_y and (_boxes[i + 1][0][0] < _boxes[i][0][0]):
              tmp = _boxes[i]
              _boxes[i] = _boxes[i + 1]
              _boxes[i + 1] = tmp
    return _boxes
    
 #full Credit goes to the paddleocr . I taken the code from there and just added the number iteration to sort the mismatched box.
