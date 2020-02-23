from BoundBox_class import BoundBox

box_2 = BoundBox.box_from_array([[107, 95], [352, 117], [420, 615], [80, 590]])
box_3 = BoundBox.box_from_array([[4, 2], [2, 4], [8, 6], [6, 9]])


k = [box_2, box_3]

p = BoundBox.merge_box(k)