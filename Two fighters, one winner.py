def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    attacker = first_attacker
    if fighter1.name==first_attacker:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health<=0:
            return attacker.name
        attacker,defender=defender,attacker
