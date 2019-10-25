from dikssionnaire import villes,test
import math
import os 


def start():
    start = input(" la ville de départ : ")
    finish = input("la ville d'arrivée : ")
    return start, finish


def trajet(start, finish):
        if(start in villes):
            if(finish in villes):
                vitesse,secondes,heures,minutes,distanceparcourue,pauses,pause,lastpause = 0,0,0,0,0,0, False,0
                lastpause = 0
                distance = villes[start][finish]
                print("Distance entre les villes : ", distance, "km")
                while(distanceparcourue < distance * 1000):
                    secondes += 1
                    if(secondes % 60 == 0):
                        if(vitesse < 90):
                            if(pause == False):
                                vitesse += 10
                                print('Accélération')
                    if( (secondes - lastpause) % 7200 == 0):
                        pause = True
                        pauses += 1
                    if(pause and secondes % 60 == 0):
                        vitesse -= 10
                        print('Décélération')
                    if(pause and vitesse == 0):
                        secondes += 60 * 15
                        lastpause = secondes
                        pause = False
                        print("Hey faut prendre une pause hésite pas pendant ce temps à souscrire à un abonnement AwayFromNetwork")       
                    distanceparcourue += vitesse / 3.6
                if(secondes/60 > 0):
                    if(secondes/3600 > 0):
                        heures = math.floor(secondes/3600)
                    minutes = math.ceil((secondes % 3600)/60)
                print("C Finis merci à toi et n'oublie pas tu peux souscrire à un abonnement AwayFromNetwork")
                print('Distance parcourue : ', distanceparcourue / 1000, 'km en : ', heures, 'heures', 'et ', minutes,'minutes.')
                print('Nombre de pauses prises : ', pauses)
                return 0


start,finish = start()
test()

print("Ville de départ : ", start)
print("Ville d'arrivée : ", finish)
trajet(start,finish)

input("c'est fini tu peux partir ou sinon tu peux relancer le programme et souscrire à un abonnement AwayFromNetwork")
