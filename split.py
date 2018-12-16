
import numpy as np
import csv
from glob import glob
import matplotlib.pyplot as plt
from PIL import Image



labels_path = 'labels.csv'
with open(labels_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)
    labels_list = np.array(data).astype(str)
pre_path = 'deploy/trainval/'
input_max = int(labels_list.shape[0])
print("max labeled = ", input_max)

missing = 0
labeled = 0
num_x = 0
num_y = 0
num_z = 0

for i in range(1, input_max):
    id_path = labels_list[i][0]
    classification = int(float(labels_list[i][1]))
    img_identifier = id_path + '_image.jpg'
    img_identifier = pre_path + img_identifier
    print(img_identifier, classification)

    file = glob(img_identifier)
    if not file:
        missing += 1
        print("Error: could not find:" + file)
        #skip!
    else:
        num_img = plt.imread(file[0], format='jpeg')
        
        myimg = Image.fromarray(num_img)
        if classification == 0:
            myimg.save('x/' + id_path.split('/')[0] + '_'+ id_path.split('/')[1] + ".jpeg")
            num_x += 1
        if classification == 1:
            myimg.save('y/' + id_path.split('/')[0] + '_'+ id_path.split('/')[1] + ".jpeg")
            num_y += 1
        if classification == 2:
            myimg.save('z/' + id_path.split('/')[0] + '_'+ id_path.split('/')[1] + ".jpeg")
            num_z += 1
        labeled += 1
    