import ru.ifmo.se.pokemon.*;
//Покемон 5
class Floette extends Flabebe{
    public Floette(String name, int level){
        super(name, level);
        super.setType(Type.FAIRY);
        super.setStats(54, 45, 47, 75, 98, 52);
        addMove(new Moonblast());
        addMove(new Psychic());
        addMove(new FairyWind());
    }
}
