"""
    Author: HELOU Komlan Mawulé
    But: Définition des fonctions de validations des champs de saisie
    Date: 03-05-2024
"""
#bibliothèque de python
import customtkinter as ctk
import tkinter as tk

#mes mùodules
import page.setting as set

def validation_des_informations(frame):
    """
        La fonction permet de valider les informations d'entete de la facture ( nom client, numéro facture, objet)
        @param: Frame (la zone contenant les informations du paramètres)
        @return: Boolean stipulant que toutes les informations sont correctes
    """
    information_valide= []
    for widget in frame.winfo_children():
        if isinstance(widget, ctk.CTkEntry):
            valeur = widget.get()
            if valeur :
                information_valide.append(True)
                widget.configure(border_color = set.champ_valide_color)
            else :
                information_valide.append(False)
                widget.configure(border_color = set.champ_invalide_color)
    
    return all(information_valide)



def validation_produit(produit_entry):
    """
    C'est une fonction qui permet de valider les informations d'un produit
    @param: tuple représentant les information du produit
    @return : Boolean
    """

    numero_ordre_entry = produit_entry[0]
    nom_entry = produit_entry[1]
    unite_entry= produit_entry[2]
    quantite_entry= produit_entry[3]
    prix_unitaire_entry = produit_entry[4]
    montant_entry = produit_entry[5]

    numero_ordre_entry.configure(state = tk.NORMAL)

    numero_ordre = numero_ordre_entry.get()
    nom_produit = nom_entry.get() ; nom_ok = False
    unite_produit = unite_entry.get()  ; unite_okv= False
    quantite_produit = quantite_entry.get(); quantite_ok = False
    prix_unitaire_produit = prix_unitaire_entry.get(); prix_uni_produit = False
    montant_entry.configure(state = tk.NORMAL)





def validation_des_produits(liste):
    """
    La fonction permet de valider le champs de saisi des informations du produits et calcul 
    @param: liste de tuple (numero_ordre, nom_poduit, unite_produit, quantite_produit, prix_unitaire_produit, montant_produit)
            représentant les champs de saisi des informations du produit
    @return: Boolean
    """

