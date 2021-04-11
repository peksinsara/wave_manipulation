#import required modules
import matplotlib.pyplot as plt
import numpy as np
from math import pi

def WaveformToBinary():
    #define number of samples that will be used
    symbolLenght=64
    numOfSignals=32  

    randomNum= np.random.rand(numOfSignals)

    randomNum[np.where(randomNum>=0.5)]=1
    randomNum[np.where(randomNum<0.5)]=0

    #generate random lines 
    plt.subplot(3,1,1, facecolor=(.18, .31, .31))
    plt.stem(randomNum)
    #plt.show()

    #generate signal
    #total number of signals
    signal=np.zeros(symbolLenght*numOfSignals)

    #creating a loop for checking where id of random generated number is 1
    idNumber=np.where(randomNum==1)

    for i in idNumber[0]:
        store=i*symbolLenght
        signal[store:store+symbolLenght]=1
        

    plt.subplot(3,1,3, facecolor=(.18, .31, .31))

    plt.plot(signal)
    plt.title('Randomly generated sequence to binary', color='white')
    plt.xlabel('Sample', color='c');
    plt.ylabel('Amplitude', color='c')
    plt.grid()
    plt.show()

WaveformToBinary()

#Frequency Modulation
def FrequencyModulation():
    Fs=2000 #sampling frequency
    t=np.arange(0,0.2,1/Fs) #time
    
    c=100 #carrierer wave
    Fm=20 #signal frequency
    
    b=3 #modulation index
    
    Frm=np.cos(2*pi*c*t + b*np.sin(2*pi*Fm*t))
    m=np.cos(2*pi*Fm*t) #message signal
    
    plt.subplot(facecolor=(.18, .31, .31))
    plt.plot(t,Frm)
    plt.title('Frequency Modulation', color='white')
    plt.plot(t,m)
    plt.xlabel('Time (t)', color='c')
    plt.ylabel('Amplitude', color='c')
    plt.legend(['Frequency Modulation Signal', 'Message Signal'])
    plt.grid()
    plt.show()
    
    
FrequencyModulation()

#Amplitude Modulation
def AmplitudeModulation():
    #time axis
    Fs=2000 #sampling frequency
    t=np.arange(0,2,1/Fs) #time
    
    #carrier wave
    Fc=50 #carrier frequency
    Ac=1 #carrier amplitude
    c=Ac*np.cos(2*pi*Fc*t) #carrier wave
    
    #generate message signal
    Fm=2 #message frequency
    Am=0.5  #Always less than frequency of the carrier wave
    m=Am*np.sin(2*pi*Fm*t) #message signal
    
    #Amplitude modulated signal
    s=c*(1 + m/Ac) 
    

    plt.subplot(3,1,1, facecolor=(.18, .31, .31))
    plt.plot(t,s)
    plt.title('Unmodulated signal')
    plt.xlabel('Time (t)', color='c')
    plt.ylabel('Amplitude', color='c')
    plt.grid()
    
    #Full modulation
    Am=1
    m = Am*np.sin(2*pi*Fm*t)
    s = c * (1 + m/Ac) 
    

    plt.subplot(3,1,3, facecolor=(.18, .31, .31))
    plt.plot(t,s)
    plt.title('Full modulated signal')
    plt.xlabel('Time (t)', color='c')
    plt.ylabel('Amplitude', color='c')
    plt.grid()
    plt.show()
    
    
AmplitudeModulation()

    

    

    
    

    



