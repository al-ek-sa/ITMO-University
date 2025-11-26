import ru.ifmo.se.pokemon.*;
//класс атаки CloseCombat
class CloseCombat extends PhysicalMove{
    public CloseCombat() {
        super(Type.FIGHTING, 120, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    Effect e = new Effect().stat(Stat.DEFENSE, -1).stat(Stat.SPECIAL_DEFENSE, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "CloseCombat атака";
    }
}
 