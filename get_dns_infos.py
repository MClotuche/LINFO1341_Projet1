import sys
import pyshark

def extract_dns_packets(pcap_file):
    dns_packets = []

    # Ouvrir le fichier pcap
    capture = pyshark.FileCapture(pcap_file)

    # Itérer sur tous les paquets
    for packet in capture:
        # Vérifier si le paquet est de type DNS
        if 'DNS' in packet:
            # Ajouter le paquet DNS à la liste
            dns_packets.append(packet)

    # Fermer le fichier pcap
    capture.close()

    return dns_packets

def main():
    # Vérifier si un fichier pcap est fourni en argument
    if len(sys.argv) != 2:
        print("Usage: python script.py fichier.pcap")
        sys.exit(1)

    # Récupérer le nom du fichier pcap à partir des arguments de la ligne de commande
    pcap_file = sys.argv[1]

    # Extraire les paquets DNS du fichier pcap
    dns_packets = extract_dns_packets(pcap_file)

    #Liste des infos acessibles dans un paquet: ici une réponse
    #print(dns_packets[-1])


    dns_occurences = {}
    for packet in dns_packets:
        if packet.dns.qry_name in dns_occurences:
            dns_occurences[packet.dns.qry_name] += 1
        else:
            dns_occurences[packet.dns.qry_name] = 1

    
    #TODO: Si le dns est une réponse, obtenir son name server responsable

    #print le nombre de paquets DNS
    print("Nombre de paquets DNS:", len(dns_packets))

    #print le dictionsnaire dns_occurences, avec un \n entre chaque paire clé:valeur
    print("\n".join([f"{key}: {value}" for key, value in dns_occurences.items()]))

if __name__ == "__main__":
    main()
