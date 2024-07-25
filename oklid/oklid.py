import math

points = [(1, 2), (5, 2), (5, 9)]

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

mindistance = min(distances)

print(f"Tüm nokta çiftleri arasindaki mesafeler: {distances}")
print(f"Minimum mesafe: {mindistance}")
