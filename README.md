# dazzle-dash

## Veille sur Dash
## Introduction
Dash est un framework open source développé par Plotly et permet la création d'applications web interactives en utilisant Python.
Il repose sur une architecture déclarative, permettant de décrire le comportement de l'application en utilisant Python sans avoir a manipuler directement du HTML, du CSS ou du JavaScript. Cela permet de faciliter le processus de développement.

Au cœur de Dash se trouve la bibliothèque Plotly, renommée pour ses graphiques interactifs. Dash s'appuie sur cette capacité pour créer des applications dynamiques dotées de visualisations de données attrayantes. Avec une variété de composants interactifs, tels que des graphiques, des tableaux, des boutons et des champs de texte, Dash offre une expérience utilisateur riche et personnalisable.

Dash est construit autour de trois piliers essentiels:  
- [ ] Le Layout
- [ ] Les Callback
- [ ] Les Composants

### Layout
Il permet de définir la structure de l'application web en jouant le même rôle que le HTML d'une page web.  
Avec le layout on peut donc choisir l'agencement des différents composants les uns par rapport aux autres sur la page. 
La librairie contient des classes représentant chaque tag HTML (div, table, span etc...) ce qui permet de définir précisemment la structure HTML de l'application web.

### Callback
Les callbacks sont l'un des points forts de Dash car c'est cela qui rend l'application interactive. 
Ils permettent de déclencher une fonction lorsqu'un utilisateur fait une action précise. 
En outre, un callback est un décorateur Python composé: 
- [X] d'une fonction a exécuter.
- [X] d'un déclencheur (Input), qui est un composant du layout dont le changement déclenchera la fonction.
- [X] d'au moins une sortie (Output), qui est un composant du layout qui reçoit la ou les valeurs retournée(s) par la fonction.
- [X] en option, d'autres composants du layout comme les States par exemple qui sont passés comme arguments d'une fonction. 

Ces fonctions Python lient les composants de l'interface utilisateur aux actions de l'utilisateur, permettant ainsi des mises à jour dynamiques et en temps réel d'autres éléments de l'application. Cette fonctionnalité offre une interactivité sans faille et une personnalisation adaptative, offrant une expérience utilisateur immersive.

### Composant
Dash permet d'ajouter de nombreux composants comme des tags HTML, des graphes, des tableaux interactifs, des menus etc...
Cette diversité de composants toujours croissante rend Dash très flexible et permet de réaliser des applications web aux fonctionnalités riches et variées.  

Dash propose également une intégration transparente avec Pandas, facilitant le chargement et la manipulation de données pour une analyse plus approfondie. De plus, les applications Dash peuvent être déployées sur diverses plateformes, garantissant une accessibilité facile pour les utilisateurs finaux.