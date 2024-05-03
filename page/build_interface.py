"""
    Author: HELOU Komlan Mawulé
    But: Définition une fonction de créeation l'interface utilisateur
    Date: 02-05-2024
"""
#Bibliothèque python
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

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

    numero_facture = ctk.CTkEntry(frame, width=850, height=sett.entry_height ,placeholder_text=txt.numero_facture_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_1)
    numero_facture.pack()

    nom_client = ctk.CTkEntry(frame, width=850, height=sett.entry_height ,placeholder_text=txt.nom_client_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_1)
    nom_client.pack()

    objet_facture = ctk.CTkEntry(frame,width=850,  height=sett.entry_height ,placeholder_text=txt.objet_facture_placeholder, justify= "left",
                            corner_radius=sett.border_entry_radius, border_color=sett.border_entry_color, font=sett.font_text_1)
    objet_facture.pack()



def entete_du_tableau(scrollFrame):
    frame = ctk.CTkFrame(scrollFrame, height=75, fg_color="green", border_color="#000", corner_radius=0)
    frame.pack()

    #Numero d'ordre
    numero_ordre = ctk.CTkEntry(frame,width=frame.winfo_width()*50, justify = "center", corner_radius=sett.border_entry_radius,font=sett.font_text_2, 
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
    numero_ordre.pack(side="left")
    numero_ordre.insert(0,"N°")
    numero_ordre.configure(state = "disable")

    #Nom du produit ou du service
    nom_poduit =ctk.CTkEntry(frame,width=frame.winfo_width()*500, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
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
        Procédure pour générer une ligne de produit (un frame contenant des entrys: Numero d'ordre, Nom du produit
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
    nom_poduit =ctk.CTkEntry(frame,width=frame.winfo_width()*500, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
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
    
    liste_des_produits.append(frame)

    #montant du produit

    montant_produit =ctk.CTkEntry(frame,width=frame.winfo_width()*100, justify = "left", corner_radius=sett.border_entry_radius, font=sett.font_text_2,
                                border_color=sett.border_entry_color , text_color= sett.text_entry_color, border_width=sett.border_entry_width)
   
    montant_produit.pack(side="left")



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
    fen.title(txt.title_application)
    fen.iconbitmap('image/logo.ico')
    fen._set_appearance_mode(sett.col_fond)
    fen.configure(fg_color=sett.col_fond)
    
    #Zone de définition des elements de la facture
    les_element_princiapux=ctk.CTkFrame(fen, height=fen.winfo_height()*0.1, fg_color=sett.col_fond)

    les_element_princiapux.pack(fill="both", padx=15, pady=5, side= "top")
    
    information(les_element_princiapux)
    #Zone de saisi des produits
    contenu_principal = ctk.CTkScrollableFrame(fen,height=510, fg_color=sett.col_fond)
    contenu_principal.pack(fill="both" ,padx= 15, pady=5)

    liste_des_produits.append(entete_du_tableau(contenu_principal))
    nombre_produit+=1
    #zone des bouton
    contenu_bouton_principaux=ctk.CTkFrame(fen, height=fen.winfo_height()*0.1, fg_color= sett.col_fond)
    contenu_bouton_principaux.pack(fill="both", padx=15, pady=5, side= "bottom")

    #Bouton pour ajouter
    Ajouter_un_produit = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_ajout_produit , width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_1,
                                      command= lambda: ajouter_produit(contenu_principal) )
    Ajouter_un_produit.pack(padx=10,pady=15, side ="left")

    #Bouton pour supprimer
    supprimer_un_produit = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_supprimer_produit , width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_1,
                                      command= lambda: supprimer_produit(contenu_principal) )
    supprimer_un_produit.pack(padx=10,pady=15, side ="left")
    
    #Evaluer la facture
    evaluer_facture = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_evaluer_facture, width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_1,
                                      command= lambda:print("000") )
    evaluer_facture.pack(padx=10,pady=15, side ="left")

    #Bouton pour Voir l'apercu de la facture
    voir_facture = ctk.CTkButton(contenu_bouton_principaux,text=txt.bouton_apercu_facture, width=sett.width_bouton, height= sett.height_bouton
                                      ,fg_color= sett.fg_bouton_color, hover_color=sett.fg_bouton_hover_color , font=sett.font_text_1,
                                      command= lambda: imprimer_facture(les_element_princiapux) )
    voir_facture.pack(padx=10,pady=15, side ="left")




    fen.mainloop()


