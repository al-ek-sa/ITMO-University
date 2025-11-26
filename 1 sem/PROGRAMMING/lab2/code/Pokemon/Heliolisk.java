import ru.ifmo.se.pokemon.*;
//Покемон 3
class Heliolisk extends Helioptile{
    public Heliolisk(String name, int level){
        super(name, level);
        super.setType(Type.FIGHTING);
        super.setStats(75, 125, 75, 30, 75, 85);
        addMove(new Swagger());
        addMove(new Bulldoze());
        addMove(new ThunderWave());
        addMove(new EerieImpulse());
    }
}
