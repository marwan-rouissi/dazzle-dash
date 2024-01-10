# dazzle-dash

## Le Data Storytelling

Le Data Storytelling, ou la "narration de données" en français, est l'art de raconter une histoire en utilisant des données. Il s'agit de prendre des données brutes (chiffres, statistiques, etc.) et de les présenter de façon narrative afin de les rendre plus accessibles et engageantes pour un public. En d'autres termes, le Data Storytelling consiste à utiliser des données pour construire une narration convaincante et significative, permettant aux spectateurs de mieux comprendre les tendances, les insights et les implications des données présentées.

Voici quelques éléments clés du data storytelling:

- Raconter une histoire: le but est de transformer des données en une narration avec un début, un développement et une conclusion, afin de captiver l'attention de l'auditeur et donner du sens aux données exploitées.
- Visualiser les données: des graphiques, tableaux, cartes, frises chronologiques etc. sont utilisés pour représenter visuellement les données et supporter le récit.
- Mettre l'accent sur l'humain: le storytelling donne un aspect plus humain et émotionnel aux données en les reliant à des expériences personnelles.
- Simplifier: le langage et les visuels sont simplifiés pour rendre les données accessibles au plus grand nombre.
- Raconter une histoire engageante: en utilisant des techniques narratives comme la dramatisation, l'humour, la surprise, pour captiver l'audience.
- Le data storytelling est utilisé dans de nombreux domaines (journalisme, marketing, éducation, etc.) pour présenter des données complexes de façon simple et engageante. C'est un puissant outil de communication et de prise de décision basée sur les données.


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