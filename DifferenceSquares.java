package Euler;

public class DifferenceSquares {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(squareOfSum(100) - sumOfSquare(100));

	}
	public static int sumOfSquare(int max){
		int sum = 0;
		for(int i =1;i<=max;i++){
			sum += i*i;
		}
		return sum;
	}
	public static int squareOfSum(int max){
		int sum = 0;
		for(int i =1;i<=max;i++){
			sum += i;
		}
		return sum*sum;
	}

}
