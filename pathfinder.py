from PIL import Image
 

# class Read:
#     """First read the elevation file
#     Then turn the file into a list of lists"""
#     elevation_map = []
#     with open("elevation_small.txt") as data:
#             for line in data.readlines():
#                 elevation_map.append(line) 


class Map:
    """
    Turn each number in elevation list into coordinates with a color for each coordinate
    Then transform those color coordinates to grayscale
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height))
        with open("elevation_small.txt") as data:
            self.matrix = [[int(x) for x in line.split()] for line in data] 
        self.maxelevation = max([max(n) for n in self.matrix])       

    def save(self, filename):
        self.image.save(filename)
        
    def draw_point(self, coords, color):
        self.image.putpixel(coords, color)

    def map_from_file(self,filename):
        for y, row in enumerate(self.matrix): 
            for x, num in enumerate(row):
                pos = int((num/self.maxelevation)*255)
                self.image.putpixel((x,y), (pos, pos, pos))
        return self

    def find_path(self):
        curr_x = 0
        curr_y = 77
        for y, row in enumerate(self.matrix): 
            for x, num in enumerate(row):
                self.image.putpixel((x,curr_y), (255, 0, 0))
        return self
            

# class Chart:
#     """first, find the lowest coordinate on the left. 
#     Then find the coordinates to the right that are touching. 
#     Then find the coordinate with the smallest absolute value.""" 


# class Grayscale:

# 		   


# class Best_Path:
#     pass
    

if __name__=="__main__":
    
    my_map = Map(600,600) 
    my_map = my_map.map_from_file("elevation_small.txt")
    my_map.find_path()
    my_map.save("elevation.png")
    my_map.image.show("elevation.png")
