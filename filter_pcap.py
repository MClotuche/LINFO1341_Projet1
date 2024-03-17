import pyshark
import sys
"""
Function to filter a pcap file (chrome capture)
based on a filter file (capture without chrome)
"""


def __main__():
    """
    #if -h argument, print how to use the script
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Usage: python filter_pcap.py <file.pcap> <filter_file.pcap>")
        sys.exit(0)
    
    #error if not 2 arguments
    if len(sys.argv) != 3:
        print("Usage: python filter_pcap.py <file.pcap> <filter_file.pcap>")
        sys.exit(1)
    """
    #get 1st argument as pcap file to filter, 2nd argument as filter
    filepath = sys.argv[1]
    #filterpath = sys.argv[2]
    #Load the pcap file
    pcap_fle = pyshark.FileCapture(filepath,include_raw=True, use_json=True)
    #pcap_filter = pyshark.FileCapture(filterpath)
    # Create the filter
    filter = ""
    paquets_info = {}

    for paquet in pcap_fle:
        print(dir(paquet))
        try:
            paquet_info = paquet.data
            paquets_info.append(paquet.info)
        except:
            continue
    
    for info in paquets_info:
        filter += "!(_ws.col.info == " + info + ") && "

    filter = filter[:-4]
    print(filter)
    
__main__()
