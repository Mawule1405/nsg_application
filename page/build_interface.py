"""
    Author: HELOU Komlan Mawulé
    But: Définition une fonction de créeation l'interface utilisateur
    Date: 02-05-2024
"""
#Bibliothèque python
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import tkinter as tk

#Module lié à l'application
import page.texte as txt
import page.setting as sett
import page.validation as val

nombre_produit = 0
liste_des_produits = []
application_de_psd = True


def imprimer_facture(frame):
    valide = val.validation_des_informations(frame)

    if(valide):
        if liste_des_produits:
            les_produits =[]
            for frame in liste_des_produits:
                les_elements= []
                for widget in frame.winfo_children():
                    les_elements.append(widget)
                les_produits.append(tuple(les_elements))
                print(les_elements)
    else:
        messagebox.showerror("Information", "Valeur manquante")
        


def information(frame):
    """
    Construction de l'entete du formulaire de production de la facture contenant les information:
     titre du formulaire, nom client, numero de la facture et l'objectif de la facture
     @param: frame (zone d'affichage des informations)
     @return: tuple des entry (nom_client, numero de la facture, objectifs de la facture)
    """
    ctk.CTkLabel(frame, text= txt.titre_formulaire, font  =  sett.font_text_1).place(x=50 ,y =5)

    ctk.CTkLabel(frame, text= txt.numero_facture, font  =  sett.font_text_2).place(x=0 ,y =40)
    numero_facture = ctk.CTkEntry(frame, width=300, height=sett.entry_height ,placeholder_text=txt.numero_facture_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_2)
    numero_facture.place(x=150 ,y =40)

    ctk.CTkLabel(frame, text= txt.nom_client, font  =  sett.font_text_2).place(x=0 ,y =80)
    nom_client = ctk.CTkEntry(frame, width=520, height=sett.entry_height ,placeholder_text=txt.nom_client_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_2)
    nom_client.place(x=150 ,y =80)

    ctk.CTkLabel(frame, text= txt.objet_facture, font  =  sett.font_text_2).place(x=0 ,y =120)
    objet_facture = ctk.CTkEntry(frame,width=520,  height=sett.entry_height ,placeholder_text=txt.objet_facture_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_2)
    objet_facture.place(x=150 ,y =120)

    return nom_client, numero_facture, objet_facture



