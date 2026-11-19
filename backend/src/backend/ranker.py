import random
from .scoring import score_game


def rank_games(games, context):
    
    
    scored =[( game, score_game(game, context)) for game in games]
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return scored

def top_n(games, context, n=5):
    return rank_games(games, context)[:n]

def pick_recommendation(games, context, pool_size=10, seed=None):
    
    pool = rank_games(games, context)[:pool_size]
    candidates, scores = zip(*pool)
    rng = random.Random(seed)
    return rng.choices(candidates, weights=scores, k=1)[0]
    
    
