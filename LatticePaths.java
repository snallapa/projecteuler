package Euler;

import java.math.BigInteger;

public class LatticePaths {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(factorial(5));
		System.out.println(paths(20,20));

	}
	public static BigInteger paths(int x, int y){
		BigInteger num = factorial(x+y);
		BigInteger num1 = factorial(x);
		BigInteger num2 = factorial(y);
		return num.divide((num1.multiply(num2)));

	}
	public static BigInteger factorial(int x){
		BigInteger ret = BigInteger.ONE;
		for(int i =1;i<=x;i++){
			ret = ret.multiply(BigInteger.valueOf(i));
		}
		return ret;
	}

}
