package Euler;

import java.math.BigInteger;

public class factorialDigitSum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BigInteger num = factorial(100);
		System.out.println(digitSum(num));
	}
	public static BigInteger digitSum(BigInteger num){
		BigInteger sum = BigInteger.ZERO;
		while(num.compareTo(BigInteger.ZERO) ==1){
			sum = sum.add(num.mod(BigInteger.TEN));
			num = num.divide(BigInteger.TEN);
		}
		return sum;
	}
	
	public static BigInteger factorial(int max){
		if(max ==1){
			return BigInteger.valueOf(1);
		}
		else{
			return BigInteger.valueOf(max).multiply(factorial(max-1));
		}
	}

}
