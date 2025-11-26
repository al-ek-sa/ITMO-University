import ru.ifmo.se.pokemon.*;
//Покемон 4
class Flabebe extends Pokemon{
    public Flabebe(String name, int level){
        super(name, level);
        super.setType(Type.FAIRY);
        super.setStats(44, 38, 39, 61, 79, 42);
        addMove(new Moonblast());
        addMove(new Psychic());
    }
}
