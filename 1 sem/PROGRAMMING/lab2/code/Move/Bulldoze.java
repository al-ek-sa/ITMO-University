import ru.ifmo.se.pokemon.*;
//класс атаки Bulldoze
class Bulldoze extends PhysicalMove{
    public Bulldoze() {
        super(Type.GROUND, 60, 100);
    }
    protected void applyOppEffects(Pokemon p) {
    Effect e = new Effect().stat(Stat.SPEED, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "Bulldoze атака";
    }
}
