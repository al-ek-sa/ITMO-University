import ru.ifmo.se.pokemon.*;
//класс атаки LowSweep
class LowSweep extends PhysicalMove{
    public LowSweep() {
        super(Type.FIGHTING, 65, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(1).turns(-1).stat(Stat.SPEED, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "LowSweep атака";
    }
}