from vehicle import Vehicle

GOAL_VEHICLE = Vehicle('X', 4, 2, 'H')

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles):
        """Create a new Rush Hour board.
        
        Arguments:
            vehicles: either a set of Vehicle objects or a dictionary of
                      mappings from id to Vehicle objects.

        Exceptions:
            TypeError: on improper type of vehicles param
            ValueError: on multiple vehicles having same id
        """
        if type(vehicles) == set:
            self.vehicles = vehicles
            self.vehicle_map = {vehicle.id : vehicle for vehicle in vehicles}
        elif type(vehicles) == dict:
            self.vehicle_map = vehicles
            self.vehicles = set(vehicles.values())
        else:
            raise TypeError('vehicles must be either list or dict')

        if len(self.vehicles) != len(self.vehicle_map.keys()):
            raise ValueError('Multiple vehicles with same id.')

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.vehicles == other.vehicles

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        s = '-' * 8 + '\n'
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        s += '-' * 8 + '\n'
        return s

    def get_board(self):
        """Representation of the Rush Hour board as a 2D list of strings"""
        board = [[' ' for i in range(6)] for j in range(6)]
        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = vehicle.id
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = vehicle.id
        return board

    def solved(self):
        """Returns true if the board is in a solved state."""
        return GOAL_VEHICLE in self.vehicles

    def moves(self):
        """Return iterator of next possible moves."""
        board = self.get_board()
        for v in self.vehicles:
            if v.orientation == 'H':
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == ' ':
                    new_v = Vehicle(v.id, v.x - 1, v.y, v.orientation)
                    new_vehicle_map = self.vehicle_map.copy()
                    new_vehicle_map[v.id] = new_v
                    yield RushHour(new_vehicle_map)
                if v.x + v.length <= 5 and board[v.y][v.x + v.length] == ' ':
                    new_v = Vehicle(v.id, v.x + v.length, v.y, v.orientation)
                    new_vehicle_map = self.vehicle_map.copy()
                    new_vehicle_map[v.id] = new_v
                    yield RushHour(new_vehicle_map)
            else:
                if v.y - 1 >= 0 and board[v.y - 1][v.x] == ' ':
                    new_v = Vehicle(v.id, v.x, v.y - 1, v.orientation)
                    new_vehicle_map = self.vehicle_map.copy()
                    new_vehicle_map[vehicle.id] = new_v
                    yield RushHour(new_vehicle_map)
                if v.y + v.length <= 5 and board[v.y + v.length][v.x] == ' ':
                    new_v = Vehicle(v.id, v.x, v.y + v.length, v.orientation)
                    new_vehicle_map = self.vehicle_map.copy()
                    new_vehicle_map[vehicle.id] = new_v
                    yield RushHour(new_vehicle_map)
