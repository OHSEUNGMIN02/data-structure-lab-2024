#pragma once

#include <cstdio>

class Complex
{
	double real;
	double imag;
public:
	void set(double r, double i) {
		real = r;
		imag = i;
	}
	void read(char* msg = "º¹¼Ò¼ö =") {
		printf(" %s ", msg);
		scanf("%1f%1f", &real, &imag);
    }
	void 
}