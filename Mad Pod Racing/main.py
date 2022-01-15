import sys
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
import math

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    elif next_checkpoint_angle < 8 and next_checkpoint_dist > 4000:
        thrust = 'BOOST'
    else:
        thrust = 100
    print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
