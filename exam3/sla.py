import sys

def show_sla(pourcentage):
    pourcentage = 365.25 - ((pourcentage * 365.25) / 100)
    heure = int (pourcentage * 24) 
    minute = int(((pourcentage*24)- heure) * 60)
    seconde = (((((pourcentage*24)-heure) * 60) - minute) * 60) // 1



    return ("{}h {}m {}s".format(heure, minute, seconde))


if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))