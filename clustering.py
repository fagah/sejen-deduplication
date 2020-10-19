from future.builtins import next

import sys
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
        print('#################################################################################')
        sys.exit('Unable to continue without training step. Please run the training file first!!')


    # Ici nous cherchons le seuil qui maximisera une moyenne pondérée entre la précision et le rappel. 
    #Lorsque nous fixons le poids de rappel à 2, nous sommes disons que nous nous soucions deux fois plus du rappel
    # que de la précision.
    
    clustered_dupes = deduper.partition(data_d, 0.5)
    
    # ## Clustering
    
    # La fonction match renverra un ensemble d'identifiants d'enregistrements qui selon dedupe font tous
    # référence à la meme entite
    
    print('# duplicate sets', len(clustered_dupes))
          
    cluster_membership = {}
    for cluster_id, (records, scores) in enumerate(clustered_dupes):
        for record_id, score in zip(records, scores):
            cluster_membership[record_id] = {
                "Cluster ID": cluster_id,
                "confidence_score": score
            }
    
    with open(output_file, 'w') as f_output, open(input_file) as f_input:
    
        reader = csv.DictReader(f_input)
        fieldnames = ['Cluster ID', 'confidence_score'] + reader.fieldnames
    
        writer = csv.DictWriter(f_output, fieldnames=fieldnames)
        writer.writeheader()
    
        line_number = 1
        for row_id, row in enumerate(reader):
            print(row_id)
            print(row)
            print('##################################################################')
            print(cluster_membership)
            if(row_id < len(cluster_membership)):
                row.update(cluster_membership[line_number])
                writer.writerow(row)
                line_number = line_number + 1
