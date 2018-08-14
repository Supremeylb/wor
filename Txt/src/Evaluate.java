import java.util.Stack;

public class Evaluate{
    public static void main(String[] args) {
        Stack<String> ops = new Stack<String>();
        Stack<Double> vals = new Stack<Double>();
        while (!StdIn.isEmpty()){
            String s = StdIn.readString();
            if      (s.equals("("))  ;
            else if (s.equals("+")) ops.push(s);
            else if (s.equals("-")) ops.push(s);
            else if (s.equals("*")) ops.push(s);
            else if (s.equals("/")) ops.push(s);
            else if (s.equals("sqrt")) ops.push(s);
            else if (s.equals(")")){
                String op = ops.pop();
                double v = vals.pop();
                if (op.equals("+")) v += vals.pop();
                if (op.equals("-")) v += vals.pop();
                if (op.equals("*")) v += vals.pop();
                if (op.equals("/")) v += vals.pop();
                vals.push(v);
            }
        }
        StdOut.println(vals.pop());
    }
}