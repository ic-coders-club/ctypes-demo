#include <iostream>


struct MyStruct {
    int x; 
    double y;
};


extern "C"{

double add_doubles(double a, double b){
    return a+b;
}

void cout_string(const char * s){
    std::cout << s << std::endl;
}

double sum_doubles(double * double_array, int n_doubles){
    double sum = 0;
    for (int i=0; i<n_doubles; i++){
        sum += double_array[i];
    }
    return sum;
}

void fill_my_struct(int a, double b, MyStruct * myStruct ){
    myStruct->x = a;
    myStruct->y = b;
}

}
