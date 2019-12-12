import matplotlib.pyplot as plt
import math
import random
import numpy.fft

lenght = 2048
signal = [0.] * lenght;

F1=5;
P1=0.1; #синусоида немного сдвинута по фазе
P2=0.3
F2=10;
k=0;

coeff = 2 * math.pi / lenght #для ускорения вычислений заранее подсчитаем множитель

coeff1 = 2 * math.pi * F1 / lenght
coeff2 = 2 * math.pi *F2 / lenght
coeff3 = 2 * math.pi * 7 / lenght

#генерируем сигнал, состоящий из синусоид и шума
while (k < lenght):
    signal[k] = math.sin(coeff3*k) + math.cos((coeff1*k)+P1) + math.cos(coeff2*k+P2) + 1*(random.random() - 0.5)
    #signal[k] = math.cos(2*math.pi*F1*(k/lenght)+P1) + math.cos(2*math.pi*F2*(k/lenght)) + 1*(random.random() - 0.5)
    k=k+1
    
#рисуем его на картинке
plt.plot(signal)
plt.show()


#теперь ищем какую-либо частоту в данном сигнале
REL_FREQ=1; #вот эту частоту
k=0;
s_re=0;
s_im=0;

while (REL_FREQ<15):
    REL_FREQ=REL_FREQ+1
    s_re=0;
    s_im=0;
    k=0;

    while (k<lenght):
        s_re = s_re+math.cos(REL_FREQ*k*coeff)*signal[k]
        s_im = s_im+math.sin(REL_FREQ*k*coeff)*signal[k]
    #s_re = s_re+math.cos(2*math.pi*REL_FREQ*(k/lenght))*signal[k]
    #s_im = s_im+math.sin(2*math.pi*REL_FREQ*(k/lenght))*signal[k]
        k=k+1
        
        
    print ('frequency:',REL_FREQ,', amplitude:', int(math.sqrt(s_re*s_re+s_im*s_im)))
    


print(s_re,";",s_im,";",math.sqrt(s_re*s_re+s_im*s_im))
    
    

#print (numpy.fft.fft(signal, n=40))
