#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;
    int arr[n];
    for (int i = 0; i < n; i++){
        cin>>arr[i];
    }
    int jump = 0;
    int idx = 0;
    while(idx<n-1){
        if(arr[idx] == 1){
            idx += arr[idx];
            cout<<idx<<endl;
            jump += 1;
        }
        else{
            sort(arr+idx+1, arr+arr[idx]+1);
            idx += arr[idx];
            cout<<idx<<endl;
            jump += 1;
        }
    }
    cout<<jump<<endl;
    for (int i = 0; i < n; i++){   //Making an array
        cout<<arr[i]<<" ";
    }
    return 0;
}