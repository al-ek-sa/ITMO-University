import ru.ifmo.se.pokemon.*;
//Покемон 6
class Florges extends Floette{
    public Florges(String name, int level){
        super(name, level);
        super.setType(Type.FAIRY);
        super.setStats(78, 65, 68, 112, 154, 75);
        addMove(new Moonblast());
        addMove(new Psychic());
        addMove(new FairyWind());
        addMove(new EnergyBall());
    }
}
