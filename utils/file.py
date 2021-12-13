from pathlib import Path
import os


class File:
    FILE = os.path.join(Path(__file__).resolve().parent.parent, 'resource', 'score')

    def __init__(self):
        pass

    @classmethod
    def load_data(cls):
        data = dict()
        with open(cls.FILE, 'r') as score_file:
            scores = score_file.readlines()
            for idx, score in enumerate(scores):
                if idx > 5:
                    break
                if '\n' in score:
                    score = score.strip('\n')
                player, player_score = score.split(':')
                data[player] = int(player_score)
        return data

    @classmethod
    def save_data(cls, new_score):
        data = cls.load_data()
        data[new_score['player']] = new_score['score']
        new_scores = sorted(data.items(), reverse=True, key=lambda item: item[1])
        with open(cls.FILE, 'w') as score_file:
            for idx, score in enumerate(new_scores):
                if idx < 5:
                    score_file.write(f"{score[0]}:{score[1]}\n")
