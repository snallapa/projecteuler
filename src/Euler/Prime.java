package Euler;

public class Prime {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(largePrime());

	}
	public static int largePrime(){
		int i =0;
		int n = 1;
		while(i<=10001){
			if(isPrime(n) == true){
				i++;

			}
			n++;
		}
		return n;
	}
	
	public static boolean isPrime(int num){
		for(int i =2;i<num;i++){
			if(num%i == 0){
				return false;
			}
		}
		return true;
	}

}
