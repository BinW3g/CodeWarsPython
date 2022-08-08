# codewars challenge link
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

possible_ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]


class User:
    rank = -8
    progress = 0

    def inc_progress(self, challenge_rank):
        if challenge_rank not in possible_ranks:
            raise ValueError("para is not in range of possible ranks")
        if self.rank < 8:
            rank_dif = possible_ranks.index(challenge_rank) - possible_ranks.index(self.rank)
            if rank_dif == 0:
                self.progress += 3
            if rank_dif == -1:
                self.progress += 1
            if rank_dif > 0:
                self.progress += 10 * pow(rank_dif, 2)
            if self.progress >= 100:
                rank_ups = int(self.progress / 100)
                if possible_ranks.index(self.rank) + rank_ups > len(possible_ranks):
                    self.rank = 8
                else:
                    self.rank = possible_ranks[possible_ranks.index(self.rank) + rank_ups]
                self.progress = self.progress % 100
                if self.rank == 8:
                    self.progress = 0


if __name__ == '__main__':
    user = User()
    # user.progress = 20
    # user.rank = 1
    user.inc_progress(1)
    print(user.progress == 40)
    print(user.rank == -2)

    user = User()
    print(user.rank == -8)
    print(user.progress == 0)
    user.inc_progress(-7)
    print(user.progress == 10)
    user.inc_progress(-5)
    print(user.progress == 0)
    print(user.rank == -7)
