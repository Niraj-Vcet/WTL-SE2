import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SecretMessageDecoder {

    public static void printSecretMessage(String docUrl) {
        try {
            List<CharPoint> points = parseCharPoints(fetchHtml(docUrl));
            printGrid(points);
        } catch (Exception e) {
            throw new RuntimeException("Failed to decode secret message", e);
        }
    }

    private static String fetchHtml(String url) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url.trim()))
                .header("User-Agent", "Mozilla/5.0")
                .GET()
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient().send(
                request,
                HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8)
        );

        if (response.statusCode() < 200 || response.statusCode() >= 300) {
            throw new IOException("HTTP error: " + response.statusCode());
        }

        return response.body();
    }

    private static List<CharPoint> parseCharPoints(String html) {
        Document document = Jsoup.parse(html);
        Element table = document.selectFirst("table");

        if (table == null) {
            throw new IllegalStateException("No table found.");
        }

        Elements rows = table.select("tr");
        if (rows.isEmpty()) {
            throw new IllegalStateException("Table contains no rows.");
        }

        Elements headerCells = rows.first().children();

        for (int i = 1; i < rows.size(); i++) {
            Elements cells = rows.get(i).children();

            if (cells.size() <= 3) {
                continue;
            }

            try {
                int x = Integer.parseInt(cells.get(0).text().trim());
                int y = Integer.parseInt(cells.get(1).text().trim());
                String character = cells.get(2).text();

                if (!character.isEmpty()) {
                    points.add(new CharPoint(x, y, character.charAt(0)));
                }
            } catch (NumberFormatException ignored) {
                // Ignore non-data rows.
            }
        }

        return points;
    }

    private static void printGrid(List<CharPoint> points) {
        if (points.isEmpty()) {
            System.out.println("(no data found)");
            return;
        }

        int minX = points.stream().mapToInt(CharPoint::x).min().orElse(0);
        int maxX = points.stream().mapToInt(CharPoint::x).max().orElse(0);
        int minY = points.stream().mapToInt(CharPoint::y).min().orElse(0);
        int maxY = points.stream().mapToInt(CharPoint::y).max().orElse(0);

        char[][] grid = new char[maxY - minY + 1][maxX - minX + 1];

        for (char[] row : grid) {
            Arrays.fill(row, ' ');
        }

        for (CharPoint point : points) {
            grid[point.y() - minY][point.x() - minX] = point.ch();
        }

        for (char[] row : grid) {
            System.out.println(new String(row));
        }
    }

    private static final class CharPoint {
        private final int x;
        private final int y;
        private final char ch;

        CharPoint(int x, int y, char ch) {
            this.x = x;
            this.y = y;
            this.ch = ch;
        }

        int x() {
            return x;
        }

        int y() {
            return y;
        }

        char ch() {
            return ch;
        }
    }

    public static void main(String[] args) {
        String exampleDocUrl =
                "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub";

        printSecretMessage(exampleDocUrl);
    }
}