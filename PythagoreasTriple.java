package Euler;

public class PythagoreasTriple {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(pyth());

	}
	public static int pyth(){
		for(int a = 1;a<3333;a++){
			for(int b = 1;b<3333;b++){
				for(int c = 1;c<3333;c++){
					if(a + b + c == 1000){
						if(Math.pow(a, 2) + Math.pow(b,2) == Math.pow(c, 2)){
							return a*b*c;
						}
					}
				}
			}
		}
		return 0;
	}
	

}
