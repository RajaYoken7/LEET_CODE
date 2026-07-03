class Solution(object):
    def largestAltitude(self, gain):
        currentAltitude = 0
        maxAltitude = 0
        for i in gain:
            currentAltitude += i
            if currentAltitude > maxAltitude:
                maxAltitude=currentAltitude
        return maxAltitude