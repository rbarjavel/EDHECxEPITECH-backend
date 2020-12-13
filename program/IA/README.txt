pip install:
    nltk
    pickle
    numpy
    tensorflow

Utilisation:
    lancer EasyStock.py => affiche les catégories reconnues dans la phrase.
    L'envoie des values reconnues à l'api de Kéké n'est pas encore implémenté.
    Pour le moment la phrase est rentrée en dur dans le code.
    
    On recoit une phrase ex: "je cherche une robe rouge faite en coton en taille L".
    L'IA renvoie un dictionnaire contenant le type, la couleur, le tissue et la taille du produit recherché.

Modifications:
    Pour ajouter des tissues, des couleurs, des types de vetements, ou des tailles procéder comme suit:
        Copier coller un intent complet dans le JSON correspondant à la catégorie.
        Modifier les valeurs.

        Les valeurs sont comme suit:
            tag = le nom de la catégorie de reconnaissance (par souci de simplicité on mettra le même nom que la response).
            patterns = les différentes écritures que l'IA devra reconnaitre pour déterminer la catégorie (différentes orthographes ici). On peut aussi rentrer des groupes de mots si necessaire.
            responses = la valeur renvoyée par l'IA dans le dictionnaire.

    Une fois que les modifications sont appliquées dans les JSONS il faudra lancer le programme pour réentrainer l'IA: retrain_model.py

Warnings:
    Au premier lancement la librairie nltk pourrait générer une erreur disant qu'un paquet est manquant.
    Pour régler ce probleme verriier que la commande nltk.download('punkt') dans gui_deepchat.py est décommentée.
    Si le problème persiste contacter Romain mdr.

    NE PAS supprimer les fichiers plk et h5, ce sont les fichiers 'cerveau' du modèle. Sans ça l'IA est cassée et le modèle doit être recréé.