import ru.ifmo.se.pokemon.*;
//класс атаки Confide
class Confide extends StatusMove{
    public Confide() {
        super(Type.NORMAL, 0, 0);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    Effect e = new Effect().chance(1).turns(-1).stat(Stat.SPECIAL_ATTACK, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "Confide атака";
    }
}
