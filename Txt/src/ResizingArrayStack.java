import java.util.Iterator;
public class ResizingArrayStack<Item> implements Iterator<Item>
{
    private Item[] a = (Item[]) new Object[1];
    private int i = 0;
    private int N = 0;
    public boolean isEmpty() { return N == 0;}
    public boolean hasNext() { return i < N;}
    public Item next() { return a[++i];}
    private void resize(int max)
    {
        Item[] temp = (Item[]) new Object[max];
        for(int i = 0; i < N; ++i)
            temp[i] = a[i];
        a = temp;
    }
    public void push(Item item)
    {
        if (N == a.length) resize(2*a.length);
        a[N++] = item;
    }
    public Item pop()
    {
        a[N] = null;
        if (N > 0 && N == a.length/4)
            resize(a.length/2);
        return a[--N];
    }
    public Iterator<Item> iterator()
    {return new ResizingArrayStack();}
    private class ReverseArrayIterator implements Iterator<Item>
    {
        private int i = N;
        public boolean hasNext() {return i > 0;}
        public Item next() { return a[--i];}

    }
}