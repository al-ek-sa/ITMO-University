import ru.ifmo.se.pokemon.*;
//класс атаки Psychic
class Psychic extends SpecialMove{
    public Psychic() {
        super(Type.PSYCHIC, 90, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().chance(0.1).turns(-1).stat(Stat.SPECIAL_DEFENSE, -1);
    p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "Psychic атака";
    }
}
