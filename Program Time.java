import java.util.*;

public class Main{

    public static int findLargestCycle(int[] edges) {
        int n = edges.length;
        int largestCycle = -1;
        boolean[] visited = new boolean[n];
        int[] pathLength = new int[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                Map<Integer, Integer> visitedInCurrentPath = new HashMap<>();
                int current = i;
                int length = 0;

                while (current != -1 && !visited[current]) {
                    visited[current] = true;
                    visitedInCurrentPath.put(current, length);
                    current = edges[current];
                    length++;
                }

                if (current != -1 && visitedInCurrentPath.containsKey(current)) {
                    largestCycle = Math.max(largestCycle, length - visitedInCurrentPath.get(current));
                }
            }
        }

        return largestCycle;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] edges = new int[N];

        for (int i = 0; i < N; i++) {
            edges[i] = sc.nextInt();
        }

        System.out.println(findLargestCycle(edges));
    }
}