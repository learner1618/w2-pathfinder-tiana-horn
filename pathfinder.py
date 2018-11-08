from PIL import Image



class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def save(self, filename):
        self.img.save(filename)

    def draw_point(coords, color):
        self.img.putpixel(coords, color)

    def map_from_file(filename):
        lowest_elevation = []
        highest_elevation = [] 
        with open("elevation_small.txt") as elevation_file:
            line = elevation_file.readline().strip()
            elevation = line.split(" ")
            for num in elevation:
                if num is min:
                    lowest_elevation.append(num)
                    
            print(elevation)

if __name__=="__main__":

# print(map_from_file("elevation_small.txt"))

# print(Map(map_from_file("elevation_small.txt")))  
     map = Map(90,90)
     map.save("elevation.png")
