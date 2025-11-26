import ru.ifmo.se.pokemon.*;
//класс атаки ThunderWave
class ThunderWave extends StatusMove{
    public ThunderWave() {
        super(Type.ELECTRIC, 0, 100);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect.paralyze(p);
    }
    @Override
    protected String describe() {
        return "ThunderWave атака";
    }
}
