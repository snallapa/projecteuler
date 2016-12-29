package Euler;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.math.BigInteger;

public class FiftyDigitSum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		BigInteger[] numbers = readNumbers();
		BigInteger sum = BigInteger.ZERO;
		for(int i =0;i<100;i++){
			sum = sum.add(numbers[i]);
		}
		String str = sum.toString();
		System.out.println(sum);
		System.out.println(str.substring(0,10));
	}

	public static BigInteger[] readNumbers() {
		BigInteger[] numbers = new BigInteger[100];
		Reader fr = null;
		try {
			fr = new InputStreamReader(new FileInputStream("numbers"));
			BufferedReader reader = new BufferedReader(fr);
			String line = reader.readLine();
			int i = 0;
			while (line != null) {
				line = line.trim();
				if(line.isEmpty()){
					continue;
				}
				System.out.println(line);
				numbers[i] = new BigInteger(line);
				i++;
				line = reader.readLine();
			}
			fr.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return numbers;

	}

}
