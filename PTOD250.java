class SpecialQueue {
    private Queue<Integer> q;
    private Deque<Integer> minDeque;
    private Deque<Integer> maxDeque;
    public SpecialQueue() {
        q = new LinkedList<>();
        minDeque = new LinkedList<>();
        maxDeque = new LinkedList<>();
    }
    public void enqueue(int x) {
        q.add(x);
        while (!minDeque.isEmpty() && minDeque.peekLast() > x) {
            minDeque.pollLast();
        }
        minDeque.addLast(x);
        while (!maxDeque.isEmpty() && maxDeque.peekLast() < x) {
            maxDeque.pollLast();
        }
        maxDeque.addLast(x);
    }
    public void dequeue() {
        if (q.isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        int removed = q.poll();
        if (!minDeque.isEmpty() && removed == minDeque.peekFirst()) {
            minDeque.pollFirst();
        }
        if (!maxDeque.isEmpty() && removed == maxDeque.peekFirst()) {
            maxDeque.pollFirst();
        }
    }
    public int getFront() {
        if (q.isEmpty()) {
            throw new NoSuchElementException("Queue is empty!");
        }
        return q.peek();
    }
    public int getMin() {
        if (minDeque.isEmpty()) {
            throw new NoSuchElementException("Queue is empty!");
        }
        return minDeque.peekFirst();
    }
    public int getMax() {
        if (maxDeque.isEmpty()) {
            throw new NoSuchElementException("Queue is empty!");
        }
        return maxDeque.peekFirst();
    }
}
