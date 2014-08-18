//modified from http://blog.prashanthellina.com/2008/01/07/interfacing-python-with-c-using-ctypes/

int add(int a, int b)
{
    return(a+b);
}

int sum_values(int *values, int n_values)
{
    int i;
    int sum = 0;

    for (i=0; i<n_values; i++){
        sum+=values[i];
    }
}
