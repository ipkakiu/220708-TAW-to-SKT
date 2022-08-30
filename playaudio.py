import simpleaudio as sa

FileName = 'CKT to STW'
FileFormat = '.wav'
#FileFormat2 = '.mp4 '

wav_obj = sa.WaveObject.from_wave_file(FileName + FileFormat)
play_obj = wav_obj.play()
print("Music is playing...")
play_obj.wait_done()