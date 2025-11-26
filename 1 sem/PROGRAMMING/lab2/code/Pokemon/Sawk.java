import ru.ifmo.se.pokemon.*;
//Покемон 1
class Sawk extends Pokemon{
    public Sawk(String name, int level){
        super(name, level);
        super.setType(Type.ELECTRIC, Type.NORMAL);
        super.setStats(44, 38, 33, 61, 43, 70);
        addMove(new DoubleTeam());
        addMove(new LowSweep());
        addMove(new CloseCombat());
        addMove(new Confide());
    }
}