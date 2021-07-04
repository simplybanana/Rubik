import random


class Rubik(object):
    def __init__(self):
        """
               0: Red
               1: Orange
               2: White
               3: Yellow
               4: Blue
               5: Green
               """
        self.faces = {}
        self.faces["F"] = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
        self.faces["B"] = [1, 1, 1,
                           1, 1, 1,
                           1, 1, 1]
        self.faces["L"] = [2, 2, 2,
                           2, 2, 2,
                           2, 2, 2]
        self.faces["R"] = [3, 3, 3,
                           3, 3, 3,
                           3, 3, 3]
        self.faces["U"] = [4, 4, 4,
                           4, 4, 4,
                           4, 4, 4]
        self.faces["D"] = [5, 5, 5,
                           5, 5, 5,
                           5, 5, 5]
        self.done = self.faces

    def rotate_face(self,face,rotations):
        if rotations == 1:
            self.faces[face] = self.faces[face][-3::-3] + self.faces[face][-2::-3] + self.faces[face][::-3]
        elif rotations == -1:
            self.faces[face] = self.faces[face][2::3] + self.faces[face][1::3] + self.faces[face][::3]

    def moves(self, move):
        if move == "F":
            self.faces["L"][6:9], self.faces["U"][6:9], self.faces["R"][6:9], self.faces["D"][6:9] = self.faces["D"][6:9], self.faces["L"][6:9], self.faces["U"][6:9], self.faces["R"][6:9]
        elif move == "F'":
            self.faces["L"][6:9], self.faces["U"][6:9], self.faces["R"][6:9], self.faces["D"][6:9] = self.faces["U"][6:9], self.faces["R"][6:9], self.faces["D"][6:9], self.faces["L"][6:9]
        elif move == "B":
            self.faces["U"][:3], self.faces["L"][:3], self.faces["D"][:3], self.faces["R"][:3] = self.faces["R"][:3], self.faces["U"][:3], self.faces["L"][:3], self.faces["D"][:3]
        elif move == "B'":
            self.faces["U"][:3], self.faces["L"][:3], self.faces["D"][:3], self.faces["R"][:3] = self.faces["L"][:3], self.faces["D"][:3], self.faces["R"][:3], self.faces["U"][:3]
        elif move == "L":
            self.faces["F"][::3], self.faces["U"][::3], self.faces["B"][::3], self.faces["D"][2::3] = self.faces["U"][::3], self.faces["B"][::3], self.faces["D"][::-3], self.faces["F"][-3::-3]
        elif move == "L'":
            self.faces["F"][::3], self.faces["U"][::3], self.faces["B"][::3], self.faces["D"][2::3] = self.faces["D"][::-3], self.faces["F"][::3], self.faces["U"][::3], self.faces["B"][-3::-3]
        elif move == "R":
            self.faces["F"][2::3], self.faces["U"][2::3], self.faces["B"][2::3], self.faces["D"][::3] = self.faces["D"][-3::-3], self.faces["F"][2::3], self.faces["U"][2::3], self.faces["B"][::-3]
        elif move == "R'":
            self.faces["F"][2::3], self.faces["U"][2::3], self.faces["B"][2::3], self.faces["D"][::3] = self.faces["U"][2::3], self.faces["B"][2::3],self.faces["D"][-3::-3], self.faces["F"][::-3]
        elif move == "U":
            self.faces["F"][:3], self.faces["L"][2::3], self.faces["B"][6:], self.faces["R"][::3] = self.faces["R"][-3::-3], self.faces["F"][:3], self.faces["L"][::-3], self.faces["B"][6:]
        elif move == "U'":
            self.faces["F"][:3], self.faces["L"][2::3], self.faces["B"][6:], self.faces["R"][::3] = self.faces["L"][2::3], self.faces["B"][-1:-4:-1], self.faces["R"][::3], self.faces["F"][2::-1]
        elif move == "D":
            self.faces["F"][6:], self.faces["R"][2::3], self.faces["B"][:3], self.faces["L"][::3] = self.faces["L"][::3], self.faces["F"][-1:-4:-1], self.faces["R"][2::3], self.faces["B"][2::-1]
        elif move == "D'":
            self.faces["F"][6:], self.faces["R"][2::3], self.faces["B"][:3], self.faces["L"][::3] = self.faces["R"][-1::-3], self.faces["B"][:3], self.faces["L"][-3::-3], self.faces["F"][6:]
        if "'" in move:
            self.rotate_face(move[0], -1)
        else:
            self.rotate_face(move, 1)


if __name__ == '__main__':
    cube = Rubik()
    print(cube.faces)