public class LoadBalancerLC{
    public static void main(String[] args){
        String servers[] = {
            "Server 1",
            "Server 2",
            "Server 3"
        };

        int connections [] = {4,5,2};

        for (int i = 1; i < 10;i++){
            int min = 0;

            for(int j = 1;j<connections.length;j++){
                if(connections[j]<connections[min]){
                    min = j;
                }
            }

            System.out.println(
                "Requests " + i + " is handled by " + servers[min]
            );

            connections[min]++;
        }
    }
}
