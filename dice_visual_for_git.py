#The diagram shows the approximate results that can be obtained for any number of different cubes.

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die_for_git import Die

# Creation of three dice.
die_1, die_2, die_3 = Die(3), Die(5), Die(9)

# Modeling a series of throws with saving the results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# Analysis of results.
max_result = die_1.number_sides + die_2.number_sides + die_3.number_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualization of results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D3, D5 and D9 dice 1000 times', 
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d3_d5_d9.html')

#As you can see, 3 and 17 are the least likely to come up, and 9, 10, and 11 are the most common.
#The ability to use Plotly to simulate dice rolls gives you a lot of freedom to explore this phenomenon. In a matter of minutes, you can simulate a huge number of rolls with a variety of dice.


