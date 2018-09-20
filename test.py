package test;

public class Test {

	public static void main(String[] args) {
	

	}

}

/*
Get X and Y from the Joystick, do whatever scaling and calibrating you need to do based on your hardware.
Invert X
Calculate R+L (Call it V): V =(100-ABS(X)) * (Y/100) + Y
Calculate R-L (Call it W): W= (100-ABS(Y)) * (X/100) + X
Calculate R: R = (V+W) /2
Calculate L: L= (V-W)/2
Do any scaling on R and L your hardware may require.
Send those values to your Robot.
Go back to 1.
*/
