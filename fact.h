#define Factorial(n)({\
    int result =1;\
    for (int i=1;i<=n;i++)\
        result *=i;\
    result;\
})