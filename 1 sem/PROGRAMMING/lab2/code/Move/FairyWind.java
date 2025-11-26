import ru.ifmo.se.pokemon.*;
//класс атаки FairyWind
class FairyWind extends SpecialMove{
    public FairyWind() {
        super(Type.FAIRY, 40, 100);
    }
//Fairy Wind deals damage with no added effects.
    @Override
    protected String describe() {
        return "FairyWind атака";
    }
}
