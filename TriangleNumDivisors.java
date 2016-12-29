package Euler;

public class TriangleNumDivisors {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int divisors = 0;
		int sum = 0;
		int i =1;
		while(divisors<500){
			sum = i*(i+1)/2;
			divisors = divisors(sum);
			System.out.println(divisors);
			i++;
		}
		System.out.println(sum);
		

	}
	public static int divisors(int num){
		int divisors = 0;
		for(int i =1;i<=num;i++){
			if(num%i == 0){
				divisors+=1;
			}
		}
		return divisors;
	}

}
