#include<bits/stdc++.h>
using namespace std;

long long int fun(long long int x, long long int y, long long int z){
    if (x==y==z){
        return 0;
    }
    long long int result = abs(x-y) + abs(y-z) + abs(z-x);
    return result;
}
int main(){
    int t;
    cin>>t;
    while(t){
        int n;
        cin>>n;
        long long int arr[n];
        for (int i = 0; i < n; i++){
            cin>>arr[i];
        }
        sort(arr, arr+n);
        long long int max_value = fun(arr[0], arr[1], arr[n-1]);
        cout<<max_value<<endl;
        t--;

    }
    
    return 0;
}