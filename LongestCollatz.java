package Euler;

public class LongestCollatz {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int largest = 0;
		int index = 0;
		for(int i =1;i<=1000000;i++){
			if(collatz(i,0)>largest){
				System.out.println(collatz(i,0));
				index = i;
			}
		}
		System.out.println(index);
	}
	
	public static int collatz(int n, int level){
		if(n==1){
			return level+1;
		}
		if(n%2 == 0){
			return collatz(n/2, level+1);
		}
		else{
			return collatz(3*n + 1, level +1);
		}
	}

}
