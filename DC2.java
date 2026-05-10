// Client.java
// RMI Client for String Concatenation
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            // Locate the registry on localhost
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            
            // Lookup the remote object
            StringConcat stub = (StringConcat) registry.lookup("StringConcatService");
            
            Scanner scanner = new Scanner(System.in);
             
            System.out.println("   RMI String Concatenation Client");
           
            
            // Get input from user
            System.out.print("Enter first string: ");
            String str1 = scanner.nextLine();
            
            System.out.print("Enter second string: ");
            String str2 = scanner.nextLine();
            
            
            System.out.println("Sending strings to server...");
            
            // Call the remote method
            String result = stub.concatenate(str1, str2);
            
            // Display result
            System.out.println("Result from Server:");
            System.out.println("Concatenated String: " + result);
            
            
            scanner.close();
            
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}


// Server.java
// RMI Server for String Concatenation
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Create an instance of the implementation
            StringConcatImpl obj = new StringConcatImpl();
            
            // Create RMI registry on port 1099
            Registry registry = LocateRegistry.createRegistry(1099);
            
            // Bind the remote object in the registry
            registry.rebind("StringConcatService", obj);
            
            
            System.out.println("   RMI String Concatenation Server");
           
            System.out.println("Server is ready and waiting for clients...");
            System.out.println("Service bound as: StringConcatService");
            System.out.println("Port: 1099");
            
            
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}


// StringConcat.java
// Remote Interface for String Concatenation
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface StringConcat extends Remote {
    // Remote method to concatenate two strings
    String concatenate(String str1, String str2) throws RemoteException;
}


//StringConcatImpl.java
// Implementation of the Remote Interface
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringConcatImpl extends UnicastRemoteObject implements StringConcat {
    
    // Constructor
    public StringConcatImpl() throws RemoteException {
        super();
    }
    
    // Implementation of concatenate method
    @Override
    public String concatenate(String str1, String str2) throws RemoteException {
        System.out.println("Server received request to concatenate:");
        System.out.println("String 1: " + str1);
        System.out.println("String 2: " + str2);
        String result = str1 + str2;
        System.out.println("Result: " + result);
        System.out.println("----------------------------");
        return result;
    }
}



