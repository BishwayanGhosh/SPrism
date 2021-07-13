from pydub import AudioSegment as AS
from glob import glob
import os
dir=input('Input directory address:')
dir_save=input('Input Save Address:')
audio_files=glob(dir+'/*.mp3')
print(f"{len(audio_files)} files found")
for i in range(0,len(audio_files)):
    # print(f"{audio_files[i]}:audio")
    audio=audio_files[i]
    src=os.path.basename(audio)
    src=src[0:src.index(".")]
    dst=dir_save+'\\'+src+'.wav'
    # print(f"{src}  {dst} filename")
    sound=AS.from_mp3(audio)
    sound.export(dst,format="wav")