import math

from pyclass.Position import Position
from pyclass.Sprite import Sprite


def RGB(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def getDistanceBetweenPoints(positionOne: Position, positionTwo: Position):
    return round((((positionOne.x - positionTwo.x) ** 2 + (positionOne.y - positionTwo.y) ** 2) ** .5), 2)


def getDistanceBetweenSprites(spriteOne: Sprite, spriteTwo: Sprite):
    return round(((spriteOne.getX() - spriteTwo.getX()) ** 2 + (spriteOne.getY() - spriteTwo.getY()) ** 2) ** .5, 2)


def getAngleBetweenPoints(positionOne: Position, positionTwo: Position):
    return round(math.degrees(math.atan2(positionTwo.y - positionOne.y, positionTwo.x - positionOne.x)), 2)


def getAngleBetweenSprites(spriteOne: Sprite, spriteTwo: Sprite):
    return round(math.degrees(math.atan2(spriteTwo.getY() - spriteOne.getY(), spriteTwo.getX() - spriteOne.getX())), 2)


def polarOffsetBy(positionOne: Position, dist: float, angle: float):
    angle %= 360
    return Position(positionOne.x + dist * math.cos(math.radians(angle)), positionOne.y + dist * math.sin(math.radians(angle)))


def rotateBy(center: Position, angle: float, points):
    if points:
        for index in range(len(points)):
            distanceBetweenPoints = getDistanceBetweenPoints(center, points[index])
            angleBetweenPoints = getAngleBetweenPoints(center, points[index])
            points[index] = polarOffsetBy(center, distanceBetweenPoints, angle + angleBetweenPoints)
    return points


def polarOffsetBy2(pointOne, dist: float, angle: float):
    angle %= 360
    return pointOne[0] + dist * math.cos(math.radians(angle)), pointOne[1] + dist * math.sin(math.radians(angle))


def getDistanceBetweenPoints2(pointOne, pointTwo):
    return round(((pointOne[0] - pointTwo[0]) ** 2 + (pointOne[1] - pointTwo[1]) ** 2) ** .5, 2)


def getAngleBetweenPoints2(pointOne, pointTwo):
    return round(math.degrees(math.atan2(pointTwo[1] - pointOne[1], pointTwo[0] - pointOne[0])), 2)


def rotateBy2(center, angle: float, points):
    if points:
        for index in range(len(points)):
            distanceBetweenPoints = getDistanceBetweenPoints2(center, points[index])
            angleBetweenPoints = getAngleBetweenPoints2(center, points[index])
            points[index] = polarOffsetBy2(center, distanceBetweenPoints, angle + angleBetweenPoints)
    return points
