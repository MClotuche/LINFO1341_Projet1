import sys
import matplotlib.pyplot as plt


def main():
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


    #Create a 'others' category for protocols that occur less than 45 times 
    others = 0
    for protocol in protocol_occurences:
        if protocol_occurences[protocol] < 46:
            others += protocol_occurences[protocol]
    protocol_occurences['others'] = others

    #create a new dictionary with the protocols that occur more than 45 times
    protocol_occurences = {protocol: occurences for protocol, occurences in protocol_occurences.items() if occurences > 44}
    #Create the pie chart
    tot_number = sum(protocol_occurences.values())

    fig, ax = plt.subplots()
    ax.pie(protocol_occurences.values(), labels=protocol_occurences.keys(), autopct='%1.1f%%')
    ax.axis('equal')
    plt.savefig('Mhome_captures/graphs/wifi_open.pdf')
    plt.show()


if __name__ == "__main__":
    main()
