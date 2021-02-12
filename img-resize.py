import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle

out_dir = './png-etl1'
im_size = 25
save_file = out_dir + '/katakana.pickle'
plt.figure(figsize=(9, 17))

kanadir = list(range(177, 220 + 1))
kanadir.append(166)
kanadir.append(221)
result = []
for i,code in enumerate(kanadir):
  img_dir = out_dir + '/' + str(code)
  fs = glob.glob(img_dir + '/*')
  print('dir=', img_dir)
  for j, f in enumerate(fs):
    img = cv2.imread(f)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img_gray, (im_size, im_size))
    result.append([i, img])
    if j== 3:
      plt.subplot(11, 5, i + 1)
      plt.axis('off')
      plt.title(str(i))
      plt.imshow(img, cmap='gray')

pickle.dump(result, open(save_file, 'wb'))
plt.show()
print('OK')