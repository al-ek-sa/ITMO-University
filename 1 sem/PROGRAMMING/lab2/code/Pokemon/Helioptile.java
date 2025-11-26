import ru.ifmo.se.pokemon.*;
//Покемон 2
class Helioptile extends Pokemon{
    public Helioptile(String name, int level){
        super(name, level);
        super.setType(Type.ELECTRIC, Type.NORMAL);
        super.setStats(62, 55, 52, 109, 94, 109);
        addMove(new Swagger());
        addMove(new Bulldoze());
        addMove(new ThunderWave());
    }
}
