import java.net.*;
import java.io.*;
import java.util.Scanner;

public class ChatServer {
    private static DatagramSocket socket;
    private static InetAddress clientAddress;
    private static int clientPort = -1;
    private static volatile boolean running = true;

    public static void main(String[] args) throws IOException {
        int port = 9876;
        socket = new DatagramSocket(port);
        System.out.println("UDP Chat Server started on port " + port);
        System.out.println("Waiting for a client to say hello...");

        // Thread 1: continuously receive messages
        Thread receiveThread = new Thread(() -> {
            byte[] buffer = new byte[1024];
            while (running) {
                try {
                    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet); // blocks until a message arrives

                    // Learn the client's address/port from the first packet received
                    clientAddress = packet.getAddress();
                    clientPort = packet.getPort();

                    String message = new String(packet.getData(), 0, packet.getLength());

                    if (message.equalsIgnoreCase("exit")) {
                        System.out.println("\nClient disconnected.");
                        continue;
                    }

                    System.out.println("\nClient: " + message);
                    System.out.print("You: ");
                } catch (IOException e) {
                    if (running) e.printStackTrace();
                }
            }
        });
        receiveThread.setDaemon(true);
        receiveThread.start();

        // Main thread: read from console and send messages
        Scanner scanner = new Scanner(System.in);
        while (running) {
            String outgoing = scanner.nextLine();

            if (clientAddress == null) {
                System.out.println("No client has connected yet. Waiting...");
                continue;
            }

            byte[] data = outgoing.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(data, data.length, clientAddress, clientPort);
            socket.send(sendPacket);

            if (outgoing.equalsIgnoreCase("exit")) {
                running = false;
            } else {
                System.out.print("You: ");
            }
        }

        socket.close();
        scanner.close();
        System.out.println("Server shut down.");
    }
}