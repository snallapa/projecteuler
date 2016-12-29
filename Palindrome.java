package Euler;

public class Palindrome {
	public static void main(String[] args) {
		System.out.println(findPalindrome());
	}
	public static int findPalindrome(){
		String numStr = "";
		int num = 0;
		int factor2 = 0;
		int realNum=0;
		for(int a=9;a>0;a--){
			for(int b = 9;b>-1;b--){
				for(int c = 9;c>-1;c--){
					numStr = "" + a + b + c + c + b + a;
					num = Integer.parseInt(numStr);
					for(int factor = 100;factor<1000;factor++){
						if(num%factor==0){
							factor2 = num/factor;
							if(String.valueOf(factor).length()==3 && String.valueOf(factor2).length()==3){
								return num;
								
							}
						}
					}
				}
			}
		}

				
		
		
		return realNum;
	}

}
