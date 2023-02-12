class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player = 0
        trainer = 0 
        match = 0
        while player < len(players) and trainer < len(trainers):
            if players[player] > trainers[trainer]:
                trainer += 1

            else:
                trainer += 1
                player += 1
                match += 1

        return match
