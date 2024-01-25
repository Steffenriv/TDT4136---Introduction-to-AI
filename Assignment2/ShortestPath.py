import math

import numpy as np
import pandas as pd

from queue import PriorityQueue 

from Map import Map_Obj

class ShortestPath():
    
    def __init__(self, task: int):
        #Initialize map and get start and goal position
        self.samfundet = Map_Obj(task)
        self.samfundet.fill_critical_positions(task)
        
        self.startpos = self.samfundet.get_start_pos()
        self.goalpos = self.samfundet.get_goal_pos() 
        
        #Run search algorithm
        self.search()
        #Show map
        self.samfundet.show_map()
        self.samfundet.int_map.shape
        
    def search(self):
        # came_from, cost_so_far = self.a_star_search(tuple(self.startpos), tuple(self.goalpos))
        self.a_star_search(tuple(self.startpos), tuple(self.goalpos))
        
        # for pos in came_from:
        #     self.samfundet.set_cell_value(pos,2)
            
        # print("came from:",came_from)
        # print("---------")
        # print("cost:",cost_so_far)
        
    def neighbors(self, pos : tuple):
        neighborList = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
        print("Neighbor list:",neighborList)
        
        for neighbor in neighborList:
            ##if(neighbors[0] < 0 or neighbors[1] < 0):
            #    print(neighbors)
            ##    neighborList.remove(neighbors) 
            ##print("Neighbor values:")
            #print(neighbors[0],neighbors[1])
            #print("------------------")
            if self.samfundet.get_cell_value(neighbor) == -1:
                neighborList.remove(neighbor)
                print("Neighbor values:")
                print(neighbor[0],neighbor[1])
                
        print("Updated Neighbor list:",neighborList)
        return neighborList
    
    def heuristic(self, a: tuple, b: tuple) -> float:
        # (x1, y1) = a
        # (x2, y2) = b
        # return abs(x1 - x2) + abs(y1 - y2)
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star_search(self, start: tuple, goal: tuple):
        frontier = PriorityQueue()
        print("Start:",start)
        print("---------")
        print("Goal:",goal)
        print("--------")
        frontier.put((0, start))
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0


        while not frontier.empty():
        #for i in range(2000):
            current = tuple(frontier.get()[1])
            print("current:",current)
            print("---------")
            if current == goal:
                print("Goal reached")
                break
            
            for next in self.neighbors(current):
                print("nextneighbor:",next)
                new_cost = cost_so_far[current] + self.samfundet.get_cell_value(current)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next, goal)
                    print("heuristic:", self.heuristic(next, goal))
                    frontier.put((priority, next))
                    came_from[next] = current
        # return came_from, cost_so_far

#Run
def run(): 
    #print("Which task do you want to run? (1-3)")
    #taskNr = int(input())
    #ShortestPath(taskNr)
    ShortestPath(1)

if __name__ == "__main__":
    run()