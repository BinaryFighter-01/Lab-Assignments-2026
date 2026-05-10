// HotelClient.java

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {

    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            HotelInterface stub = (HotelInterface) registry.lookup("HotelService");

            Scanner sc = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Exit");

                int choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {
                    case 1:
                        System.out.print("Enter Guest Name: ");
                        String name = sc.nextLine();

                        System.out.print("Enter Room Number: ");
                        String room = sc.nextLine();

                        System.out.println(stub.bookRoom(name, room));
                        break;

                    case 2:
                        System.out.print("Enter Guest Name: ");
                        String cname = sc.nextLine();

                        System.out.println(stub.cancelBooking(cname));
                        break;

                    case 3:
                        System.exit(0);
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// HotelImpl.java

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.HashMap;

public class HotelImpl extends UnicastRemoteObject implements HotelInterface {

    HashMap<String, String> bookings;

    protected HotelImpl() throws RemoteException {
        bookings = new HashMap<>();
    }

    public synchronized String bookRoom(String guestName, String roomNo) throws RemoteException {

        if (bookings.containsKey(guestName)) {
            return "Booking already exists for " + guestName;
        }

        bookings.put(guestName, roomNo);
        return "Room " + roomNo + " booked for " + guestName;
    }

    public synchronized String cancelBooking(String guestName) throws RemoteException {

        if (!bookings.containsKey(guestName)) {
            return "No booking found for " + guestName;
        }

        bookings.remove(guestName);
        return "Booking cancelled for " + guestName;
    }
}

// HotelInterface.java

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelInterface extends Remote {

    String bookRoom(String guestName, String roomNo) throws RemoteException;

    String cancelBooking(String guestName) throws RemoteException;
}

// HotelServer.java

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelServer {

    public static void main(String[] args) {
        try {
            HotelImpl obj = new HotelImpl();

            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("HotelService", obj);

            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
