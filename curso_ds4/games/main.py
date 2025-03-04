import json
from athlete import Athlete
from sports import Sport
from team import Team
from game import Game

def main(archivo_torneo: str):
    ''' Función principal del juego '''
    if archivo_torneo:
        with open(archivo_torneo, "r", encoding='utf8') as f:
            torneo = json.load(f)
    else:
        players_mexico = ['Chicharito', 'Piojo', 'Chucky', 
                          'Tecatito', 'Gullit', 'Ochoa', 
                          'Guardado', 'Herrera', 'Layun', 
                          'Moreno', 'Araujo']
        players_espania = ['Casillas', 'Ramos', 'Pique', 
                           'Alba', 'Iniesta', 'Silva', 
                           'Isco', 'Busquets', 'Costa', 
                           'Morata', 'Asensio']
        players_brasil = ['Neymar', 'Coutinho', 'Marcelo',
                          'Casemiro', 'Alisson', 'Jesus',
                          'Paulinho', 'Thiago', 'Silva',
                          'Firmino', 'Danilo']
        players_argentina = ['Messi', 'Aguero', 'Di Maria',
                             'Mascherano', 'Higuain', 'Dybala',
                             'Otamendi', 'Romero', 'Rojo',
                             'Banega', 'Fazio']
        
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        lista_brasil = [Athlete(x) for x in players_brasil]
        lista_argentina = [Athlete(x) for x in players_argentina]  
        
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("España", soccer, lista_espania)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argentina)
        
        equipos = [mexico, espania, brasil, argentina]
        d = {}
        
        for i in range(len(equipos)):
            for j in range(i + 1, len(equipos)):  # Evita repetir enfrentamientos
                juego = Game(equipos[i], equipos[j])
                d[f"{equipos[i].name} vs {equipos[j].name}"] = juego.to_json()
                
        torneo = list(d.values())
        archivo_torneo = "torneo.json"
        
        with open(archivo_torneo, "w", encoding='utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        
        print(f"Se escribió el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], 
                 Sport(juego['A']['sport']['name'], 
                       juego['A']['sport']['players'],
                       juego['A']['sport']['league']), 
                [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'],
                 Sport(juego['B']['sport']['name'],
                       juego['B']['sport']['players'],
                       juego['B']['sport']['league']),
                [Athlete(x['name']) for x in juego['B']['players']])
        
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo = ""
    main(archivo)
