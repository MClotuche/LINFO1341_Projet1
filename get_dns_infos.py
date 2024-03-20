import sys
import pyshark
from collections import namedtuple

dns_query_types = {
    1: 'A',             # IPv4 address
    2: 'NS',            # Name server
    5: 'CNAME',         # Canonical name for an alias
    6: 'SOA',           # Start of a zone of authority
    12: 'PTR',          # Pointer to a canonical name
    15: 'MX',           # Mail exchange
    16: 'TXT',          # Text strings
    28: 'AAAA',         # IPv6 address
    33: 'SRV',          # Service locator
    252: 'AXFR',        # Request for a transfer of an entire zone
    255: 'ANY',         # Request for all records
    28: 'AAAA',         # IPv6 address
    39: 'DNAME',        # Delegation name
    41: 'OPT',          # Option
    43: 'DS',           # Delegation signer
    46: 'RRSIG',        # Resource record signature
    47: 'NSEC',         # Next secure
    48: 'DNSKEY',       # DNSSEC key
    59: 'CDS',          # Child DS
    60: 'CDNSKEY',      # Child DNSKEY
    61: 'DLV',          # DNSSEC lookaside validation
    65: 'HTTPS',        # HTTPS
    80: 'HTTP'          # HTTP
}


def extract_dns_packets(pcap_file):

    dns_dataset = {}
    Dns_entry = namedtuple('dn', ['ns','ty']) #additionnal records neglected
    
    # Ouvrir le fichier pcap
    capture = pyshark.FileCapture(pcap_file)
    # Itérer sur tous les paquets
    for packet in capture:
        # Vérifier si le paquet est de type DNS
        if 'DNS' in packet:
            try:
                name_server = packet.dns.soa_mname
            except:
                name_server = None
            
            # Check si déjà dans le dataset
            if packet.dns.qry_name in dns_dataset:
                #ajoute uniqment les secondes du temps
                
                dns_dataset[packet.dns.qry_name].append(Dns_entry(name_server, dns_query_types[int(packet.dns.qry_type)]))
            else: #ajout
                dns_dataset[packet.dns.qry_name] = [Dns_entry(name_server, dns_query_types[int(packet.dns.qry_type)])]

    # Fermer le fichier pcap
    capture.close()

    return dns_dataset

def main():
    # Vérifier si un fichier pcap est fourni en argument
    if len(sys.argv) != 2:
        print("Usage: python script.py fichier.pcap")
        sys.exit(1)

    # Récupérer le nom du fichier pcap à partir des arguments de la ligne de commande
    pcap_file = sys.argv[1]
    #récupère le nom du fichier, sans le chemin relatif
    csv_name = pcap_file.split('/')[-1]

    # Extraire les paquets DNS du fichier pcap
    dns_packets = extract_dns_packets(pcap_file)

    #Parcourt le dictionnaire dns_packets
    #Pour chaque élement de la liste, ajoute une nouvelle ligne dans un fichier excel
    #avec le nom du serveur responsable et le type de requête DNS
    with open('dns_recap/'+str(csv_name)+'.csv', 'w') as file:
        file.write("DNS Request,Name Server,Query Type\n")
        for dns_request, dns_entries in dns_packets.items():
            for entry in dns_entries:
                file.write(f"{dns_request},{entry.ns},{entry.ty}\n")

    #Liste des infos acessibles dans un paquet: ici une réponse
    #Récup serveur responsable: dns.resp_name
    """
    for attr in dir(dns_packets[20].dns):
        print(attr, getattr(dns_packets[20].dns, attr))
    print(dns_packets[20].dns)#.qry_type)


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
    #print("\n".join([f"{key}: {value}" for key, value in dns_occurences.items()]))
    """
if __name__ == "__main__":
    main()
