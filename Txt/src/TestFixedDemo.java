public class TestFixedDemo{
    public static void main(String[] args) {
        Fixed<String> s;
        s = new Fixed<String>(100);
        while (!StdIn.isEmpty())
        {
            String item = StdIn.readString();
            if (!item.equals("-"))
                s.push(item);
            else if (!s.isEmpty()) StdOut.print(s.pop() + " ");
        }
    }
}