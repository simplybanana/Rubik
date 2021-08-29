import random
import copy
from collections import deque


def inverse_move(move):
    if "'" in move:
        move = move[0]
    else:
        move += "'"
    return move


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
        self.done = copy.deepcopy(self.faces)
        self.move_list = ["F","F'","L","L'","R","R'","B","B'","D","D'","U","U'"]


    def bfs(self,start):
        if start == self.done:
            return []
        foward_parents = {start: None}
        backward_parents = {self.done: None}
        forward_moves = {}
        backward_moves = {}
        for move in self.move_list:
            forward_moves[move] = move
            backward_moves[inverse_move(move)] = move
        foward = (forward_moves,foward_parents,backward_parents)
        backward = (backward_moves,backward_parents,foward_parents)
        queue = deque([(start,foward),(self.done,backward),None])
        finished = False
        i = 0
        while not finished and queue:
            vertex = queue.popleft()
            if vertex is None:
                queue.append(None)
                continue
            position = vertex[0]
            moves, parents, other_parents = vertex[1]
            for move in moves:
                next_position = self.moves(move)
            visited = []
            
def rotate_face(faces,face,rotations):
    if rotations == 1:
        faces[face] = faces[face][-3::-3] + faces[face][-2::-3] + faces[face][::-3]
    elif rotations == -1:
        faces[face] = faces[face][2::3] + faces[face][1::3] + faces[face][::3]   
    return faces
    
def moves(faces, move):
    if move == "F":
        faces["L"][6:9], faces["U"][6:9], faces["R"][6:9], faces["D"][6:9] = faces["D"][6:9], faces["L"][6:9], faces["U"][6:9], faces["R"][6:9]
    elif move == "F'":
        faces["L"][6:9], faces["U"][6:9], faces["R"][6:9], faces["D"][6:9] = faces["U"][6:9], faces["R"][6:9], faces["D"][6:9], faces["L"][6:9]
    elif move == "B":
        faces["U"][:3], faces["L"][:3], faces["D"][:3], faces["R"][:3] = faces["R"][:3], faces["U"][:3], faces["L"][:3], faces["D"][:3]
    elif move == "B'":
        faces["U"][:3], faces["L"][:3], faces["D"][:3], faces["R"][:3] = faces["L"][:3], faces["D"][:3], faces["R"][:3], faces["U"][:3]
    elif move == "L":
        faces["F"][::3], faces["U"][::3], faces["B"][::3], faces["D"][2::3] = faces["U"][::3], faces["B"][::3], faces["D"][::-3], faces["F"][-3::-3]
    elif move == "L'":
        faces["F"][::3], faces["U"][::3], faces["B"][::3], faces["D"][2::3] = faces["D"][::-3], faces["F"][::3], faces["U"][::3], faces["B"][-3::-3]
    elif move == "R":
        faces["F"][2::3], faces["U"][2::3], faces["B"][2::3], faces["D"][::3] = faces["D"][-3::-3], faces["F"][2::3], faces["U"][2::3], faces["B"][::-3]
    elif move == "R'":
        faces["F"][2::3], faces["U"][2::3], faces["B"][2::3], faces["D"][::3] = faces["U"][2::3], faces["B"][2::3],faces["D"][-3::-3], faces["F"][::-3]
    elif move == "U":
        faces["F"][:3], faces["L"][2::3], faces["B"][6:], faces["R"][::3] = faces["R"][-3::-3], faces["F"][:3], faces["L"][::-3], faces["B"][6:]
    elif move == "U'":
        faces["F"][:3], faces["L"][2::3], faces["B"][6:], faces["R"][::3] = faces["L"][2::3], faces["B"][-1:-4:-1], faces["R"][::3], faces["F"][2::-1]
    elif move == "D":
        faces["F"][6:], faces["R"][2::3], faces["B"][:3], faces["L"][::3] = faces["L"][::3], faces["F"][-1:-4:-1], faces["R"][2::3], faces["B"][2::-1]
    elif move == "D'":
        faces["F"][6:], faces["R"][2::3], faces["B"][:3], faces["L"][::3] = faces["R"][-1::-3], faces["B"][:3], faces["L"][-3::-3], faces["F"][6:]
    if "'" in move:
        return rotate_face(faces, move[0], -1)
    else:
        return rotate_face(faces, move, 1)


if __name__ == '__main__':
    cube = Rubik()
