import java.util.Arrays;  
import java.util.Random;  
public class LAba {
    public static void main(String[] args) {
        int a = 4;
        int b = 24;
        int c = ((b - a) / 2) + 1;
        int[] I = new int[c];
        for (int i = 0; i < c; i++) {
            I[i] = a + 2 * i;
        }
    {
    float[] x = new float[10];
    Random rand = new Random();
    float min = -8.0f;
    float max = 3.0f;

    for (int i = 0; i < 10; i++) {
                x[i] = min + rand.nextFloat()*(max-min) ;
            }
    double [][] s=new double  [11][10];
    for (int i = 0; i < 11; i++) {
    for (int j = 0; j < 10; j++) {
    double  currentX = x[j];
    if (i < I.length && I[i] == 6) {  
         s[i][j] = Math.sin(Math.tan(Math.asin((currentX-2.5)/11)));
         }
            else if (i < I.length && Arrays.asList(8, 12, 14, 18, 22).contains(I[i])) {  
          s[i][j] = Math.log(Math.exp(Math.tan(currentX)-1));
          }
            else {  
             s[i][j] = Math.tan(Math.pow(Math.log(Math.abs(currentX)), 1.0/3.0)) / 2.0;;
           }
        }
    }
            for (double [] row : s) {  
                for (double  value : row) {  
                    System.out.printf("%.5f ", value);  
                }  
                System.out.println();  
            }
        }
    }
 }