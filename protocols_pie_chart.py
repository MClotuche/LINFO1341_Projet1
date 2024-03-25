import sys
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    """"
    #Capture wifi open non filtrée
    protocol_occurences = {
        'TCP':  731,
        'DNS': 264,
        'HTTP2': 229,
        'TLSv1.3':  121,
        'QUIC': 45,
        'TLSv1.2':  39,
        'HTTP2/JSON': 27,
        'HTTP3':  17,
        'HTTP':  11,
        'UDP': 7,
        'WebSocket': 5,
        'SSDP': 4,
        'HTTP/JSON': 1,
    }
    """
    #Capture filtrée
    protocol_occurences = {
            'HTTP:':  11,
            'TLSv1.3':  93,
            'TLSv1.2':  32,
            'TCP':  576,
            'HTTP2': 120,
            'HTTP2/JSON': 27,
            'HTTP/JSON': 1,
            'WebSocket': 5,
    }
    
    
    #Create a 'others' category for protocols that occur less than 45 times 
    others = 0
    for protocol in protocol_occurences:
        if protocol_occurences[protocol] < 28:
            others += protocol_occurences[protocol]
    protocol_occurences['others'] = others

    #create a new dictionary with the protocols that occur more than 45 times
    protocol_occurences = {protocol: occurences for protocol, occurences in protocol_occurences.items() if occurences > 28}
    #Create the pie chart
    
    tot_number = sum(protocol_occurences.values())

    fig, ax = plt.subplots()
    ax.pie(protocol_occurences.values(), labels=protocol_occurences.keys(),
        # show percentage with two decimal points
        autopct='%1.2f%%',
        # increase the size of all text elements
        textprops={'fontsize':14},
        colors=sns.color_palette('Paired')
           )
    ax.axis('equal')
    plt.savefig('Mhome_captures/graphs/wifi_open_filtered.pdf')
    plt.show()


if __name__ == "__main__":
    main()
