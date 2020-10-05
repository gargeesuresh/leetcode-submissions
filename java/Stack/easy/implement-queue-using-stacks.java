class MyQueue {
Stack<Integer> queue = new Stack<Integer>();
public void push(int x) {
    Stack<Integer> temp = new Stack<Integer>();
    while(!queue.empty()){
        temp.push(queue.pop());
    }
    queue.push(x);
    while(!temp.empty()){
        queue.push(temp.pop());
    }
}
public void pop() {
    queue.pop();
}
public int peek() {
    return queue.peek();
}
public boolean empty() {
    return queue.empty();
}
}

