#similar code with matplotlib to visualize clean rooms as green and dirty rooms as red and vacuum as blue cicle
import random
import matplotlib.pyplot as plt
import numpy as np
import time
class ReflexVacuumCleaner:
    def __init__(self):
        self.rooms=["A","B","C","D"]
        self.location=random.choice(self.rooms)
        self.environment={room:random.choice(['Clean','Dirty']) for room in self.rooms}
    def perceive(self):
        return self.environment[self.location]
    def act(self,status): 
        if status=='Dirty':
            print(f"Vacuum at {self.location} Dirty -> Cleaning...")
            self.environment[self.location]='Clean'
        else:
            old_location=self.location
            current_index=self.rooms.index(self.location)
            self.location=self.rooms[(current_index+1)%len(self.rooms)]
            print(f"Vacuum at {old_location} is Clean -> Moving to room {self.location}...")
    def is_done(self):
        return all(state =='Clean' for state in self.environment.values())
    def visualize(self):
        colors = {'Clean': 'green', 'Dirty': 'red'}
        room_colors = [colors[self.environment[room]] for room in self.rooms]
        plt.figure(figsize=(8, 2))
        plt.bar(self.rooms, [1]*len(self.rooms), color=room_colors)
        vacuum_index = self.rooms.index(self.location)
        plt.scatter(vacuum_index, 0.5, s=200, c='blue', label='Vacuum')
        plt.ylim(0, 1)
        plt.title('Vacuum Cleaner Environment')
        plt.legend()
        plt.show()
if __name__ == "__main__":
    vacuum=ReflexVacuumCleaner()
    print(f"Initial Environment: {vacuum.environment}")
    vacuum.visualize()
    while not vacuum.is_done():
        status=vacuum.perceive()
        vacuum.act(status)
        vacuum.visualize()
        time.sleep(1)