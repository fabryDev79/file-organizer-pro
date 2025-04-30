# FILE ORGANIZER PRO
# by @Fabry79
# Organizza automaticamente i tuoi file per tipo o per data

print("""
  ______ _ _       ____                        _             
 |  ____(_) |     |  _ \                      (_)            
 | |__   _| | ___ | |_) | ___ _ __   ___  _ __ _ _ __   __ _ 
 |  __| | | |/ _ \|  _ < / _ \ '_ \ / _ \| '__| | '_ \ / _` |
 | |    | | |  __/| |_) |  __/ | | | (_) | |  | | | | | (_| |
 |_|    |_|_|\___||____/ \___|_| |_|\___/|_|  |_|_| |_|\__, |
                                                        __/ |
                                                       |___/ 
                    FILE ORGANIZER PRO
                    by @Fabry79
""")

import os
import shutil
from datetime import datetime

def organize_by_type(folder_path):
    print(f"\n[INFO] Organizzazione per tipo in corso nella cartella: {folder_path}")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_dir = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(file_path, os.path.join(target_dir, filename))
    print("[DONE] Organizzazione per tipo completata.")

def organize_by_date(folder_path):
    print(f"\n[INFO] Organizzazione per data in corso nella cartella: {folder_path}")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            modified_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d')
            target_dir = os.path.join(folder_path, date_folder)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(file_path, os.path.join(target_dir, filename))
    print("[DONE] Organizzazione per data completata.")

if __name__ == "__main__":
    folder = input("Inserisci il percorso della cartella da organizzare: ").strip()
    mode = input("Vuoi organizzare per [T]ipo o per [D]ata? ").strip().lower()

    if not os.path.exists(folder):
        print("[ERRORE] Il percorso non esiste. Controlla e riprova.")
    else:
        if mode == 't':
            organize_by_type(folder)
        elif mode == 'd':
            organize_by_date(folder)
        else:
            print("[ERRORE] Scelta non valida. Usa 'T' o 'D'.")



# ESEMPIO USO:
# organize_by_type("/percorso/della/cartella")
# organize_by_date("/percorso/della/cartella")