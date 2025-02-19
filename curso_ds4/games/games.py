class Sport:
    '''
    Clase para representar un deporte
    '''
    
    def __init__(self, name: str, players: int, league: str):
        self.name = name
        self.players = int(players)  # Convertir players a entero siempre
        self.league = league
    
    def __str__(self) -> str:
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self) -> str:
        """
        Representación en string de un Sport
        """
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self) -> dict:
        """
        Retorna el Sport en formato JSON
        """
        return {
            'name': self.name,
            'players': self.players,
            'league': self.league
        }
        
if __name__ == '__main__':
    a = Sport("Football", 11, "NFL")
    print(a)          # Imprime la representación de Sport con __str__()
    print(repr(a))    # Imprime la representación de Sport con __repr__()
    print(f"a: {id(a)}")
    
    b = repr(a)       # Guarda la representación del objeto
    print(b)
    b = eval(b)       # Evalúa la representación para reconstruir el objeto
    print(b)
    print(repr(a))
    print(f"b: {id(b)}")
