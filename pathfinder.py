from PIL import Image



class Map:
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
