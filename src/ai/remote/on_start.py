from ...core.game_agent import GameMatch

def on_start(game, data):

    if data['game'] in game.matches:
        game.matches[data['game']].add(data['player'])
    else:
        game.matches[data['game']] = GameMatch(
            data['player'],
            data['grid'],
            data['timelimit']
        )
