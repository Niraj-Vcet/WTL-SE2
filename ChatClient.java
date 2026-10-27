import java.net.*;
import java.io.*;
import java.util.Scanner;

public class ChatClient {
    private static DatagramSocket socket;
    private static InetAddress serverAddress;
    private static int serverPort;
    private static volatile boolean running = true;

    public static void main(String[] args) throws IOException {
        serverPort = 9876;
        serverAddress = InetAddress.getByName("localhost"); // change to server IP if remote

        socket = new DatagramSocket();
        System.out.println("Connected to UDP Chat Server at " + serverAddress.getHostAddress() + ":" + serverPort);
        System.out.println("Type a message and press Enter. Type 'exit' to quit.");

        // Thread 1: continuously receive messages from the server
        Thread receiveThread = new Thread(() -> {
            byte[] buffer = new byte[1024];
            while (running) {
                try {
                    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet); // blocks until a message arrives

                    String message = new String(packet.getData(), 0, packet.getLength());

                    if (message.equalsIgnoreCase("exit")) {
                        System.out.println("\nServer ended the chat.");
                        running = false;
                        continue;
                    }

                    System.out.println("\nServer: " + message);
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
        // Send an initial "hello" so the server learns our address/port
        byte[] hello = "Hello from client".getBytes();
        socket.send(new DatagramPacket(hello, hello.length, serverAddress, serverPort));
        System.out.print("You: ");

        while (running) {
            String outgoing = scanner.nextLine();

            byte[] data = outgoing.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(data, data.length, serverAddress, serverPort);
            socket.send(sendPacket);

            if (outgoing.equalsIgnoreCase("exit")) {
                running = false;
            } else {
                System.out.print("You: ");
            }
        }

        socket.close();
        scanner.close();
        System.out.println("Client shut down.");
    }
}