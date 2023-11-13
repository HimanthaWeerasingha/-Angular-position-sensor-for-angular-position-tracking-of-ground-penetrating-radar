//Sensor project
float angle;
// import libraary for LCD
#include<LiquidCrystal.h>

LiquidCrystal lcd(A0,A1,A2,A3,A4,A5);

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop()
{
  // Read input values from LDRs
  int bval0 = digitalRead(0);
  int bval1 = digitalRead(2);
  int bval2 = digitalRead(3);
  int bval3 = digitalRead(4);
  int bval4 = digitalRead(5);
  int bval5 = digitalRead(6);
  int bval6 = digitalRead(7);
  int bval7 = digitalRead(8);
  int bval8 = digitalRead(9);
  
  // get decimal value
  
  angle = (bval0*(256)) + (bval1*(128)) + (bval2*(64)) + (bval3*(32)) + (bval4*(16)) + (bval5*(8)) + (bval6*(4)) + (bval7*(2)) + (bval8);     
 
  Serial.println(angle);
  
  lcd.setCursor(0,0);
  lcd.println("Angle = ");
  lcd.print(angle);
}
