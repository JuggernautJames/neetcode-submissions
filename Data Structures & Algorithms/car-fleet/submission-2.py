class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleetstimes = [0] * len(speed)
        for i in range(len(speed)):
            cars.append((position[i], speed[i]))
        cars.sort()
        for i in range(len(cars)):
            pos, speed = cars[i]
            fleetstimes[i] = (target - pos) / speed
        index = len(fleetstimes) - 1
        while True:
            if index < 1: break
            if (fleetstimes[index] - fleetstimes[index-1] >= 0):
                fleetstimes.pop(index-1)
            index -= 1
        return len(fleetstimes)


