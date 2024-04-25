#define factor(n) do {\
							int i;\
                            printf("Factors of %d are: ", n);\
                            for (i = 1; i <= n; i++) {\
                                if (n % i == 0) {\
                                    printf("%d ", i);\
                                }\
                            }\
                            printf("\n");\
                        } while(0)

