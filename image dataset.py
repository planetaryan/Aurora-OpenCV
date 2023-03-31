import h5py
h5=h5py.File("gender_model_weights.h5",'r')
from imutils import paths
import cv2
from deepface import DeepFace
impaths=list(paths.list_images(r"C:\Users\plane\OneDrive\Desktop\malefemale"))

for i in impaths:
    image=cv2.imread(i)
    res=DeepFace.analyze(image,actions=['gender'])
    print(res['gender'])

