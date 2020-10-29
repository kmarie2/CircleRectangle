"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        centerX,centerY,radius,xmin,xmax,ymin,ymax
        
some examples:

# An obvious overlap:
>>> circleRectangleOverlap(100,20,8, 80,120, 18,25)
True


# An obvious miss:
>>> circleRectangleOverlap(100,20,8, 180,220, 18,25)
False


(Note we can't have a circle with negative radius)

>>> circleRectangleOverlap(6,6,3, 3,6, 9,9)
True


>>> circleRectangleOverlap(10,15,8.5, 2,4, 1,5)
False


>>> circleRectangleOverlap(9,6,3, 0,5, 7,9)
False


>>> circleRectangleOverlap(13,13,6.5, 7,10, 12,13)
True


>>> circleRectangleOverlap(20,15,10, 5,8, 10,15)
False


>>> circleRectangleOverlap(6,6,2, 3,9, 5,6)
True


>>> circleRectangleOverlap(4,5,2, 5,10, 3,7)
True


>>> circleRectangleOverlap(11,9,3.5, 7,15, 7,15)
True

>>> circleRectangleOverlap(11,9,3.5, 7,15, 14,15)
False

>>> circleRectangleOverlap(11,10,3.5, 7,15, 5,7)
True


>>> circleRectangleOverlap(4,6,1.5, 0,3, 6,10)
True


>>> circleRectangleOverlap(3,1,5, 0,2, 1,4)
True

# Keeton and I generate these last three problems together to see if they would break my algorithm
# and fortunately, they don't!

>>> circleRectangleOverlap(320,188,9.219544457292887, 75,285, 178,218 )
False

>>> circleRectangleOverlap(228,255,34.655446902326915, 129,373, 81,165 )
False

>>> circleRectangleOverlap(268,113,36.71511950137164, 145,425, 199,256)
False

"""

from math import *
from Logic import *
  
  
def circleRectangleOverlap(centerX: float,centerY: float,radius: float,xmin: float,xmax: float,ymin: float,ymax: float) -> bool:
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes...
    MODE:str = 'mine'

    if MODE=='mine':
        distance_corner1: float = ((ymax - centerY) ** 2 + (xmin - centerX) ** 2) ** 0.5
        distance_corner2: float = ((ymin - centerY) ** 2 + (xmin - centerX) ** 2) ** 0.5
        distance_corner3: float = ((ymin - centerY) ** 2 + (xmax - centerX) ** 2) ** 0.5
        distance_corner4: float = ((ymax - centerY) ** 2 + (xmax - centerX) ** 2) ** 0.5
        distanceCYBeyond: float = centerY - ymax
        distanceCXBeyond: float = centerX - xmax
        distanceCYBelow: float = centerY - ymin
        distanceCXBelow: float = centerX - xmin
        # Check if any corner is in the circle
        if distance_corner1 <= radius and distance_corner2 <= radius and distance_corner3 <= radius and distance_corner4 <= radius:
            return True
        # Check if the center of the circle is inside the rectangle
        elif centerX > xmin and centerX < xmax and centerY > ymin and centerY < ymax:
            return True
        #now the side quadrants
        # side right
        elif distanceCYBelow >= 0 and distanceCYBeyond <= 0 and distanceCXBeyond >= 0:
            if radius >= distanceCXBeyond:
                return True
            else:
                return False
        #side left
        elif distanceCYBelow >= 0 and distanceCYBeyond <= 0 and distanceCXBelow <= 0:
            if radius >= abs(distanceCXBelow):
                return True
            else:
                return False
        #bottom side (Higher Y)
        elif distanceCXBelow >= 0 and distanceCXBeyond <= 0 and distanceCYBeyond >=0 :
            if radius >= distanceCYBeyond:
                return True
            else:
                return False
        #top side (Lower Y)
        elif distanceCXBelow >= 0  and distanceCXBeyond <= 0 and distanceCYBelow <= 0:
            if radius >= abs(distanceCYBelow):
                return True
            else:
                return False

        # if the circle and rectangle are far from each other and the radius is not overlapping with anything
        else:
            return False


    elif MODE=='code review':
        
        try:
            import circleRectangleToReview as review
        except:
            print("Your circleRectangleToReview.py file does not seem to be ready yet")
            return True
            
        return review.myCircleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
        
    elif MODE=='answer key':
        return keyCircleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
    elif MODE=='test samples':
        try:
            from CircleRectangleSamples import circleRectangleOverlapSamples
# the line below only works in the QuaCS lab computers
#           from sample_answers.cs105.Intersect.CircleRectangleSamples import circleRectangleOverlapSamples
            try:
                answer: bool = circleRectangleOverlapSamples(centerX,centerY,radius,xmin,xmax,ymin,ymax)
                return answer
            except:
                print("A sample solution had an error or failed a precondition.")
                print("This should have been caught by the lab files already, so please report it.")
                return True
        except:
            print("Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers")
            print(" If you are running this program on another computer, you'll have to wait to check")
            print(" your test suite against the sample answers when you're back in the lab.")
            print(" (Remember to Team->Commit on your computer and Team->Update in the lab.)")
    
            return True  # Well, sometimes this is the right answer!            
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception
        return True

def keyCircleRectangleOverlap(centerX: float, centerY: float, radius: float, xmin: float, xmax: float, ymin: float, ymax: float) -> bool:

    return True  # The key will be released later, above this line

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"))
    else:
        print("Rats!")

if __name__ == "__main__": _test()
