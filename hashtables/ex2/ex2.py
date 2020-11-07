#  Hint:  You may not need all of these.  Remove the unused functions.
from dataclasses import dataclass

@dataclass
class Ticket:
    source:str
    destination:str


def reconstruct_trip(tickets, length = None):
    """
    YOUR CODE HERE
    """
    # Your code here

    t_dict = {ticket.source: ticket.destination for ticket in tickets}
    route = []

    next_destination = t_dict["NONE"]

    while next_destination != "NONE":
        route.append(next_destination)
        next_destination = t_dict[next_destination]

    extra = length - len(route) 
    route.extend(["NONE"] * extra)
    return route


if __name__ == "__main__":
    tickets = [
        Ticket( source= "PIT", destination= "ORD"  ),
        Ticket( source= "XNA", destination= "CID"  ),
        Ticket( source= "SFO", destination= "BHM"  ),
        Ticket( source= "FLG", destination= "XNA"  ),
        Ticket( source= "NONE",destination= "LAX" ),
        Ticket( source= "LAX", destination= "SFO"  ),
        Ticket( source= "CID", destination= "SLC"  ),
        Ticket( source= "ORD", destination= "NONE" ),
        Ticket( source= "SLC", destination= "PIT"  ),
        Ticket( source= "BHM", destination= "FLG"  )
    ]

    print(reconstruct_trip(tickets, 15))