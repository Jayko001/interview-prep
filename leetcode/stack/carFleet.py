class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetCount = 0
        time = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            t = (target - p) / s
            time.append(t)

        temp = 0
        for j in range(len(time)):
            if time[j] <= temp:
                continue
            else:
                temp = time[j]
                fleetCount += 1

        return fleetCount