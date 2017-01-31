#include <stdio.h>
#include <math.h>
#include <cmath>
#include <iostream>

double f (double x) {
    return (cos(x) + sin(50 * x) * sin (50 * x));
}

double fprime (double x) {
    return (100 * sin (50 * x) * cos (50 * x) - sin(x));
}

double g (double f1 (double y), double f2 (double y), double x) {
    double z_1, z_2;

    z_1 = f1(x);
    z_2 = f2(x);

    return (x - z_1/z_2);
}

int main () {
    int i, Numstep;
    double pi2, x, xnew, x_0, INCR, TOL;
    FILE *pFile_x, *pFile_steps, *pFile_fail;

    Numstep = 100;
    TOL = 1e-8;
    INCR = .0001;
    pi2 = M_PI/2;
    x_0 = pi2 - .1;
    pFile_x = fopen("Xinitial.txt", "w");
    pFile_steps = fopen("Numsteps.txt", "w");
    pFile_fail = fopen("Fail.txt", "w");

    while(x_0 < pi2 + .1) {
        x = x_0;
        for (i = 0; i < Numstep; i++) {
            xnew = g(f, fprime, x);

            if (std::abs(x - pi2) < TOL) {
//                printf("Step = %i, x_0 = %lg, and x_final = %lg.\n", 
//                        i, x_0, x);
                fprintf(pFile_x, "%lg\n", x_0);
                fprintf(pFile_steps, "%i\n", i);
                break;
            }
    
            x = xnew;
        }

        if(i == Numstep) {
//            printf("Newton's method failed to converge for x_0 = %lg.\n", x_0);
            fprintf(pFile_fail, "%lg\n", x_0);
        }

        x_0 += INCR;
    }

    fclose(pFile_x);
    fclose(pFile_steps);
    fclose(pFile_fail);
    return 0;
}
