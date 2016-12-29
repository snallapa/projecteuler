package Euler;

public class SmallestMultiple {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(smallest(20));

	}
	
	public static double smallest(int max){
		int product =1;
		for(int i =4;i<max;i++){
			if(isPrime(i)){
				product = product*i;
			}
		}
		double highestTwos = Math.pow(2,highestTwo(max));
		double highestThree = Math.pow(3,highestThree(max));
		long num = (long)(product*highestTwos*highestThree);
		return num;
	}
	
	public static int highestTwo(int max){
		int high = 0;
		for(int i =0;i<=max;i++){
			if(Math.pow(2.0, (double)(i))>max){
				high = i-1;
				break;
			}
		}
		return high;
	}
	
	public static int highestThree(int max){
		int high = 0;
		for(int i =0;i<=max;i++){
			if(Math.pow(3.0, (double)(i))>max){
				high = i-1;
				break;
			}
		}
		return high;
	}
	public static boolean isPrime(int num){
		for(int i = 2;i<num;i++){
			if(num%i ==0 || num == i){
				return false;
			}
		}
		return true;
	}

}
