# import winsound
# winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

# import os
# os.system("start C:/thepathyouwant/file")

# import os
# os.system("start E:\Turn.mp3")
## os.system("start E:\Imagens\chapolin.jpg")


from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')


# import pygame 							# Metodo aula que não funciona

# pygame.init()
# pygame.mixer.music.load('ex021.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()
