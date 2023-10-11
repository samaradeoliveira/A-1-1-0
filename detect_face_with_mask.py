import cv2
import numpy as np

#importar tensorflow

#criar variável model para receber o modelo treinado. 


video = cv2.VideoCapture(0)

while True:

    check,frame = video.read()

    # Altere o dado de entrada:
    # 1. Redimensione a imagem
   

    

    # 2. Converta a imagem em um array Numpy e aumente a dimensão para o funcionamento correto das imagens treinadas
   
    
    # 3. Normalize a imagem (ajuda no treinamento eficaz da máquina, especialmente em redes neurais) (rapidez no processamento de imagens)
   

    # Preveja o resultado
    

   

    print("Previsão: ", prediction)
        
    cv2.imshow("Resultado",frame)
            
    key = cv2.waitKey(1)

    if key == 32:
        print("Fechando")
        break

video.release()
