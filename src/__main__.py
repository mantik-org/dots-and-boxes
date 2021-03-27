from .core.game import Game

def main():
    Game.getInstance().run('localhost', 8080)

if __name__ == '__main__':
    main()