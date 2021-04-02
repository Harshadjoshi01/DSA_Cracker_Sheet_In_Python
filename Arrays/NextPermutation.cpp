#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
bool is_greater(int x, int y){
    bool var = (x >= y) ? true : false;
    return var;
}
int * digit_array(int x, int arr[], int len){
    int i = len-1;
    while(x){
        int y = x%10;
        arr[i] = y;
        i--;
        x = x/10;
    }
    return arr;
}

int main(){
    int var = 987654321;
    string num = to_string(var);
    int len = num.length();
    int digit_arr[len];
    int *p = digit_array(var, digit_arr, len);
    for (int i = len-1; i >= 1; i--){
        bool variable = is_greater(p[i-1],p[i]);
        if (variable){
            continue;
        } else {
            swap(p[i-1], p[len-1]);
            sort(p+i,p+len);
            break;

        }
    }
    for (int i = 0; i < len; i++) {
        cout<<p[i]<<" ";
    }
    return 0;
}