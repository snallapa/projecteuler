package Euler;

public class PrimeSum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(primeSum(2000000));

	}

	public static long primeSum(int max) {
		long sum = 2;
		for (long i = 1; i < max; i = i + 2) {
			if (isPrime(i)) {
				sum += i;
			}
		}
		return sum;
	}

	public static boolean isPrime(long num) {
		if (num == 1) {
			return false;
		}
		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;
	}

}
