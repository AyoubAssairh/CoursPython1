#On demande au joueur son nom et son score précédent
nom_joueur = input('Saisissez votre nom :')
score = input('Saissez votre score précédent :')

if score.isdigit():
    score = int(score) + 1
    print(nom_joueur,'a obtenu', score, 'points.')
else:
    print("Erreur !!")

print(nom_joueur,'a obtenu', score,'points.')