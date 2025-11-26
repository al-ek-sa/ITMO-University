import ru.ifmo.se.pokemon.*;
//класс атаки Swagger
class Swagger extends StatusMove{
    public Swagger() {
        super(Type.NORMAL, 0, 85);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
    super.applyOppEffects(p);
    Effect e = new Effect().turns(-1).stat(Stat.ATTACK, 2);
    p.addEffect(e);
    Effect.confuse(p);
    }
    @Override
    protected String describe() {
        return "Swagger атака";
    }
}
