from ...core.game_agent import GameAgent

def on_start(game, data):

    if data['game'] in game.agents:
        game.agents[data['game']].add(data['player'])
    else:
        game.agents[data['game']] = GameAgent(
            data['player'],
            data['grid'],
            data['timelimit']
        )
