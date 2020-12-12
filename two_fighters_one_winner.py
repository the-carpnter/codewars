def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        f, s = fighter1, fighter2
    else:
        f, s = fighter2, fighter1
    while True:
        if f.health <= 0:
            return s.name
        s.health -= f.damage_per_attack
        if s.health <= 0:
            return f.name
        f.health -= s.damage_per_attack
