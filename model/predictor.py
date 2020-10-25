import tensorflow as tf
import cv2
import base64
import numpy as np
model = tf.keras.models.load_model('model/my_model.h5')
def predictor(data):
    global model
    im_bytes = base64.b64decode(data)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adddark = np.zeros(img.shape, np.uint8)
    alpha=0.3
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(img, alpha,adddark,beta, 0.0)
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
    dst = clahe.apply(dst)
    im=cv2.resize(dst,(128,128))




    batch = np.expand_dims(im,axis=0)
    batch = np.expand_dims(batch,axis=3)





    test=model.predict(batch)
    print(test)
    predicted_ids=np.argmax(test)
    print(predicted_ids)
    if predicted_ids==[0]:
      prediction='A'
    elif predicted_ids==[1]:
      prediction='B'
    elif predicted_ids==[2]:
      prediction='C'
    elif predicted_ids==[3]:
      prediction='D'
    elif predicted_ids==[4]:
      prediction='E'
    elif predicted_ids==[5]:
      prediction='F'
    elif predicted_ids==[6]:
      prediction='G'
    elif predicted_ids==[7]:
      prediction='H'
    elif predicted_ids==[8]:
      prediction='I'
    elif predicted_ids==[9]:
      prediction='J'
    elif predicted_ids==[10]:
      prediction='K'
    elif predicted_ids==[11]:
      prediction='L'
    elif predicted_ids==[12]:
      prediction='M'
    elif predicted_ids==[13]:
      prediction='N'
    elif predicted_ids==[14]:
      prediction='O'
    elif predicted_ids==[15]:
      prediction='P'
    elif predicted_ids==[16]:
      prediction='Q'
    elif predicted_ids==[17]:
      prediction='R'
    elif predicted_ids==[18]:
      prediction='S'
    elif predicted_ids==[19]:
      prediction='T'
    elif predicted_ids==[20]:
      prediction='U'
    elif predicted_ids==[21]:
      prediction='V'
    elif predicted_ids==[22]:
      prediction='W'
    elif predicted_ids==[23]:
      prediction='X'
    elif predicted_ids==[24]:
      prediction='Y'
    elif predicted_ids==[25]:
      prediction='Z'
    return prediction
