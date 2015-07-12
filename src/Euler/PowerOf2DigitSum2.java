package Euler;

import java.math.BigInteger;

public class PowerOf2DigitSum2 {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		BigInteger num = twoPower(1000);
		System.out.println(digitSum(num));
	}
	
	public static BigInteger digitSum(BigInteger num){
		BigInteger sum = BigInteger.ZERO;
		BigInteger mod = BigInteger.ZERO;
		while(num.compareTo(BigInteger.ZERO) ==1){
			mod = num.mod(BigInteger.TEN);
			sum = sum.add(mod);
			num = num.divide(BigInteger.TEN);
		}
		return sum;
	}
	public static BigInteger twoPower(int num){
		if(num==1){
			return BigInteger.valueOf(2);
		}
		else{
			return BigInteger.valueOf(2).multiply(twoPower(num -1));
		}
	}

}
