# simple reflex agent

# assume that the agent can only see whether floor is clean or dirty,
# not what room it's in

import random

# we randomize action when agent is in clean room
def get_rules():
	action_if_clean = random.choice(['left', 'right'])
	return {
		'clean': action_if_clean,
		'dirty': 'suck'
	}

def agent_function(percept, rules):
	action = rules[percept]
	return action

def clean(initial_position, rules, world, iterations):
	def perform_action(position, rules, world, count):
		percept = world[position]
		action = agent_function(percept, rules)
		if action == 'suck':
			world[position] = 'clean'
		elif action == 'left':
			position = 'A'
		else:
			position = 'B'
		print('Action:', action)
		print('Position:', position)
		print('World:', world)
		count -= 1
		if count > 0:
			perform_action(position, get_rules(), world, count)

	perform_action(initial_position, rules, world, iterations)


if __name__ == '__main__':

	states = ['clean', 'dirty']
	locations = ['A', 'B']

	# initial state of the world
	world = {
		'A': random.choice(states),
		'B': random.choice(states),
	}
	# initial position of cleaner
	initial_position = random.choice(locations)

	print('# Initial state')
	print('Position:', initial_position)
	print('World:', world)
	print ('# And clean...')
	clean(initial_position, get_rules(), world, 10)
