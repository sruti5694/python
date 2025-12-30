colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF','purple':'#800080','yellow':'#FFFF00',
'cyan':'#00FFFF','magenta':'#FF00FF','black':'#000000','white':'#FFFFFF'}
print(colors)
print(colors['purple'])
print(colors.get('cyan'))
colors['ray'] = 23
print(colors)
colors.update({'yellow':87})
print(colors)
del colors['black']
print(colors)
colors.pop('white')
print(colors)
colors.popitem()
print(colors)
# colors.clear()
# print(colors)
new = colors.copy()
print(new)
new1 = dict(colors)
print(new1)