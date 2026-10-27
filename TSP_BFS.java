
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class TSP_BFS {

    static int n;              // number of cities
    static int[][] dist;       // distance matrix

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of cities: ");
        n = sc.nextInt();

        dist = new int[n][n];
        System.out.println("Enter the distance matrix (n x n):");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = sc.nextInt();
            }
        }

        int minCost = bfsTSP();

        System.out.println("\n--- BFS Result ---");
        System.out.println("Minimum tour cost: " + minCost);

        sc.close();
    }

    static int bfsTSP() {
        int minCost = Integer.MAX_VALUE;
        Queue<State> queue = new LinkedList<>();

        boolean[] startVisited = new boolean[n];
        startVisited[0] = true;
        queue.add(new State(0, startVisited, 1, 0));

        while (!queue.isEmpty()) {
            State current = queue.poll();

            // All cities visited -> close the tour
            if (current.count == n) {
                int totalCost = current.cost + dist[current.currentCity][0];
                minCost = Math.min(minCost, totalCost);
                continue;
            }

            // Generate all valid next states and push them into the queue
            for (int next = 0; next < n; next++) {
                if (!current.visited[next]) {
                    boolean[] newVisited = current.visited.clone();
                    newVisited[next] = true;
                    queue.add(new State(
                            next,
                            newVisited,
                            current.count + 1,
                            current.cost + dist[current.currentCity][next]
                    ));
                }
            }
        }
        return minCost;
    }

    static class State {

        int currentCity;
        boolean[] visited;
        int count;   // number of cities visited so far
        int cost;    // distance travelled so far

        State(int currentCity, boolean[] visited, int count, int cost) {
            this.currentCity = currentCity;
            this.visited = visited.clone();
            this.count = count;
            this.cost = cost;
        }
    }
}
