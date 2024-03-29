### Martin CLOTUCHE - Laura RAUW
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Ce répertoire contient les différents scripts, captures réseaux et résultats nécéssaires à l'analyse de l'application OneDrive de Microsoft. 

Le script le plus important est get_dns_tls infos. Il permet de récupérer les requêtes DNS, types et serveurs authoritatifs (disponibles dans le répertoire dns_recap), ainsi que les correspondances noms de domaines-ports-adresses (répertoire tls_recap) d'une capture réseau pcap. 

Les premières captures du projet sont disponibles dans le réperoire captures, mais les captures finales, utilisées comme références dans le rapport, sont disponibles dans le répertoire Mhome_captures/raw_chrome, principalement les mesures wifi (typiquement Mhome_captures/raw_chrome/wifi_open_chrome_capture.pcap)

raw_bg: captures des communications "parasites" du réseau

raw_chrome: captures de l'application onedrive web

keys: clé nécéssaire au déchiffrement des captures

filter_list: liste de filtres Wireshark utiles

graphs: graphiques consommation réseau et autres figures

videos: enregistrement live des captures



