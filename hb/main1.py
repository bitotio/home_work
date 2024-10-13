from hitbox import Hitbox



Hb1 = Hitbox(0, 0, 100, 100)
Hb2 = Hitbox(50, 50, 100, 100)
Hb3 = Hitbox(130, 130, 100, 100)


industriction1 = Hb1.intersects(Hb2)
industriction2 = Hb2.intersects(Hb3)
industriction3 = Hb1.intersects(Hb3)
print(industriction1,industriction2, industriction3)


