from glob import glob
from datetime import datetime, timedelta

import os
def main():
    

    

    # Obtenez la date d'aujourd'hui
    today = datetime.today()

    # Obtenez le premier jour du mois actuel
    first_day_of_current_month = today.replace(day=1)

    # Soustrayez un jour pour obtenir le dernier jour du mois précédent
    last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

    print(last_day_of_previous_month.strftime('%Y%m%d'))
    data_files = glob(f'./prd/*{last_day_of_previous_month}.txt')
    if len(data_files) ==10:
        print(data_files)
        print(len(data_files))

        os.exec('python monscript.py ')





if __name__=='__main__':
    main()
