# simple reflex agent

import random

states = ['clean', 'dirty']
locations = ['A', 'B']

# state of the world
world = {
	'A': random.choice(states),
	'B': random.choice(states),
}

# rules mapping states to actions
rules = {
	'A': {
		'clean': 'B',
		'dirty': 'suck'
	},
	'B': {
		'clean': 'A',
		'dirty': 'suck'
	}
}

# initial percept
position = random.choice(locations)

def agent_function(percept, state, rules):
	pos = percept
	floor = state[pos]
	action = rules[pos][floor]
	return action

def clean(initial_percept, initial_state, rules, iterations):
	def perform_action(percept, state, rules, count):
		action = agent_function(percept, state, rules)
		if action == 'A' or action == 'B':
			percept = action
		else:
			state[percept] = 'clean'
		print (percept, state)
		count -= 1
		if count > 0:
			perform_action(percept, state, rules, count)

	perform_action(initial_percept, initial_state, rules, iterations)


if __name__ == '__main__':
	print ('Initial state')
	print (position, world)
	print ('And clean...')
	clean(position, world, rules, 4)