import ru.ifmo.se.pokemon.*;
//класс атаки EnergyBall
class EnergyBall extends SpecialMove{
    public EnergyBall() {
        super(Type.GRASS, 90, 100);
    }
     @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(0.1).turns(-1).stat(Stat.SPECIAL_DEFENSE, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "EnergyBall атака";
    }
}
