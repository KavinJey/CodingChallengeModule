import java.util.*;
import static java.lang.Math.*;

public class Main {
    //Java version of Competitive coding library
    //Collection of algorithms that would prove useful in a competitive coding setting

    public static int[] primeGenerator(int n) {
        boolean[] arr = new boolean[n];
        for(int i = 0; i < n; i++) {
            arr[i] = true;
        }

        //Marks all non-primes false
        for(int i = 2; i < sqrt(n); i++) {
            if (arr[i] == true) {

                for(int j =i*i; j < n; j +=i) {
                    arr[j] = false;
                }
            }
        }

        int[] primes = new int[n];
        int count = 0;
        for(int i = 0; i < primes.length; i++) {
            if (arr[i] == true) {
                primes[count] = i;
                count++;
            }
        }

        return primes;

    }






    public static void main (String[] args) {
        System.out.print(Arrays.toString(primeGenerator(300)));

    }


}
