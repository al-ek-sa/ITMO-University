import ru.ifmo.se.pokemon.*;
//класс атаки EerieImpulse
class EerieImpulse extends StatusMove{
    public EerieImpulse() {
        super(Type.ELECTRIC, 0, 90);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(1).turns(-1).stat(Stat.SPECIAL_ATTACK, -2);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "EerieImpulse атака";
    }
}
