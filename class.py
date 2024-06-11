#https://exercism.org/tracks/python/exercises/high-scores
class HighScores:
    def __init__(self,scores):
        self.scores=scores
    def latest(self):
        length_list=len(self.scores)
        latest_score=self.scores[length_list-1]
        return latest_score
    def personal_top_three(self):
        new_list=sorted(self.scores)
        return sorted(new_list[-3:],reverse=True)
    def personal_best(self):
        max_score=0
        for score in self.scores:
            if (score>max_score):
                max_score=score
        return max_score
