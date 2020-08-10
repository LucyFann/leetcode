package queue;

import java.util.LinkedList;
import java.util.Queue;

public class numIslands {

    public static Integer numIslands(int[][] numIslands) {
 
        if (numIslands.length == 0) {
            return 0;
        }
 
        // 岛屿数量
        int count = 0;
 
        // 循环未知海域的二维数组
        for (int i = 0; i < numIslands.length; i ++) {
            for (int j = 0; j < numIslands[i].length; j ++) {
 
                // numIslands 拥有的值有：1 未探索的岛屿，0 海域，-1 已探索的岛屿
                if (numIslands[i][j] == 1) {
                    count ++;
                    System.out.println("岛屿登陆点（根节点），这是发现的第" + count + "座岛屿");
                }
                // 开始 BFS 广度优先算法探索岛屿
                visitLand(numIslands, i, j);
            }
        }
        return count;
    }
 
    public static void visitLand(int[][] numIslands, int i, int j) {
 
        // 声明队列
        Queue<Integer> queue = new LinkedList<>();
 
        // 在后面 while 的循环中，如果是岛屿，也会陆续把这个岛屿周围的点的定位添加到队列中
        // 所有点都以 先 i，后 j，的顺序添加，因此队列以 i，j 交错的形式存在
        // i 与后一个 j 组成一个需要探索的位置，也可以理解成一个需要探索点的坐标
        // 而探索的顺序就是从根节点开始，第一层的点全部探索完后，之后探索第二层的所有点，以此类推
        // 不太理解的需要好好理解下
        // 把 i 放入队列
        queue.offer(i);
 
        // 把 j  放入队列
        queue.offer(j);
 
        // 循环队列
        // 每次循环都取一对 i，j，以此锁定一个需要探索的海域
        while (!queue.isEmpty()) {
 
            // 队列的 poll 方法会把队列最前面的值返回后，把这个值删除
            i = queue.poll();
 
            j = queue.poll();
 
            // 如果这个点是海域或者已探索的岛屿都跳过
            if (numIslands[i][j] != 1) {
                continue;
            }
 
            // 记录下这个点探索过了，把探索过的点状态变为 -1
            numIslands[i][j] = -1;
 
            // 把这个点的上面点加入队列
            if (i - 1 >= 0) {
                queue.offer(i - 1);
                queue.offer(j);
            }
 
            // 把这个点的下面点加入队列
            if (i + 1 < numIslands.length) {
                queue.offer(i + 1);
                queue.offer(j);
            }
 
            // 把这个点的左面点加入队列
            if (j - 1 >= 0) {
                queue.offer(i);
                queue.offer(j - 1);
            }
 
            // 把这个点的右面点加入队列
            if (j + 1 < numIslands[i].length) {
                queue.offer(i);
                queue.offer(j + 1);
            }
        }
    }
 

}