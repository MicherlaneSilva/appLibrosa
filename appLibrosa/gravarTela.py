import cv2

def gravar(tempo):
    cap = cv2.VideoCapture(0)
    contador = 0
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('meuRosto.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)

            #cv2.imshow('frame',frame)
            contador += 1
            if contador == 20 * tempo:
                break
        else:
            break

    

    cap.release()
    out.release()
    cv2.destroyAllWindows()