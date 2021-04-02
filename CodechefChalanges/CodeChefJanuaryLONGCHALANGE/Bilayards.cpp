#include<iostream>
using namespace std;
int main(){
    int test_case = 0;
    cin>>test_case;
    while(test_case){
        long long int n,k,i,j,r;
        cin>>n>>k>>i>>j;
        if ((k > 4) && (k%4 != 0)){
            r = k - ((k/4)*4);
        }
        else if (k%4 == 0){
            r = 4;
        }
        else{
            r = k;
        }
        long long int x = 0;
        long long int y = 0;
        if(j>i){
            switch(r){
                case 1:
                    x = i+(n-j);
                    y = n;
                    break;
                
                case 2:
                    x = n;
                    y = i+(n-j);
                    break;
                
                case 3:
                    x = j-i;
                    y = 0;
                    break;
                
                case 4:
                    x = 0;
                    y = j-i;
                    break;
            }
        }
        else if (i > j){
            switch(r){
                case 1:
                    x = n;
                    y = j+(n-i);
                    break;
                
                case 2:
                    x = j+(n-i);
                    y = n;
                    break;
                
                case 3:
                    x = 0;
                    y = i-j;
                    break;
                
                case 4:
                    x = i-j;
                    y = 0;
                    break;
                
            }
        }
        else{
            x = n;
            y = n;
        }


        cout<<x<<" "<<y<<endl;
        test_case--;
    }
    return 0;
}