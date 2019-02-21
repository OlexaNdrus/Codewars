def street_fighter_selection(fighters, initial_position, moves):
    hero_pass=[]
    if moves:
        position=[initial_position[0],initial_position[1]]
        for i in moves:
            if i=='up':
                position[0] = 0
            elif i=='down':
                position[0] = 1
            elif i=='right':
                position[1] += 1
                if position[1]>=len(fighters[0]):
                    position[1]=0
            else:
                position[1] -= 1
                if abs(position[1])>len(fighters[0]):
                    position[1] = -1
            hero_pass.append(fighters[position[0]][position[1]])
    return hero_pass

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
moves = ["right","right","right","right","right","right","right","right","right","right","right","right","right","left","left","left","left","left","left","left"]
initial_position=(0,0)


print(street_fighter_selection(fighters,initial_position,moves))