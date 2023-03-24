effort_increase = 0.01
effort = 1
for day in range (365):
    if day % 2 == 0:
        effort *= (1 + effort_increase) 
print("365天后的努力程度为:{:.2f}".format(effort))