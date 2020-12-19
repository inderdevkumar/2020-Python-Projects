class Card:
    '''
    Represents the card in a deck of cards
    The rank is an integers and the suit is a string
    Suit will be H, D, S, C
    
    The beauty of OOP (encaps) is that we can enforce this
    '''
    def __init__(self, rank, suit):
        # We can enforce rules here, but we can skip
        # But if you want extra practice be my guest!!! :)
        if rank < 0 or rank > 13:
            print("Must be between 0 and 13")
            raise ValueError
            
        if not suit in ['S', 'H', 'D', 'C']:
            print("Must be S H D C")
            raise ValueError
            
        self._rank = rank
        self._suit = suit
        
        
    def get_suit(self):
        return self._suit
    
    def get_rank(self):
        return self._rank
    
    def __str__(self):
        return str(self._rank) + " : " + self._suit
    
    def __gt__(self, card):
        return self._rank > card.get_rank()