def entete_du_tableau(scrollFrame):
    """
    Pour construire l'entete du tableau de la facture sous forme de grille avec les colonnes
    numero d'ordre, Nom du produit, Unité, Quantité, Prix unitaire, Montant
    @param: scrollFrame ( pour contenir toutes les lignes du tableau de la saisie)
    @return : None
    """
    frame = ctk.CTkFrame(scrollFrame, height=75, fg_color="green", border_color="#000", corner_radius=0)
    frame.pack()

    #Numero d'ordre
    numero_ordre = ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius,font=sett.font_text_2, 
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
    numero_ordre.pack(side="left")
    numero_ordre.insert(0,"N°")
    numero_ordre.configure(state = "disable")

    #Nom du produit ou du service
    nom_poduit =ctk.CTkEntry(frame,width=frame.winfo_width()*300, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    nom_poduit.pack(side="left")
    nom_poduit.insert(0,"Nom du produit")
    nom_poduit.configure(state = "disable")

    #Unité du produit
    unite_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    unite_produit.pack(side="left")
    unite_produit.insert(0,"Unité")
    unite_produit.configure(state = "disable")

    #Quantité du produit
    quantite_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    quantite_produit.pack(side="left")
    quantite_produit.insert(0,"Qte")
    quantite_produit.configure(state = "disable")

    #prix unitaire
    prix_unitaire_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*100, justify = "right", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    prix_unitaire_produit.pack(side="left")
    prix_unitaire_produit.insert(0,"PU (FCFA)")
    prix_unitaire_produit.configure(state = "disable")
    
    #montant du produit

    montant_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*100, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    montant_produit.pack(side="left")
    montant_produit.insert(0,"Mnt (FCFA)")
    montant_produit.configure(state = "disable")

    return frame




def ajouter_produit(scrollFrame):
    """
        Procédure pour générer une ligne de produit (les entrys: Numero d'ordre, Nom du produit
        unité, quantité, le prix unitaire et le montant total)
        @param: scrollFrame: la zone scrollable dans laquelle le produit sera insérer
        @return: None
    """
    global nombre_produit
    
    frame = ctk.CTkFrame(scrollFrame, height=50, fg_color=sett.border_entry_color, border_color= sett.border_entry_color, corner_radius=0)
    frame.pack()

    #Numero d'ordre
    numero_ordre = ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
    numero_ordre.pack(side="left")
    numero_ordre.insert(0,nombre_produit)
    numero_ordre.configure(state = "disable")
    nombre_produit+=1
    #Nom du produit ou du service
    nom_poduit =ctk.CTkEntry(frame,width=frame.winfo_width()*300, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    nom_poduit.pack(side="left")

    #Unité du produit
    unite_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    unite_produit.pack(side="left")

    #Quantité du produit
    quantite_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    quantite_produit.pack(side="left")

    #prix unitaire
    prix_unitaire_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*100, justify = "right", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    prix_unitaire_produit.pack(side="left")
    

    #montant du produit
    montant_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*100, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width,
                                state="disable")
   
    montant_produit.pack(side="left")


    liste_des_produits.append((numero_ordre, nom_poduit, unite_produit, quantite_produit, prix_unitaire_produit, montant_produit))



def supprimer_produit(scrollFrame):
    """
        Procédure pour supprimer une ligne de produit (un frame contenant des entrys: Numero d'ordre, Nom du produit
        unité, quantité, le prix unitaire et le montant total)
        @param: scrollFrame: la zone scrollable dans laquelle le produit sera insérer
        @return: None
    """
    global nombre_produit

    if nombre_produit >1:
        
        dernier_widget  = ""
        for widget in enumerate( scrollFrame.winfo_children()):
            
            dernier_widget = widget[1]

        dernier_widget.destroy()
        nombre_produit-=1
        liste_des_produits.pop(-1)
    else:
        messagebox.showinfo(txt.boite_de_dialogue_suppression_title, txt.boite_de_dialogue_suppression_contenu)
    



def buildInterface():
    """
        Ce ci est une procédure permettant de créer l'interface de gestion 
        @param: None
        @return : None
    """
    global nombre_produit 

    fen = ctk.CTk()
    fen.geometry("900x750+400+0")
    fen.resizable(width=False,height=True)
    fen.title(txt.title_application)
    fen.iconbitmap('image/logo.ico')
    fen._set_appearance_mode(sett.col_fond)
    fen.configure(fg_color=sett.col_fond)
    
    #Zone de définition des elements de la facture
    les_element_princiapux=ctk.CTkFrame(fen, height=200, width=670, fg_color=sett.col_fond)

    les_element_princiapux.place(x=210 ,y =5)
    
    information(les_element_princiapux)
    #Zone de saisi des produits
    contenu_principal = ctk.CTkScrollableFrame(fen,height=500, width=670, fg_color=sett.col_fond)
    contenu_principal.place(x=210 ,y= 200)

    liste_des_produits.append(entete_du_tableau(contenu_principal))
    nombre_produit+=1

    #zone des bouton
    contenu_bouton_principaux=ctk.CTkFrame(fen, height= 800, width=90, fg_color= sett.col_fond, border_width=2)
    contenu_bouton_principaux.place( x=0, y=0)

    #Bouton pour ajouter
    Ajouter_un_produit = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_ajout_produit , width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_2,
                                      command= lambda: ajouter_produit(contenu_principal) )
    Ajouter_un_produit.pack(padx=10,pady=5)

    #Bouton pour supprimer
    supprimer_un_produit = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_supprimer_produit , width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_2,
                                      command= lambda: supprimer_produit(contenu_principal) )
    supprimer_un_produit.pack(padx=10,pady=5)
    
    #Evaluer la facture
    evaluer_facture = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_evaluer_facture, width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_2,
                                      command= lambda:print("000") )
    evaluer_facture.pack(padx=10,pady=5)

    #Bouton pour Voir l'apercu de la facture
    voir_facture = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_apercu_facture, width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_2,
                                      command= lambda: imprimer_facture(les_element_princiapux) )
    voir_facture.pack(padx=10,pady=5)




    fen.mainloop()


