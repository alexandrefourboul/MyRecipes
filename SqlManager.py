import sys
import psycopg2
import datetime
import traceback
from utils.requests_recipe import *


# SqlManager : Objet agissant comme un canal entre la base de données et python
class SqlManager(object):
    def __init__(self, database, username, passwd, host, port=5432):
        "établissement de la connexion - Creation du curseur"
        try:
            self.db = psycopg2.connect(host=host, user=username, password=passwd, database=database, port=port)
            self.db.set_client_encoding('UTF8')
        except Exception as err:
            print('La connexion avec la base de donnees a chou :\n' \
                  'Erreur dtece :\n%s' % err)
            self.echec = 1
        else:
            print("Connexion au serveur POSTGRES OK")
            self.cursor = self.db.cursor()  # cration du curseur
            self.echec = 0

    def query(self, req, param=None):
        try:
            self.cursor.execute(req, param)
        except Exception as err:
            print("Requte SQL incorrecte :\n{}\nErreur dtecte :".format(req))
            print(err)
            return 0
        else:
            return 1

    def db_add_recipe(self, values):
        self.query(req_add_recipe, values)
        self.db.commit()

    def db_add_one_step(self, values):
        self.query(req_add_one_step, values)

    def db_add_recipe_steps(self, values_list):
        for row in values_list:
            self.db_add_one_step(row)
        self.db.commit()

    def db_add_one_ingredient(self, values):
        self.query(req_add_one_ingredient, values)

    def df_add_ingredients(self, values_list):
        for row in values_list:
            self.db_add_one_ingredient(row)
        self.db.commit()

    # handler pour les messages entrants par le flux mytraindata
    # Met à jour toutes les tables suite à l'arrivée d'un message
    """def transfer_message_avise(self, event):
        # Récupération des éléments utiles du json
        statement_time = datetime.datetime.fromtimestamp(event['date_releve'])
        marti = event['device']['id']
        time_set2 = datetime.datetime.now()
        payload = event['data']['payload_decrypte']
        fcntup = event['counter_lpwan']
        time_database = datetime.datetime.fromtimestamp(event['date_reception_ptf'])
        type_trame = event['id_trame']
        try:
            meli_id = event['connectivite']['Lrrid']
        except :
            meli_id = "erreurDB"


        cur_msg = payload[:2]
        prev_msg = None
        num_train = None
        #Si c'est une trame de mesure (0x05), alors on cherche à récupérer les infos de circulations (quand elles existent)
        if type_trame == '0x05':
            try:
                num_train = int(event['data']['circulation']['num_train'])
            except ValueError:
                num_train = None
            cur_msg = event['data']['etat_courant']['code_message']
            prev_msg = event['data']['etat_precedent']['code_message']
        #Si N°train existe : on recupère le id_train de la table train associé
        if num_train is not None:
            id_train = self.update_train(event, num_train, statement_time)
        else:
            id_train = None
        #Insertion du message / pré-remplissage du précédent si besoin / remplissage du message courant is deja existant
        self.query(req_insert_avise, (
            marti, statement_time, cur_msg, payload, fcntup, prev_msg, time_database, id_train, meli_id, time_set2,
            statement_time.date()))
        self.db.commit()
        #Met à jour les infos de communication du MARTI et de la MELI
        self.update_ref(meli_id, marti, statement_time)

    # Met à jour la table train selon les attribut du message reçu
    # Retourne l'id_train correspondant dans la table train
    def update_train(self, event, num_train, statement_time):
        #On essaye de récuperer la ligne contenant le N° train et la date train du message
        self.cursor.execute(req_get, (num_train, statement_time.date()))
        row = self.cursor.fetchone()
        try:
            num_resa = int(event['data']['circulation']['num_reservation']) - 1
        except:
            num_resa = -1
        full_car_number = full_name_voiture(event['identification_mr']['num_imat_ef_rame'])
        #Si le train n'existe pas en base
        if row is None:
            cars = [None] * 30
            msgs = [0] * 30
            cars[num_resa] = full_car_number
            msgs[num_resa] += 1
            #On crée le train dans la table train
            self.cursor.execute(req_new_train,
                                (num_train, statement_time, statement_time, cars, msgs, statement_time.date()))
            self.db.commit()
            #On récupere le dernier id créée (le train que l'on vient d'insérer)
            self.cursor.execute(req_max_id_train)
            return self.cursor.fetchone()[0]
        #Si le train existe en base
        else:
            row[4][num_resa] = full_car_number
            row[5][num_resa] += 1
            #On met à jour la ligne du train grâce aux données du message
            self.cursor.execute(req_update_train, (statement_time, statement_time, statement_time, statement_time,
                                                   statement_time, statement_time, row[4], row[5], row[0]))
            self.db.commit()
            return row[0]

    #Met à jour les tables référentielles des MARTI et des MELI (uniquement les last_comm )
    def update_ref(self, meli_id, marti_num, statement_time):
        #MAJ MARTI
        try:
            self.cursor.execute(req_update_marti, (statement_time, statement_time, marti_num))
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        #MAJ MELI
        try:
            self.cursor.execute(req_update_meli, (statement_time, statement_time, meli_id))
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        self.db.commit()

    # handler pour les messages entrants par le flux mytraindata_autres_profiles
    # Met à jour toutes les tables suite à l'arrivée d'un message
    def transfer_message_autres_profiles(self, event):
        # Récupération des éléments utiles du json
        statement_time = datetime.datetime.fromtimestamp(event['date_releve'])
        marti = event['device']['id']
        time_set2 = datetime.datetime.now()
        payload = event['data']['payload_decrypte']
        fcntup = event['counter_lpwan']
        time_database = datetime.datetime.fromtimestamp(event['date_reception_ptf'])
        type_trame = event['id_trame']
        config = event['config_marti']['config_id']
        try:
            meli_id = event['connectivite']['Lrrid']
        except:
            meli_id = "erreurDB"

        v1_usecase, v1_type_mesure, v1_type_capteur, v1_valeur, v1_unite, v1_valeur_interpretee, v1_unite_interpretee = None, None, None, None, None, None, None
        v2_usecase, v2_type_mesure, v2_type_capteur, v2_valeur, v2_unite, v2_valeur_interpretee, v2_unite_interpretee = None, None, None, None, None, None, None
        # Si c'est une trame de mesure (0x03), alors on cherche à récupérer les valeurs utiles
        if type_trame == '0x03':
            try:
                v1_usecase = event['data']['voie1'].pop("usecase")['code'],
                v1_type_mesure, v1_type_capteur, v1_valeur, v1_unite, v1_valeur_interpretee, v1_unite_interpretee = \
                    event['data']['voie1'].values()
            except (TypeError,AttributeError):
                pass
            try:
                v2_usecase = event['data']['voie2'].pop("usecase")['code'],
                v2_type_mesure, v2_type_capteur, v2_valeur, v2_unite, v2_valeur_interpretee, v2_unite_interpretee = \
                    event['data']['voie2'].values()
            except (TypeError,AttributeError):
                pass
        #On insère la nouvelle ligne de données dnas la table other_profiles
        self.query(req_insert_other, (
            marti, config, type_trame[-2:], fcntup, statement_time, time_database, time_set2, payload, meli_id,
            v1_usecase, v1_valeur, v1_unite, v1_valeur_interpretee, v1_unite_interpretee,
            v1_type_capteur, v1_type_mesure, v2_usecase, v2_valeur, v2_unite, v2_valeur_interpretee,
            v2_unite_interpretee, v2_type_capteur, v2_type_mesure,statement_time.date()))
        self.query(req_update_marti_sanitaire,(statement_time, statement_time, marti))
        self.db.commit()

#Complète un N°voiture incomplet (Numéro Européen + chiffre d'auto-contrôle)
def full_name_voiture(v):
    n = len(v)
    if n == 12:
        return v
    elif n == 7:
        v = '5087' + v
    elif n == 9:
        v = '50' + v
    return v + auto_controle(v)

# à partir des 11 chiffres de la voiture , on reconstruit le chiffre d'auto-contrôle
def auto_controle(v):
    i = -1
    s = 0
    for c in v:
        i += 1
        cint = int(c)
        if i % 2:
            s += cint
        elif cint > 4:
            s += 1 + (2 * cint - 10)
        else:
            s += 2 * cint
    reste = s % 10
    if reste > 0:
        return str(10 - reste)
    else:
        return '0'"""
