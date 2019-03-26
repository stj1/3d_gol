import random


data_frame = []
coords = []
cube_initial_state = []
cube_computed_state = []


class Point(object):

    def __init__(self, coord, status=False, gen=0):
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]
        self.z = coord[2]
        self.status = status
        self.gen = gen

    def initialize_cube(n):
        """Create cube data frame -- level --> row --> points."""
        # 1 - create levels
        for level in range(n):
            data_frame.append([])
        # 2 - create rows
        for level in data_frame:
            while len(level) < n:
                level.append([])
        # 3 - create points
        for level in data_frame:
            for row in level:
                while len(row) < n:
                    row.append([])
        # create points coordinates
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    coords.append((x, y, z))
        # move points to data frame
        n = 0
        for level in data_frame:
            for row in level:
                for point in row:
                    point.append(
                        Point(coords[n], random.choice([True, False])))
                    n += 1
        global cube_initial_state
        cube_initial_state = data_frame
        global cube_computed_state
        cube_computed_state = data_frame

    def test_cube(cube_initial_state):
        for level in cube_initial_state:
            for row in level:
                for point in row:
                    point_xyz = point[0].coord
                    point_score = 0
                    # TODO
                    # test floor
                    print(point_xyz)

                    # test curent
                    # test celling
                    # if point_xyz[]


# print(list(range(10))[2:4]) TODO
Point.initialize_cube(3)
# print(cube_initial_state)
# Point.test_cube(cube_initial_state)


# cube_initial_state[x][y][z][unpack]
print(cube_initial_state[0][0][0][0].coord)

# create list for dead and alive points
