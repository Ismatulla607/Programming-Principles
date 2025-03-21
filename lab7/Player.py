import pygame
import os

pygame.init()

playlist = []
music_folder = r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

if not playlist:
    print("No music files found in the folder.")
    exit()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Darkhan-Juzz")
clock = pygame.time.Clock()

bg_path = r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\msc\background.png"
if not os.path.exists(bg_path):
    print("Background image not found!")
    exit()
background = pygame.image.load(bg_path)

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

playb = pygame.image.load(r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\msc\play.png")
pausb = pygame.image.load(r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\msc\pause.png")
nextb = pygame.image.load(r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\msc\next.png")
prevb = pygame.image.load(r"C:\Users\isma\OneDrive\Desktop\Git hub\Programming-Principles\lab7\msc\back.png")

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(-1)  
aplay = True

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))

    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))

    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))
    
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
