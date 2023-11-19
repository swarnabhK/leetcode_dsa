def largestAltitude(gain):
    altitudes = [0]
    for i in range(len(gain)):
        altitudes.append(gain[i]+altitudes[-1])
    return max(altitudes)

print(largestAltitude([-5,1,5,0,-7]))