import math

effort_increase = 0.01
effort = math.pow(1+effort_increase, 365)
print("365天后的努力程度为:{:.2f}".format(effort))