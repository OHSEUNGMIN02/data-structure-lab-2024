#pragma once
#include <cstdio>
#include <stdio.h>
#include <string.h>


class Car {
protected:
    int speed;
    char name[40];
public:
    int gear;
    Car(){ }
    ~Car(){ }
    Car(int s, const char* n, int g)
        : speed(s), gear(g) {
        strcpy_s(name, n);
    }
    void changeGear(int g = 4) {
        gear = g;
    }
    void speedUp() {
        speed += 5;
    }
    void display() {
        printf("[%s] : 기어=%d단 속도=%dkmph\n", name, gear, speed);
    }
    void whereAmI() { 
        printf("객체 주소 = %x\n", this); 
    }
    
};