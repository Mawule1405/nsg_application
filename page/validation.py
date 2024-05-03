"""
    Author: HELOU Komlan Mawulé
    But: Définition des fonctions de validations des champs de saisie
    Date: 03-05-2024
"""
#bibliothèque de python
import customtkinter as ctk

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