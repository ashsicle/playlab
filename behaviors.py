import math

class Behavior(object):
    def __init__(self, **parameters):
        self.parameters = parameters

    def setup(self, agent, otheragent, attraction, state):
        pass

    def apply(self, agent, state):
        pass

    def draw(self, agent, state):
        pass

                      
# move towards attractions
class MoveTowardsAttraction(Behavior):
    def setup(self, agent, otheragent, attraction, state):
        if 'closest_attraction' not in state:
            state['closest_attraction'] = None
        if 'distance_to_closest_attraction' not in state:
            state['distance_to_closest_attraction'] = 1000000

        for program in attraction:
            #print attraction
            distance_to_program = dist(
                program.position[0], program.position[1],
                agent.position[0], agent.position[1]
                )
    
            if distance_to_program < state['distance_to_closest_attraction']:
                state['distance_to_closest_attraction'] = distance_to_program
                state['closest_attraction'] = program
        
    def apply(self, agent, state):

        closest_attraction = state['closest_attraction']
        if closest_attraction is None:
            return

        distance_to_closest_attraction = state['distance_to_closest_attraction']
        if distance_to_closest_attraction < self.parameters['threshold'] and closest_attraction.position[1] < height-150:
            angle_to_closest_attraction = math.atan2(
                agent.position[1] - closest_attraction.position[1],
                agent.position[0] - closest_attraction.position[0]  
                )
            agent.turnrate += (angle_to_closest_attraction - agent.direction) / self.parameters['weight']
            agent.speed += self.parameters['speedfactor'] / distance_to_closest_attraction

    def draw(self, agent, state):
        #stroke(200)
        #noFill()
        closest = state['closest_attraction']
        distance_to_closest_attraction = state['distance_to_closest_attraction']

        
        if closest.position[1] < height-150:
            if distance_to_closest_attraction < self.parameters['threshold']:

                line(agent.position[0], agent.position[1], closest.position[0], closest.position[1])
                noStroke()
                fill(agent.agentColor,10)
                ellipse(closest.position[0], closest.position[1], self.parameters['threshold'] * 2, self.parameters['threshold'] *2)
    
    
class Swim(Behavior):
    def setup(self, agent, otheragent, attraction, state):
        #agent.speed = 
        agent.turnrate = 0

    def apply(self, agent, state):
        # Move forward, but not too fast.
        if agent.speed > self.parameters['speedlimit']:
            agent.speed = self.parameters['speedlimit']
        agent.position[0] -= math.cos(agent.direction) * agent.speed
        agent.position[1] -= math.sin(agent.direction) * agent.speed

        # Turn, but not too fast.
        if agent.turnrate > self.parameters['turnratelimit']:
            agent.turnrate = self.parameters['turnratelimit']
        if agent.turnrate < -self.parameters['turnratelimit']:
            agent.turnrate = -self.parameters['turnratelimit']
        agent.direction += agent.turnrate

        # Fix the angles.
        if agent.direction > math.pi:
            agent.direction -= 2 * math.pi
        if agent.direction < -math.pi:
            agent.direction += 2 * math.pi
        
