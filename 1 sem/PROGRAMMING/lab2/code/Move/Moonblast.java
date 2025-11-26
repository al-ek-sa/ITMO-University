import ru.ifmo.se.pokemon.*;
//класс атаки Moonblast
class Moonblast extends SpecialMove{
    public Moonblast() {
        super(Type.FAIRY, 95, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(0.3).turns(1).stat(Stat.ATTACK, -1);
    Effect.confuse(p);
    }
    @Override
    protected String describe() {
        return "Moonblast атака";
    }
}
