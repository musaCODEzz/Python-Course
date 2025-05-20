alien_1 = {'color': 'green', 'point':5}

print(alien_1['color'])
print(alien_1['point'])

new_points = alien_1['point']
print(f'You just earned {new_points} points!')

alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

alien_1['color'] = 'yellow'
print(f'The alien is now {alien_1["color"]}.')

print(alien_1)


alien_2 = {'x_position': 7, 'y_position': 25, 'speed': 'medium'}
print(f'The original speed of alien2 is {alien_2["speed"]}')

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 10
else:
    #fastest alien
    x_increment = 4

alien_2['x_position'] += x_increment
print(f"New position: {alien_2['x_position']}")
