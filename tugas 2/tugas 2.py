import collections

KamenRiderCard = collections.namedtuple('KamenRiderCard', ['Type', 'KamenRider'])

class RiderDeck:
    type = 'Transformation Final_Attack Final_Form'.split()
    rider = 'Kuuga Agito Ryuki Faiz Blade Hibiki Kabuto Den-O Kiva Decade Double Oz Fourze Wizard Gaim Drive Ghost Ex-Aid Build Zi-O'.split()

    def __init__(self):
        self._cards = [KamenRiderCard(Type, KamenRider) for KamenRider in self.rider
                                         for Type in self.type]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
print(RiderDeck()[3])