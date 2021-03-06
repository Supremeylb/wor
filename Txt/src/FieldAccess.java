//Super sub = new Sub()

class Super {
    public int field = 0;
    public int getField() {
        return field;
    }
}

class Sub extends Super {
    public int field = 1;
    public int getField() {
        return field;
    }
    public int getSuperField() {
        return super.field;
    }
}

public class FieldAccess {

    public static void main(String[] args) {
        Super sup = new Sub();
        System.out.println("sup.filed = " + sup.field + 
                ", sup.getSuperField() = " + sup.getField());
        Sub sub = new Sub();
        System.out.println("sub.filed = " + sub.field + 
                ", sub.getField() = " + sub.getField() + 
                ", sub.getSuperField() = " + sub.getSuperField());
    }
}