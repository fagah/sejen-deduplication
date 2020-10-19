from future.builtins import next

import os
import csv
import re
import logging
import optparse

import dedupe
from unidecode import unidecode


def preProcess(column):
    """
    Nettoyage des données a l’aide d’Unidecode et de Regex.
Des éléments tels que la casse, les espaces supplémentaires, les quotes et 
le caractee1ère pour les nouvelles lignes peuvent être ignorés.
    """
    try : # python 2/3 string differences
        column = column.decode('utf8')
    except AttributeError:
        pass
    column = unidecode(column)
    column = re.sub('  +', ' ', column)
    #column = re.sub('-', '', column)
    column = re.sub('\t', '', column)
    column = re.sub('\n', ' ', column)
    column = column.strip().strip('"').strip("'").lower().strip()
    # Si des données sont manquantes, indiquez-le en définissant la valeur a 'None'.
    if not column:
        column = None
    return column

def readData(filename):
    """
    Lecture des données à partir d'un fichier CSV et création d'un dictionnaire de données,
     où la clé est un identifiant d'enregistrement unique et chaque valeur est un dictionnaire
    """

    data_d = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            
            clean_row = [(k, preProcess(v)) for (k, v) in row.items()]
            row_id = int(row['id'])
            data_d[row_id] = dict(clean_row)

    return data_d

if __name__ == '__main__':
    
    optp = optparse.OptionParser()
    optp.add_option('-v', '--verbose', dest='verbose', action='count',
                help='Increase verbosity (specify multiple times for more)'
                )
    (opts, args) = optp.parse_args()
    log_level = logging.WARNING 
    if opts.verbose:
        if opts.verbose == 1:
            log_level = logging.INFO
        elif opts.verbose >= 2:
            log_level = logging.DEBUG
    logging.getLogger().setLevel(log_level)

    # ## Setup
    
    input_file = 'small_dataset.csv'
    output_file = 'doublon4_out.csv'
    settings_file = 'doublon_setting'
    training_file = 'doublon_training.json'
    
    print('importing data ...')
    data_d = readData(input_file)
    
    # Si un fichier de paramètres existe déjà, nous allons simplement le charger et ignorer 
    # l'apprentissage
    if os.path.exists(settings_file):
        print('reading from', settings_file)
        with open(settings_file, 'rb') as f:
            deduper = dedupe.StaticDedupe(f)
    else:
        # ## Training
    
        # Définir les champs sur lesquels Dedupe sera attentif
        
        fields = [
        {'field' : 'family_name', 'type': 'String'},
        {'field' : 'given_name', 'type': 'String'},
        {'field' : 'cel_n0', 'type': 'String','has_missing':True},
        {'field' : 'tel_n0', 'type': 'String','has_missing':True},
        {'field' : 'birthdate', 'type': 'String','has_missing':True},
        {'field' : 'gender', 'type': 'Exact'},
        {'field' : 'ville_n0', 'type': 'String','has_missing':True},
        {'field' : 'commune_n0', 'type': 'String','has_missing':True}
            ]
    
        # Créer un nouvel objet dedupe et lui transmettre notre modèle de données.
        deduper = dedupe.Dedupe(fields)
    
        #Pour entraîner dedupe, nous lui fournissons un échantillon de données.
        #deduper.sample(data_d, 15000)
        deduper.prepare_training(data=data_d, sample_size=15000)
    
        # Si nous avons des données d'apprentissage sauvegardées à partir d’une exécution précédente de 
        #dedupe,on le cherche et on le charge.
        #si nous voulons  entraîner dedupe à partir de zéro, il faudra supprimer le fichier training_file
        if os.path.exists(training_file):
            print('reading labeled examples from ', training_file)
            with open(training_file, 'rb') as f:
                deduper.read_training(f)
    
        #Apprentissage actif
        #Dedupe trouvera la prochaine paire d'enregistrements
        # Lorsqu'il est moins certain il  demande de les étiqueter comme des doublons ou pas.
        # L'on utilise les touches 'y', 'n' et 'u' pour marquer les doublons appuyez sur 'f' lorsque vous avez terminé
        print('starting active labeling...')
    
        dedupe.console_label(deduper)
    
        # Phase d'apprentissage de dedupey
        deduper.train()
    
        # Sauvegarde
        with open(training_file, 'w') as tf:
            deduper.write_training(tf)
    
        # Enregistrement des poids et prédicats sur le disque. Si le fichier de paramètres
        #existe, nous ignorerons tout l'apprentissage lors de la prochaine exécution de ce fichier.
        with open(settings_file, 'wb') as sf:
            deduper.write_settings(sf)
            
