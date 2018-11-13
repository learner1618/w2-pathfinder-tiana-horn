from PIL import Image
 


# class Read:
#     def read_file():
#         with open("elevation_small.txt") as data:
#             for line in data:
#                  Matrix = [int(num) for num in line.split()]
            
#                  print(Matrix)

# read_file()

# 



# class Read:
#     """First read the elevation file
#     Then turn the file into a list of lists"""
#     elevation_map = []
#     with open("elevation_small.txt") as data:
#             for line in data.readlines():
#                 elevation_map.append(line) 


class Map:
    """
    Turn each number is elevation list into coordinates with a color for each coordinate
    Then transform those color coordinates to grayscale
    """
    def __init__(self, width, height, highest_point):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height))
        self.highest_point = highest_point
       
        with open("elevation_small.txt") as data:
            self.matrix = [[int(x) for x in line.split()] for line in data]        

    def save(self, filename):
        self.image.save(filename)
        
    def draw_point(self, coords, color):
        self.image.putpixel(coords, color)

    def find_highest_elevation(self):
       self.highest_point = max([max(n) for n in self.matrix])
       return self.highest_point

    def map_from_file(self,filename):
            for y, row in enumerate(self.matrix): 
                for x, num in enumerate(row):
                    pos = int((num/self.highest_point)*255)
                    self.image.putpixel((x,y), (pos, pos, pos))
            return self

    # def find_highest_elevation(self,): 
    #     map_from_file()
    #     max_point = max(matrix)

# class Chart:
#     """first, find the lowest coordinate on the left. 
#     Then find the coordinates to the right that are touching. 
#     Then find the coordinate with the smallest absolute value.""" 


# class Grayscale:

# 		   


# class Best_Path:
#     pass
    

if __name__=="__main__":
    
    my_map = Map(600,600, 5648) 
    my_map = my_map.map_from_file("elevation_small.txt")
    my_map.find_highest_elevation()
    my_map.save("elevation.png")
    my_map.image.show("elevation.png")
