package queue;
class MyCircularQueue {

    /**
     * 队列长度
     */
    private Integer length = 0;

    /**
     * 队首(指向当前队首元素的位置, 初始值为-1)
     */
    private Integer front = -1;

    /**
     * 队尾(指向下一个插入的位置)
     */
    private Integer rear = 0;

    /**
     * 存储数组
     */
    private Integer[] array;

    /**
     * 元素个数
     */
    private Integer count = 0;

    /**
     * Initialize your data structure here. Set the size of the queue to be k.
     */
    public MyCircularQueue(int k) {
        array = new Integer[k];
        this.length = array.length;
    }

    /**
     * Insert an element into the circular queue. Return true if the operation is successful.
     */
    public boolean enQueue(int value) {
        if (count == 0) {
            front = ++front % this.length;
            rear = ++rear % this.length;
            array[front] = value;
            count++;
            return true;
        }
        if (count >= this.length) return false;
        array[rear] = value;
        rear = ++rear % this.length;
        count++;
        return true;
    }

    /**
     * Delete an element from the circular queue. Return true if the operation is successful.
     */
    public boolean deQueue() {
        if (count == 0) return false;
        if (count == 1) {
            front = (front - 1) % this.length;
            rear = (rear - 1) % this.length;
            count--;
            return true;
        }
        front = (++front % this.length);
        count--;
        return true;
    }

    /**
     * Get the front item from the queue.
     */
    public int Front() {
        if (count == 0) return -1;
        return array[front];
    }

    /**
     * Get the last item from the queue.
     */
    public int Rear() {
        if (count == 0) return -1;
        return array[(this.length + rear -1) % this.length];
    }

    /**
     * Checks whether the circular queue is empty or not.
     */
    public boolean isEmpty() {
        if (count == 0) return true;
        return false;
    }

    /**
     * Checks whether the circular queue is full or not.
     */
    public boolean isFull() {
        if (count == this.length) return true;
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
