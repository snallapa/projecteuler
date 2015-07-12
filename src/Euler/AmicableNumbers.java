package Euler;

public class AmicableNumbers {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum =0;
		int i =1;
		int num2=0;
		while(i<10000){
			num2 = divisorSum(i);
			if(i == divisorSum(num2)){
				sum +=i;
				System.out.println(sum);
			}
			i++;
		}
		System.out.println(sum);
		
	}
	
	public static int divisorSum(int num){
		int sum = 0;
		for(int i =1;i<num/2 + 1;i++){
			if(num%i == 0){
				sum +=i;
			}
		}
		return sum;
	}
	

}
