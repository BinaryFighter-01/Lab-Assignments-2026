// Client.java
// RMI Client for String Concatenation
import java.rmi.registry.*;
import java.util.*;

public class Client {

    public static void main(String[] args)
    throws Exception {

        Registry r =
        LocateRegistry.getRegistry("localhost",1099);

        StringConcat s =
        (StringConcat) r.lookup("test");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter First String: ");
        String a = sc.nextLine();

        System.out.print("Enter Second String: ");
        String b = sc.nextLine();

        System.out.println("Result = " + s.join(a,b));
    }
}


// Server.java
// RMI Server for String Concatenation
import java.rmi.registry.*;

public class Server {

    public static void main(String[] args)
    throws Exception {

        Registry r =
        LocateRegistry.createRegistry(1099);

        r.rebind("test",
        new StringConcatImpl());

        System.out.println("Server Ready");
    }
}


// StringConcat.java
// Remote Interface for String Concatenation
import java.rmi.*;

public interface StringConcat extends Remote {

    String join(String a, String b)
    throws RemoteException;
}

//StringConcatImpl.java
// Implementation of the Remote Interface
import java.rmi.server.*;
import java.rmi.*;

public class StringConcatImpl
extends UnicastRemoteObject
implements StringConcat {

    StringConcatImpl() throws RemoteException {}

    public String join(String a, String b) {

        return a + b;
    }
}



