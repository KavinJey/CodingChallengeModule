import java.util.*;
import java.lang.*;

public class primes {

    //Uses Sieve of Atkin
    public static int[] primeGenerator(int limit) {
        int limitSqrt = (int) Math.sqrt((double) limit);
        boolean[] sieve = new boolean[limit + 1];
        Arrays.fill(sieve, false);

        sieve[0] = false;
        sieve[1] = false;
        sieve[2] = true;
        sieve[3] = true;


        for (int x = 1; x <= limitSqrt; x++) {
            for (int y = 1; y <= limitSqrt; y++) {
                // first quadratic using m = 12 and r in R1 = {r : 1, 5}
                int n = (4 * x * x) + (y * y);
                if (n <= limit && (n % 12 == 1 || n % 12 == 5)) {
                    sieve[n] = !sieve[n];
                }
                // second quadratic using m = 12 and r in R2 = {r : 7}
                n = (3 * x * x) + (y * y);
                if (n <= limit && (n % 12 == 7)) {
                    sieve[n] = !sieve[n];
                }
                // third quadratic using m = 12 and r in R3 = {r : 11}
                n = (3 * x * x) - (y * y);
                if (x > y && n <= limit && (n % 12 == 11)) {
                    sieve[n] = !sieve[n];
                } // end if
                // note that R1 union R2 union R3 is the set R
                // R = {r : 1, 5, 7, 11}
                // which is all values 0 < r < 12 where r is
                // a relative prime of 12
                // Thus all primes become candidates
            } // end for
        } // end for
        // remove all perfect squares since the quadratic
        // wheel factorization filter removes only some of them
        for (int n = 5; n <= limitSqrt; n++) {
            if (sieve[n]) {
                int x = n * n;
                for (int i = x; i <= limit; i += x) {
                    sieve[i] = false;
                } // end for
            } // end if
        } // end for
        // put the results to the System.out device
        // in 10x10 blocks

        int count = 0;
        for (int i = 0; i < sieve.length; i++) {
            if (sieve[i] == true) {
                count += 1;
            }

        }

        int[] primes = new int[count];
        count = 0;
        for (int i = 0; i < sieve.length; i++) {
            if (sieve[i] == true) {
                primes[count] = i;
                count += 1;
            }
        }

        return primes;
    }

    public static boolean isPrime(long num) {
        for (int i = 2; i < (num / 2); i++) {
            long remainder = num % i;

            if (remainder == 0) {
                return false;
            }
        }

        return true;

    }

    public static ArrayList<Integer> primeFactors(long num) {
        ArrayList arr = new ArrayList();

        while (num % 2 == 0) {
            arr.add(2);
            num = (long) (num / 2);
        }

        for (int i = 3; i < (long) (Math.sqrt(num)) + 1; i += 2) {
            while (num % i == 0) {
                arr.add(i);
                num = (long) (num / i);

            }
        }

        if (num > 2) {
            arr.add((long) num);
        }

        return arr;
    }


    public static void main(String[] args) {

        System.out.println(primeFactors(7));

    }

}

