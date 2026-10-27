import java.util.Scanner;

public class TSP_DFS {

    static int n;              // number of cities
    static int[][] dist;       // distance matrix
    static int minCost = Integer.MAX_VALUE;

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

        boolean[] visited = new boolean[n];
        visited[0] = true;   // start at city 0

        dfsTSP(0, visited, 1, 0);

        System.out.println("\n--- DFS (Backtracking) Result ---");
        System.out.println("Minimum tour cost: " + minCost);

        sc.close();
    }

    static void dfsTSP(int currentCity, boolean[] visited, int count, int cost) {
        
        if (count == n) {
            int totalCost = cost + dist[currentCity][0];
            minCost = Math.min(minCost, totalCost);
            return;
        }

        for (int next = 0; next < n; next++) {
            if (!visited[next]) {
                visited[next] = true;  
                dfsTSP(next, visited, count + 1, cost + dist[currentCity][next]);
                visited[next] = false;  
            }
        }
    }
}