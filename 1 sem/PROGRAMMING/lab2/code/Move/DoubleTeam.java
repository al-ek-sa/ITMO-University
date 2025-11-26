import ru.ifmo.se.pokemon.*;
//класс атаки DoubleTeam
class DoubleTeam extends StatusMove{
    public DoubleTeam() {
        super(Type.NORMAL, 0, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(1).turns(-1).stat(Stat.EVASION, 1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "DoubleTeam атака";
    }
}
