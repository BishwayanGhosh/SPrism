import pandas as pd
from glob import glob
import librosa as lr
from pydub import AudioSegment as AS
import os
import math
dir=input('Input directory to read from:')
s=input('Enter number of samples:')
audio_files=glob(dir + '/*.wav')
print(f"{len(audio_files)} files available")
columns=['Label']
for i in range(0,int(s)):
    val=f"T{i}"
    columns=columns+[val]
#print(f"{len(columns)}")
label=input("Enter Label no.:");
df=pd.DataFrame(columns=columns)
for aud in audio_files:
    audioName=str(os.path.basename(aud))
    audio,freq=lr.load(aud)
    aud=[label]
    #print(f"{len(audio)}")
    #print(f"{int(math.floor(len(audio))/int(s))}")
    i=0
    for j in range(0,int(s)):
        aud=aud+[str(audio[i])]
        i=i+int(math.floor(len(audio))/int(s))
    print(f"{len(aud)}")
    df.loc[len(df.index)]=aud
filename=input('Enter Filename to store to:')
#print(f"{df}")
df.to_csv(filename)