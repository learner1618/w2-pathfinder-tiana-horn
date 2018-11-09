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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height))
       
        with open("elevation_small.txt") as data:
            self.matrix = [[int(x) for x in line.split()] for line in data]        




    def save(self, filename):
        self.image.save(filename)
        
    def draw_point(self, coords, color):
        self.image.putpixel(coords, color)


    def map_from_file(self,filename):
            for y, row in enumerate(self.matrix): 
                for x, num in enumerate(row):
                    self.image.putpixel((x,y), (255, 0, 0))
            return self

    # def find_highest_elevation(self,): 
    #     map_from_file()
    #     max_point = max(matrix)
    # def map_from_file(self, filename):
        
            
                    # map.save("elevation.png")

    # def read_file():
    #     with open("elevation_small.txt") as data:
    #         for line in data:
    #              Matrix = [int(num) for num in line.split()]
                       

# class Chart:
#     """first, find the lowest coordinate on the left. 
#     Then find the coordinates to the right that are touching. 
#     Then find the coordinate with the smallest absolute value.""" 

                       
                # elevation_test.append([num])
             

        # print(elevation.png)

# class Grayscale:
#     def__init__(self, highest, lowest):

#     for y, row in enumerate(data):
# 	    for x, num in enumerate(row):
# 		   


# class Best_Path:
#     pass
    



if __name__=="__main__":

    # print(Map(600,600))
    my_map = Map(600,600) 
    my_map = my_map.map_from_file("elevation_small.txt")
    # map = map.draw_point()
    # breakpoint()
    my_map.save("elevation.png")
    my_map.image.show("elevation.png")




# -----------
# stuff that probably isn't right but I don't want to delete
# for line in data.readlines():
            # elevation_map.append(Matrix)
    #     elevation_map.append(line)
    #     w = len(line)
    #     h = len(line)
    # for i in elevation_map:
    #     Matrix = [[i for x in range(w)] for y in range(h)]
    #     print(Matrix)
        # Matrix.image.putpixel(x,y)(255, 0, 0)
       # print(Matrix)
    #    print(elevation_map[5:])
