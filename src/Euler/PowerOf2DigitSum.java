package Euler;

public class PowerOf2DigitSum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long num = (long)Math.pow(2,1000);
		int sum = 0;
		while(num>0){
			sum += num%10;
			num = num/10;
		}
		System.out.println(sum);
	}

}
