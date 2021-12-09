import ftplib
import sys
import os
import sys
from settings import hostname, server, username, password, date

try:
    session = ftplib.FTP(server, username, password)
except:
    sys.exit(0)

def upload():
    try:
        session = ftplib.FTP(server, username, password)
        file = open(f'{backup_path}/minecraft.tar.gz','rb')
        session.storbinary('STOR backups/'+hostname+'_'+date+'.zip', file)
        file.close()
        session.quit()
        os.remove(f'{backup_path}/minecraft.tar.gz')
    except:
        print("Se produjo un error a la hora de subir el backup.")
        sys.exit(1)

def download():
    files = []
    try:
        session.cwd('backups')
        files = session.nlst()
        files.sort(reverse=True)
        if len(files) > 0:
            last_backup=files[0]
        else:
            print("No existe ningún backup.")
            sys.exit()
    except:
        print("Se produjo un error a la hora de listar los backups.")
        sys.exit(1)

    try:
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)
        session.retrbinary('RETR '+last_backup ,open(f'{backup_path}/minecraft.tar.gz', 'wb').write)
        session.quit()
    except:
        print("Se produjo un error a la hora de descargar el backup.")
        sys.exit(1)

try:
    if len(sys.argv) == 2:
        backup_path = "../../backup"
    elif len(sys.argv) == 3:
        backup_path = sys.argv[2]
    else:
        print("Necesitas especificar 'upload' o 'download' para ejecutar el script.")
        sys.exit()
    if sys.argv[1] == "upload":
        upload()
    elif sys.argv[1] == "download":
        download()
    else:
        print("Necesitas especificar 'upload' o 'download' para ejecutar el script.")
        sys.exit()
except:
    print("Ha ocurrido un error a la hora de ejecutar el script.")
