import cv2
import numpy as np

#import tensorflow as tf

#model = tf.keras.models.load_model('keras_model.h5')

video = cv2.VideoCapture(0)

while True:

    check,frame = video.read()

    # Altere o dado de entrada:
    # 1. Redimensione a imagem
    

    

    # 2. Converta a imagem em um array Numpy e aumente a dimensão

    
    # 3. Normalize a imagem
   

    # Preveja o resultado
   

   

    print("Previsão: ", prediction)
        
    cv2.imshow("Resultado",frame)
            
    key = cv2.waitKey(1)

    if key == 32:
        print("Fechando")
        break

video.release()