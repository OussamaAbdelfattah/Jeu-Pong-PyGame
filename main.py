import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Définition de la fenêtre de jeu
largeur_ecran = 640
hauteur_ecran = 480
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption('Pong')

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Paramètres du jeu
largeur_raquette = 15
hauteur_raquette = 60
vitesse_raquette = 5
largeur_balle = 15
hauteur_balle = 15
vitesse_balle_x = 3
vitesse_balle_y = 3

# Création des raquettes
raquette_joueur1 = pygame.Rect(0, hauteur_ecran // 2 - hauteur_raquette // 2, largeur_raquette, hauteur_raquette)
raquette_joueur2 = pygame.Rect(largeur_ecran - largeur_raquette, hauteur_ecran // 2 - hauteur_raquette // 2, largeur_raquette, hauteur_raquette)

# Création de la balle
balle = pygame.Rect(largeur_ecran // 2 - largeur_balle // 2, hauteur_ecran // 2 - hauteur_balle // 2, largeur_balle, hauteur_balle)

# Variables pour le mouvement des raquettes
raquette_joueur1_bouge_haut = False
raquette_joueur1_bouge_bas = False
raquette_joueur2_bouge_haut = False
raquette_joueur2_bouge_bas = False

# Police pour le texte
font = pygame.font.Font(None, 36)

# Boucle de jeu
jeu_en_cours = True
horloge = pygame.time.Clock()

while jeu_en_cours:
    for event in pygame.event.get():
        if event.type == QUIT:
            jeu_en_cours = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                raquette_joueur1_bouge_haut = True
            elif event.key == K_s:
                raquette_joueur1_bouge_bas = True
            elif event.key == K_UP:
                raquette_joueur2_bouge_haut = True
            elif event.key == K_DOWN:
                raquette_joueur2_bouge_bas = True
        elif event.type == KEYUP:
            if event.key == K_w:
                raquette_joueur1_bouge_haut = False
            elif event.key == K_s:
                raquette_joueur1_bouge_bas = False
            elif event.key == K_UP:
                raquette_joueur2_bouge_haut = False
            elif event.key == K_DOWN:
                raquette_joueur2_bouge_bas = False

    # Mouvement des raquettes
    if raquette_joueur1_bouge_haut and raquette_joueur1.top > 0:
        raquette_joueur1.y -= vitesse_raquette
    if raquette_joueur1_bouge_bas and raquette_joueur1.bottom < hauteur_ecran:
        raquette_joueur1.y += vitesse_raquette
    if raquette_joueur2_bouge_haut and raquette_joueur2.top > 0:
        raquette_joueur2.y -= vitesse_raquette
    if raquette_joueur2_bouge_bas and raquette_joueur2.bottom < hauteur_ecran:
        raquette_joueur2.y += vitesse_raquette

    # Mouvement de la balle
    balle.x += vitesse_balle_x
    balle.y += vitesse_balle_y

    # Rebond de la balle sur les bords supérieur et inférieur
    if balle.top <= 0 or balle.bottom >= hauteur_ecran:
        vitesse_balle_y *= -1

    # Rebond de la balle sur les raquettes
    if balle.colliderect(raquette_joueur1) or balle.colliderect(raquette_joueur2):
        vitesse_balle_x *= -1

    # Vérification de la victoire
    if balle.left <= 0:
        gagnant_texte = font.render("Joueur 2 a gagné !", True, BLANC)
        ecran.blit(gagnant_texte, (largeur_ecran // 4, hauteur_ecran // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Attendre 2 secondes
        jeu_en_cours = False
    elif balle.right >= largeur_ecran:
        gagnant_texte = font.render("Joueur 1 a gagné !", True, BLANC)
        ecran.blit(gagnant_texte, (largeur_ecran // 4, hauteur_ecran // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Attendre 2 secondes
        jeu_en_cours = False

    # Dessin de l'écran de jeu
    ecran.fill(NOIR)
    pygame.draw.rect(ecran, BLANC, raquette_joueur1)
    pygame.draw.rect(ecran, BLANC, raquette_joueur2)
    pygame.draw.ellipse(ecran, BLANC, balle)
    pygame.draw.aaline(ecran, BLANC, (largeur_ecran // 2, 0), (largeur_ecran // 2, hauteur_ecran))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limite de vitesse de la boucle principale
    horloge.tick(60)

# Fermeture de Pygame
pygame.quit()
