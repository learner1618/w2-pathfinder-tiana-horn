from PIL import Image


class Read:
    """First read the elevation file
    Then turn the file into a list"""




class Map:
    """
    Turn each number is elevation list into coordinates with a color for each coordinate
    Then transform those color coordinates to grayscale
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def save(self, filename):
        self.image.save(filename)

    def draw_point(self, coords, color):
        self.image.putpixel(coords, color)

    def map_from_file(self,filename):
        elevation_map = [[]]
        elevation_test = [[]]
        with open("elevation_small.txt") as data:
            for line in data.readlines():
                elevation_map.append(line) 
                for y, row in enumerate(elevation_map):
                    for x, num in enumerate(row):
                        elevation_test = image.putpixel((x,y), (num, num, num))
                        map.save("elevation.png")
                        open "elevation.png"

class Chart:
    """first, find the lowest coordinate on the left. 
    Then find the coordinates to the right that are touching. 
    Then find the coordinate with the smallest absolute value.""" 

                       
                # elevation_test.append([num])
             

        # print(elevation.png)

# class Grayscale:
#     def__init__(self, highest, lowest):

#     for y, row in enumerate(data):
# 	    for x, num in enumerate(row):
# 		   


# class Best_Path:
#     pass
    


# if __name__=="__main__":

#     print(Map(90,90))

    # print(Map(map_from_file("elevation_small.txt")))  
    # map = Map(90,90)
    # map.save("elevation.png")
