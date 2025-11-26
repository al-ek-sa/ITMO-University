import ru.ifmo.se.pokemon.*;
//Создание боя
public class Bitva1 {
    public static void main(String[] args) {
        Battle b = new Battle();
        Sawk p1 = new Sawk ("", 55);
        Helioptile p2 = new Helioptile ("", 32);
        Heliolisk p3 = new Heliolisk("", 44);
        Flabebe p4 = new Flabebe("", 48);
        Floette p5 = new Floette("", 58);
        Florges p6 = new Florges("", 5);
        b.addAlly(p1);
        b.addFoe(p2);
        b.addFoe(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}
