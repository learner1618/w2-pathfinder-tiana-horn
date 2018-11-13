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
 
            for y, row in enumerate(self.matrix): 

                for x, num in enumerate(row):
                    for i in range(500):
                        cand = abs(((self.matrix[x][i])-(self.matrix[x][i+1])))
                        print(cand)
                        # if abs(((self.matrix[x][i])-(self.matrix[x][i+1]))) < abs(((self.matrix[x][i])-(self.matrix[x][i+1]))):
                        #     # print(self.matrix[x][i])
                        #     print("It's lit")
                    # while y < 500:
                    #     curr_y = y
              
               
                    #     candidates = [min(n) for n in ([((self.matrix[curr_y - 1])), ((self.matrix[curr_y])), ((self.matrix[curr_y + 1]))])]
                    #     new_y = min(candidates)
                    #     print(new_y)

                # while new_y < 500:
                #     self.image.putpixel((x, new_y), (0, 0, 255))
            return self
                # print(new_y)    

        # return self
        # curr_y = 70
        # for y, row in enumerate(self.matrix): 
        #     while curr_y < 500:
        #         # new_y = curr_y + 1
        #         # print(new_y)
        #     for x, num in enumerate(row):
        #         curr_pos(x,)
      
        #         self.image.putpixel((x, new_y), (0, 0, 255))
        # return self
            
            # candidates = [(x+1,y), (x+1,y+1), (x+1,y-1)]
            # for i in candidates:
            #     next_move = min(n) for n in [abs(((x,y) - (x+1,y))), abs(((x,y) - (x+1,y))), abs(((x,y) - (x+1,y)))]
            # curr_pos = data[x][y]
            # candidates = 
            
            # for y, row in enumerate(self.matrix): 
            #     for x, num in enumerate(row):
            #         while (x,y) < (599, 599): 
            #             curr_y = y 
            #             next_move = (((x,curr_y))), (( (x,curr_y+1))), (( (x,curr_y-1)))
            #             # self.image.putpixel((x, y+1), (0, 0, 255))
            #             print(next_move)

            
                
            
# once have candidates, iterate through values to calculate difference, record the index
# class Chart:
#     """first, find the lowest coordinate on the left. 
#     Then find the coordinates to the right that are touching. 
#     Then find the coordinate with the smallest absolute value.""" 


# class Grayscale:

# 		   


# class Best_Path:
#     pass


#________________________________
#       print(self.matrix[x][y])


                #    for i in range(500):
                #         print(self.matrix[x][i])
# 
#  #         curr_y += 1
        #         for x, num in enumerate(row):
        #             curr_pos = (x, curr_y)
        #     self.image.putpixel((curr_pos), (0, 0, 255))
                

                # candidates = [(x + 1, abs(curr_y - 1)), (x + 1, abs(curr_y)), (x + 1, abs(curr_y + 1))]
                # print((x,y), candidates, candidates.index(new_y))
    
        # for i in len(self.matrix):
        #     i += 1 
        #     print(i)
        
        # data[x][y]


if __name__=="__main__":
    
    my_map = Map(600,600) 
    my_map = my_map.map_from_file("elevation_small.txt")
    my_map.find_path()
    my_map.save("elevation.png")
    my_map.image.show("elevation.png")
