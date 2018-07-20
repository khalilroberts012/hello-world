# from __future__ import division
import random


count = 1

l = []

player_number = raw_input("How many players?:")
while (count <= int(player_number)):
    l.append(raw_input("Who is opponent " + str(count) + " ?:"))
    count = (count + 1)




# current_count = player_number
# count2 = (count/2)
# if (player_number == count):
#     for player_number(count = int(player_number)/2)
# while (str(player_number) = count2):

pairs = {}

while len(l) > 1:

    r1 = random.randrange(0, len(l))
    elem1 = l.pop(r1)

    r2 = random.randrange(0, len(l))
    elem2 = l.pop(r2)

    pairs[elem1] = elem2

i = 1

for key, value in pairs.items():
    print("Pair {}: {} and {}".format(i, key, value))
    i += 1


# player_number = players
#
# while (count <= int(player)):
#     l.pop(raw_input("Who lost?:" ))
#     count = (count + 1)
    # if (count <= raw_input()):
    #     l.pop(raw_input("who lost"))
# current_count = count
# while(current_count):
#     current_count = count in l
#     for current_count in l:
#         print "its workin"
#         l.pop(raw_input("who lost?: "))
# if current_count == player_number


# count = (count + 1)
